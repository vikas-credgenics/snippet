from rest_framework import serializers


class GetAmountSerializer(serializers.Serializer):
    account_id = serializers.IntegerField()


class GetPrincipalOutstandingAmountSerializer(serializers.Serializer):
    account_id = serializers.IntegerField()


class GetForeclosureAmountSerializer(serializers.Serializer):
    account_id = serializers.IntegerField()


class BBPSPaymentStatusSerializer(serializers.Serializer):
    amount = serializers.FloatField()
    points = serializers.FloatField(required=False)
    lender_id = serializers.IntegerField()
    account_id = serializers.IntegerField()


class GetBBPSDuePaymentSerializer(serializers.Serializer):
    account_id = serializers.IntegerField()
