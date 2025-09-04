from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime




class VerifiedEmail(models.Model):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email} - Verified: {self.is_verified}"
