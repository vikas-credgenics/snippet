from django.db import models
from django.contrib.auth.models import User


class RewardWalletSummary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)


class RewardRules(models.Model):
    entity = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    sub_category = models.CharField(max_length=255)
    conversion_factor = models.FloatField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class RewardTransactionDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rule = models.ForeignKey(RewardRules, on_delete=models.CASCADE, null=True, blank=True)
    txn_type = models.CharField(max_length=8, choices=(("earn", "earn"), ("burn", "burn"), ("load", "load")))
    conversion_factor = models.FloatField(null=True, blank=True)
    reference_field = models.TextField(null=True, blank=True)
    amount = models.FloatField(default=0, null=True, blank=True)
    points = models.FloatField(null=True, blank=True)
    remarks = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
