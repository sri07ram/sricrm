from rest_framework import serializers

class GenerateOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
