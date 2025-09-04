from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from sricrm.serializers.registerserializer import UserRegisterSerializer
from sricrm.serializers.organizationserializer import OrganizationSerializer
from sricrm.serializers.companyserializer import CompanySerializer
from sricrm.models.verifiedemail import VerifiedEmail
from rest_framework.response import Response
from sricrm.models.company import Company
from sricrm.models.USER import Users


class CompanyView(APIView):
    @swagger_auto_schema(request_body=CompanySerializer)
    def post(self, request):
        email = request.data.get("email")

        try:
            verified = VerifiedEmail.objects.get(email=email)
            if not verified.is_verified:
                return Response({"error": "Email is not verified"}, status=400)
        except VerifiedEmail.DoesNotExist:
            return Response({"error": "Email is not verified"}, status=400)

        com_serializer = CompanySerializer(data=request.data)
        if com_serializer.is_valid():
            company = com_serializer.save()

            user = Users.objects.create(
                email=email,
                is_com_id=True,
                com=company
            )

            return Response({
                "message": "Company registered",
                "com_id": company.com_id,
                "email": company.email,
            }, status=201)
        return Response(com_serializer.errors, status=400)
