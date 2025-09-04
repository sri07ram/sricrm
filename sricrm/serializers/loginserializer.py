from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.db.models import Q
from sricrm.models.USER import Users

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        try:
            user = Users.objects.get(email=email)
        except Users.DoesNotExist:
            raise serializers.ValidationError("User not found.")

       # if not check_password(password, user.password):
        #    raise serializers.ValidationError("Invalid credentials.")

        data["user"] = user
        return data
