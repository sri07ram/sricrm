from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.hashers import make_password
from sricrm.serializers.organizationserializer import OrganizationSerializer
from sricrm.models.organization import Organization
from sricrm.models.USER import Users
from sricrm.models.verifiedemail import VerifiedEmail
from sricrm.models.company import Company

#organization view
class OrganizationView(APIView):
    @swagger_auto_schema(request_body=OrganizationSerializer)
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        com_data = request.data.get("com", [])

        try:
            verified = VerifiedEmail.objects.get(email=email)
            if not verified.is_verified:
                return Response({"error": "Email is not verified"}, status=400)
        except VerifiedEmail.DoesNotExist:
            return Response({"error": "Email is not verified"}, status=400)

        data = request.data.copy()
        data['password'] = make_password(password)

        org_serializer = OrganizationSerializer(data=data)
        if org_serializer.is_valid():
            org = org_serializer.save()

            Users.objects.create(
                email=email,
                is_org_id=True,
                org=org
            )

            for com in com_data:
                Company.objects.create(
                    com_id=com.get("com_id"),
                    com_name=com.get("com_name"),
                    email=com.get("email"),
                    password=make_password(com.get("password")),
                    org=org
                )

            return Response({
                "message": "Organization registered successfully",
                "org_id": org.org_id,
                "email": org.email,
            }, status=201)

        return Response(org_serializer.errors, status=400)

    def get(self, request, org_id):
        try:
            org = Organization.objects.get(org_id=org_id)
        except Organization.DoesNotExist:
            return Response({'error': 'Invalid org_id'}, status=404)

        serializer = OrganizationSerializer(org)
        return Response(serializer.data)