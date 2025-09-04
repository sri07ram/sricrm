from rest_framework import serializers
from sricrm.models.company import Company
from sricrm.models.USER import Users
from sricrm.serializers.registerserializer import UserRegisterSerializer
from sricrm.models.organization import Organization


class CompanySerializer(serializers.ModelSerializer):
    users = UserRegisterSerializer(many=True, read_only=True)
    org_id = serializers.CharField(write_only=True)

    class Meta:
        model = Company
        fields = ['email', 'com_name','password', 'users','org_id']

        def create(self, validated_data):
            org_id = validated_data.pop("org_id")
            try:
                org = Organization.objects.get(org_id=org_id)
            except Organization.DoesNotExist:
                raise serializers.ValidationError({"error": "Invalid org_id"})

            user = Users.objects.create(
                email=validated_data["email"],
                 org=org,
                # com=com,
            )
            # user.save()
            return user

