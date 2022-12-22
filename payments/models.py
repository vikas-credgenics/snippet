from django.db import models


class BBPSRepaymentSchedule(models.Model):
    lender_id = models.CharField(max_length=64)
    account_id = models.IntegerField()
    year = models.CharField(max_length=64)
    month = models.CharField(max_length=64)
    status = models.CharField(max_length=64, choices=(("PAID", "PAID"), ("DUE", "DUE")))
    due_date = models.DateField(null=True, blank=True)
    principal_outstanding_amount = models.FloatField()
    foreclosure_amount = models.FloatField()
    outstanding_amount = models.FloatField()
