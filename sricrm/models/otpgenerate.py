from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime


class OTPGenerate(models.Model):
    email = models.EmailField()
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return timezone.now() > self.created_at + datetime.timedelta(minutes=5)

    def __str__(self):
        return f"{self.email} - {self.otp_code}"