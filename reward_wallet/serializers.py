from rest_framework import serializers
from reward_wallet.models import RewardWalletSummary, RewardTransactionDetails


class RewardWalletEarnSerializer(serializers.Serializer):
    entity = serializers.CharField(max_length=255)
    category = serializers.CharField(max_length=255)
    sub_category = serializers.CharField(max_length=255)
    txn_type = serializers.CharField(default="earn")
    reference_field = serializers.CharField()
    amount = serializers.FloatField()
    remarks = serializers.CharField(max_length=255)


class RewardWalletBurnSerializer(serializers.Serializer):
    entity = serializers.CharField(max_length=255)
    category = serializers.CharField(max_length=255)
    sub_category = serializers.CharField(max_length=255)
    txn_type = serializers.CharField(default="burn")
    reference_field = serializers.CharField()
    point = serializers.FloatField()
    remarks = serializers.CharField(max_length=255)


class RewardWalletLoadSerializer(serializers.Serializer):
    amount = serializers.FloatField()


class RewardBalanceSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = RewardWalletSummary
        fields = ("user", "balance", "id")


class RewardTransactionSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = RewardTransactionDetails
        fields = ("id", "user", "rule", "txn_type", "conversion_factor", "reference_field", "amount", "points",
                  "remarks", "created", "updated")
