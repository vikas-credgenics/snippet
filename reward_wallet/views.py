from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from reward_wallet.models import RewardWalletSummary, RewardRules, RewardTransactionDetails
from reward_wallet.serializers import RewardWalletEarnSerializer, RewardBalanceSerializer, RewardTransactionSerializer, \
    RewardWalletBurnSerializer, RewardWalletLoadSerializer


class RewardWalletBalance(APIView):
    """
        Reward Wallet for User
    """

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        accounts = RewardWalletSummary.objects.filter(user=request.user).first()
        serializer = RewardBalanceSerializer(accounts)
        return Response(serializer.data)


class RewardWalletTransaction(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        transactions = RewardTransactionDetails.objects.filter(user=request.user).order_by('created')
        serializer = RewardTransactionSerializer(transactions, many=True)
        return Response(serializer.data)


class RewardWalletEarnAPI(APIView):
    """
    Reward Wallet Earn
    """

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = RewardWalletEarnSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {
                    "message": "Bad request"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        valid_data = serializer.validated_data

        reward_rule = RewardRules.objects.filter(entity=valid_data["entity"],
                                                 category=valid_data["category"],
                                                 sub_category=valid_data["sub_category"]).first()

        conversion_factor = reward_rule.conversion_factor
        points = valid_data["amount"] * conversion_factor
        db_data = {
            "user": request.user.id,
            "rule": reward_rule.id,
            "txn_type": "earn",
            "conversion_factor": conversion_factor,
            "reference_field": valid_data.get("reference_field"),
            "amount": valid_data["amount"],
            "points": points,
            "remarks": valid_data.get("remarks")
        }

        serializer = RewardTransactionSerializer(data=db_data)
        if serializer.is_valid():
            serializer.save()
            reward_wallet_summary, _ = RewardWalletSummary.objects.get_or_create(user=request.user, defaults={'balance': 0})
            reward_wallet_summary.balance = reward_wallet_summary.balance + points
            reward_wallet_summary.save()
            return Response(
                {
                    "message": "Success"
                },
                status=status.HTTP_200_OK
            )

        return Response(
            {
                "message": "Failed"
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


class RewardWalletBurnAPI(APIView):
    """
    Reward Wallet Earn
    """

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = RewardWalletBurnSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response(
                {
                    "message": "Bad request"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        valid_data = serializer.validated_data

        reward_rule = RewardRules.objects.filter(entity=valid_data["entity"],
                                                 category=valid_data["category"],
                                                 sub_category=valid_data["sub_category"]).first()

        conversion_factor = reward_rule.conversion_factor
        # points = valid_data["amount"] * conversion_factor
        db_data = {
            "user": request.user.id,
            "rule": reward_rule.id,
            "txn_type": "earn",
            "conversion_factor": reward_rule.conversion_factor,
            "reference_field": valid_data.get("reference_field"),
            "points": valid_data["point"],
            # "points": points,
            "remarks": valid_data.get("remarks")
        }

        serializer = RewardTransactionSerializer(data=db_data)
        if serializer.is_valid():
            serializer.save()
            reward_wallet_summary, _ = RewardWalletSummary.objects.get_or_create(user=request.user, defaults={'balance': 0})
            reward_wallet_summary.balance = reward_wallet_summary.balance - valid_data["point"]
            reward_wallet_summary.save()
            return Response(
                {
                    "message": "Success"
                },
                status=status.HTTP_200_OK
            )

        return Response(
            {
                "message": "Failed"
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


class RewardLoadAPI(APIView):
    """
    Reward Wallet Load
    """

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = RewardWalletLoadSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {
                    "message": "Bad request"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        valid_data = serializer.validated_data

        db_data = {
            "user": request.user.id,
            "txn_type": "load",
            "amount": valid_data["amount"],
            "remarks": "Load Balance"
        }

        serializer = RewardTransactionSerializer(data=db_data)
        if serializer.is_valid():
            serializer.save()
            reward_wallet_summary, _ = RewardWalletSummary.objects.get_or_create(user=request.user, defaults={'balance': 0})
            reward_wallet_summary.balance = reward_wallet_summary.balance + valid_data["amount"]
            reward_wallet_summary.save()
            return Response(
                {
                    "message": "Success"
                },
                status=status.HTTP_200_OK
            )
        print(serializer.errors)
        return Response(
            {
                "message": "Failed"
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )