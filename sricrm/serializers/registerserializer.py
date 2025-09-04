from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from sricrm.models.USER import Users
from sricrm.models.organization import Organization
from sricrm.models.company import Company


class UserRegisterSerializer(serializers.ModelSerializer):
    org_id = serializers.CharField(write_only=True)
    com_id = serializers.CharField(write_only=True)
    role = serializers.CharField(write_only=True)
    class Meta:
        model = Users
        fields = ['user_id', 'email', 'username','role', 'org_id','com_id']

    def create(self, validated_data):
        org_id = validated_data.pop("org_id")
        com_id = validated_data.pop("com_id")
        role = validated_data.pop('role')
        try:
            org = Organization.objects.get(org_id=org_id)
        except Organization.DoesNotExist:
            raise serializers.ValidationError({"error": "Invalid org_id"})

        try:
            com = Company.objects.get(com_id=com_id)
        except Company.DoesNotExist:
            raise serializers.ValidationError({"error": "Invalid com_id"})

        user = Users.objects.create(
            email=validated_data["email"],
            username=validated_data["username"],
            #org=org,
            #com=com,
            is_user_id=(role == 'user'),
            is_org_id=(role == 'org'),
            is_com_id=(role == 'company'),
        )
        #user.save()
        return user
