from django.db import models

class Company(models.Model):
    com_id = models.CharField(max_length=20, primary_key=True, blank=True)
    com_name = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True)
    org = models.ForeignKey(
        'sricrm.Organization',
        related_name='com',
        on_delete=models.CASCADE,
        null=True
    )
    org_type = models.CharField(max_length=50, null=True)

    def save(self, *args, **kwargs):
        if not self.com_id:
            last_com = Company.objects.order_by('-com_id').first()
            if last_com and last_com.com_id.startswith("com"):
                try:
                    last_num = int(''.join(filter(str.isdigit, last_com.com_id)))
                except ValueError:
                    last_num = 0
            else:
                last_num = 0

            self.com_id = f"com{last_num + 1:03d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.com_id} - {self.com_name}"
