from rest_framework import serializers
from sricrm.models.USER import Users
from sricrm.models.organization import Organization
from sricrm.models.company import Company
from sricrm.serializers.organizationserializer import OrganizationSerializer
from sricrm.serializers.companyserializer import CompanySerializer

class UserProfileSerializer(serializers.ModelSerializer):
    org = serializers.SerializerMethodField()
    com = serializers.SerializerMethodField()

    class Meta:
        model = Users
        fields = ['id', 'name', 'email', 'age', 'org', 'com']

    def get_organization_list(self, obj):
        devs = Organization.objects.filter(user=obj, developer_type="org")
        return OrganizationSerializer(devs, many=True).data
    def get_company_list(self, obj):
        devs = Company.objects.filter(user=obj, developer_type="com")
        return CompanySerializer(devs, many=True).data