from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from sricrm.models.organization import Organization
from sricrm.models.USER import Users
from sricrm.serializers.companyserializer import CompanySerializer

class OrganizationSerializer(serializers.ModelSerializer):
    com = CompanySerializer(many=True, read_only=True)
    password = serializers.CharField(write_only=True)
    com_count = serializers.SerializerMethodField()
    user_count = serializers.SerializerMethodField()
    com_summary = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = ['org_id', 'email', 'org_name', 'password','com_count','user_count','com_summary', 'com']
        read_only_fields = ['org_id']

    def create(self, validated_data):
        password = validated_data.pop('password')
        email = validated_data.get('email')
        org_name = validated_data.get('org_name')

        if Organization.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Email already exists"})

        org = Organization.objects.create(
            email=email,
            org_name=org_name,
            password=make_password(password)
        )
        return org


    def get_com_count(self,obj):
        return obj.com.count()
    def get_user_count(self,obj):
        return Users.objects.filter(org=obj).count()
    def get_com_summary(self,obj):
        companies = obj.com.all().order_by('com_id')
        summary = []
        for i, com in enumerate(companies, start=1):
            summary.append({
                "sno": i,
                "com_id": com.com_id,
                "com_name": com.com_name,
                "user_count": com.users.count(),
            })
        return summary