from sricrm.models.verifiedemail import VerifiedEmail
from rest_framework import serializers
from sricrm.models.otpgenerate import OTPGenerate


class OTPVerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp_code = serializers.CharField(max_length=6)

    def validate(self, data):
        email = data['email']
        otp_code = data['otp_code']

        try:
            otp = OTPGenerate.objects.filter(email=email, otp_code=otp_code).first()
        except OTPGenerate.DoesNotExist:
            raise serializers.ValidationError("Invalid OTP or email.")

        if not otp:
            raise serializers.ValidationError("Invalid OTP or email.")

        if otp.is_expired():
            raise serializers.ValidationError("OTP has expired.")

        verified, _ = VerifiedEmail.objects.get_or_create(email=email)
        verified.is_verified = True
        verified.save()

        return data
