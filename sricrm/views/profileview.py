from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from sricrm.serializers.organizationserializer import OrganizationSerializer
from sricrm.serializers.companyserializer import CompanySerializer
from sricrm.serializers.registerserializer import UserRegisterSerializer
from sricrm.models.USER import Users
from sricrm.models.organization import Organization
from sricrm.models.company import Company
from rest_framework.response import Response
from rest_framework import status

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if user.is_org_id:
            if user.org:
                from sricrm.serializers.organizationserializer import OrganizationSerializer
                serializer = OrganizationSerializer(user.org)
                return Response(serializer.data)

        elif user.is_com_id:
            if user.com:
                from sricrm.serializers.companyserializer import CompanySerializer
                serializer = CompanySerializer(user.com)
                return Response(serializer.data)

        elif user.is_user_id:
            from sricrm.serializers.registerserializer import UserRegisterSerializer
            serializer = UserRegisterSerializer(user)
            return Response(serializer.data)

        return Response({"error": "Invalid user profile"}, status=400)

class ProfileViewByID(APIView):
    def get(self, request, profile_id):
        from sricrm.serializers.organizationserializer import OrganizationSerializer
        from sricrm.serializers.companyserializer import CompanySerializer
        from sricrm.serializers.registerserializer import UserRegisterSerializer

        org_instance = Organization.objects.filter(org_id=profile_id).first()
        if org_instance:
            serializer = OrganizationSerializer(org_instance)
            return Response(serializer.data)

        company_instance = Company.objects.filter(com_id=profile_id).first()
        if company_instance:
            serializer = CompanySerializer(company_instance)
            return Response(serializer.data)

        user_instance = Users.objects.filter(user_id=profile_id).first()
        if user_instance:
            serializer = UserRegisterSerializer(user_instance)
            return Response(serializer.data)

        return Response({"error": "Profile not found"}, status=404)
