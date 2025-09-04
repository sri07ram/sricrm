from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from sricrm.serializers.registerserializer import UserRegisterSerializer
from sricrm.models.verifiedemail import VerifiedEmail
from sricrm.models.organization import Organization
from sricrm.models.company import Company

class UserView(APIView):
    @swagger_auto_schema(request_body=UserRegisterSerializer)
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get("email")

            try:
                verified = VerifiedEmail.objects.get(email=email)
                if not verified.is_verified:
                    return Response({"error": "Email is not verified"}, status=400)
            except VerifiedEmail.DoesNotExist:
                return Response({"error": "Email is not verified"}, status=400)

            # Validate org_id & com_id
            org_id = request.data.get("org_id")
            com_id = request.data.get("com_id")

            try:
                org = Organization.objects.get(org_id=org_id)
            except Organization.DoesNotExist:
                return Response({"error": "Invalid org_id"}, status=400)

            try:
                com = Company.objects.get(com_id=com_id)
            except Company.DoesNotExist:
                return Response({"error": "Invalid com_id"}, status=400)

            user = serializer.save()
            user.org = org
            user.com = com
            user.save()

            return Response({
                "message": "User registered successfully",
                "user_id": user.user_id,
                "email": user.email,
                "username": user.username,
                "role":user.role,
                "org_id": org.org_id,
                "com_id": com.com_id,
            }, status=201)

        return Response(serializer.errors, status=400)
