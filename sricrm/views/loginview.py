from drf_yasg.utils import swagger_auto_schema
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from rest_framework.response import Response
from rest_framework import permissions
from sricrm.serializers.loginserializer import LoginSerializer
from sricrm.models.organization import Organization
from sricrm.models.company import Company
from drf_yasg.utils import swagger_auto_schema

class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        _, token = AuthToken.objects.create(user)
        # token_obj, token = AuthToken.objects.create(user)
        print(f"Token Length: {len(token)}")
        print("Generated token:", token)
        print("Token length:", len(token))
        if user.is_user_id:
            login_type = "User"
        elif user.is_org_id:
            login_type = "Organization"
        elif user.is_com_id:
            login_type = "Company"
        else:
            login_type = "Unknown"

        return Response({
            "message": "Login successful",
            "user_type": login_type,
            "token": token
        })