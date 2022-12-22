from rest_framework import serializers


class GetOutstandingAmountSerializer(serializers.Serializer):
    month = serializers.CharField(max_length=2)
    year = serializers.CharField(max_length=4)
    account_id = serializers.IntegerField()


class GetPrincipalOutstandingAmountSerializer(serializers.Serializer):
    month = serializers.CharField(max_length=2)
    year = serializers.CharField(max_length=4)
    account_id = serializers.IntegerField()


class GetForeclosureAmountSerializer(serializers.Serializer):
    month = serializers.CharField(max_length=2)
    year = serializers.CharField(max_length=4)
    account_id = serializers.IntegerField()


class BBPSPaymentStatusSerializer(serializers.Serializer):
    amount = serializers.FloatField()
    account_id = serializers.IntegerField()
    month = serializers.CharField(max_length=2)
    year = serializers.CharField(max_length=4)


class GetBBPSDuePaymentSerializer(serializers.Serializer):
    account_id = serializers.IntegerField()
