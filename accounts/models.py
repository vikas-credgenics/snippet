from django.db import models
from django.contrib.auth.models import User


class Accounts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=255)
    account_category = models.CharField(max_length=255)
    account_id = models.CharField(max_length=255)
    provider_name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
