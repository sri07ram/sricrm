from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from sricrm.serializers.otpverifyserializer import OTPVerifySerializer
from sricrm.models.verifiedemail import VerifiedEmail
from rest_framework.response import Response

class OTPVerifyAPIView(APIView):

    @swagger_auto_schema(request_body=OTPVerifySerializer)
    def post(self, request):
        serializer = OTPVerifySerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "OTP verified successfully"}, status=200)
        return Response(serializer.errors, status=400)