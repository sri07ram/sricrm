from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from sricrm.serializers.otpgenerateserializer import GenerateOTPSerializer
from sricrm.models.otpgenerate import OTPGenerate
from rest_framework.response import Response
from rest_framework import  status

import random

class GenerateOTPView(APIView):

    @swagger_auto_schema(request_body=GenerateOTPSerializer)
    def post(self, request):
        serializer = GenerateOTPSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data["email"]

            otp_code = str(random.randint(100000, 999999))

            OTPGenerate.objects.create(email=email, otp_code=otp_code)

            return Response({
                "email": email,
                "otp_code": otp_code,
                "message": "OTP generated successfully"
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
