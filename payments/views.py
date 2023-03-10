import requests
from django.forms.models import model_to_dict
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from payments.models import BBPSRepaymentSchedule
from payments.serializers import GetAmountSerializer, BBPSPaymentStatusSerializer, GetBBPSDuePaymentSerializer
from accounts.models import Accounts


class GetLoanAmount(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        serializer = GetAmountSerializer(data=request.query_params)
        if not serializer.is_valid():
            return Response(
                {
                    "message": "Bad request"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        valid_data = serializer.validated_data
        entry = BBPSRepaymentSchedule.objects.filter(account_id=valid_data["account_id"], status="DUE").first()
        if not entry:
            return Response({}, status.HTTP_200_OK)
        return Response(
            {
                "outstanding_amount": entry.outstanding_amount,
                "principal_outstanding_amount": entry.principal_outstanding_amount,
                "foreclosure_amount": entry.foreclosure_amount,
                "status": entry.status
            },
            status=status.HTTP_200_OK
        )


class BBPSPaymentView(APIView):

    def post(self, request):
        serializer = BBPSPaymentStatusSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response(
                {
                    "message": "Bad request"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        valid_data = serializer.validated_data

        account = Accounts.objects.filter(id=valid_data["account_id"]).first()
        data = {
            "entity": account.provider_name,
            "category": account.account_type,
            "sub_category": account.account_category,
            "reference_field": "BBPS Payment",
            "remarks": "BBPS"
        }
        requests.post(f"http://{request.get_host()}/reward/load/", json={"amount": valid_data["amount"]},
                      headers={"Authorization": request.headers["Authorization"]})
        requests.post(f"http://{request.get_host()}/reward/burn/", json={"point": valid_data.get("points", 0), **data},
                      headers={"Authorization": request.headers["Authorization"]})
        requests.post(f"http://{request.get_host()}/reward/earn/", json={"amount": valid_data["amount"], **data},
                      headers={"Authorization": request.headers["Authorization"]})
        bps = BBPSRepaymentSchedule.objects.filter(account_id=valid_data["account_id"], status='DUE').first()
        if bps:
            bps.status = "PAID"
            bps.save()
        return Response(
            {
                "message": "Paid successfully"
            },
            status=status.HTTP_200_OK
        )

    def get(self, request):
        serializer = GetBBPSDuePaymentSerializer(data=request.query_params)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response(
                {
                    "message": "Bad request"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        valid_data = serializer.validated_data
        entry = BBPSRepaymentSchedule.objects.filter(account_id=valid_data["account_id"], status="DUE").first()
        if not entry:
            return Response(
                {"message": "No due payment"},
                status=status.HTTP_200_OK
            )
        return Response(
            model_to_dict(entry),
            status=status.HTTP_200_OK
        )
