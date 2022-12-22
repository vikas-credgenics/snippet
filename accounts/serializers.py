from django.contrib.auth.models import User
from rest_framework import serializers
from accounts.models import Accounts


class AccountsSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Accounts
        fields = ("id", 'account_type', 'account_category', 'account_id', 'provider_name')
