from django.db import models
from django.contrib.auth.models import User
from sricrm.models.company import Company


class Organization(models.Model):
    org_id = models.CharField(max_length=10, primary_key=True,blank=True)
    org_name = models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(unique=True,null=True)

    def save(self, *args, **kwargs):
        if not self.org_id:
            last_org = Organization.objects.all().order_by('org_id').last()
            if last_org:
                num = int(last_org.org_id.replace('org', '')) + 1
            else:
                num = 1
            self.org_id = f"org{num:03d}"
        super().save(*args, **kwargs)

