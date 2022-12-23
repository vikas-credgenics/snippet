from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()
    website = models.CharField(max_length=255)
    headquarters = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    service_rating = models.IntegerField()
    response_time_rating = models.IntegerField()
    digitisation_rating = models.IntegerField()
    customer_support_rating = models.IntegerField()
    overall_rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

