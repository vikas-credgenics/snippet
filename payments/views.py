from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from payments.models import BBPSRepaymentSchedule
from payments.serializers import GetOutstandingAmountSerializer, GetForeclosureAmountSerializer, \
    GetPrincipalOutstandingAmountSerializer, BBPSPaymentStatusSerializer, GetBBPSDuePaymentSerializer
from django.forms.models import model_to_dict


class OutstandingView(APIView):
    """
        Outstanding Amount
    """

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        serializer = GetOutstandingAmountSerializer(data=request.query_params)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response(
                {
                    "message": "Bad request"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        valid_data = serializer.validated_data
        entry = BBPSRepaymentSchedule.objects.filter(account_id=valid_data["account_id"], year=valid_data["year"],
                                                     month=valid_data["month"]).first()
        return Response(
            {
                "outstanding_amount": entry.outstanding_amount,
                "status": entry.status
            },
            status=status.HTTP_200_OK
        )


class PrincipalOutstandingView(APIView):
    """
        Principal Outstanding Amount
    """

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        serializer = GetPrincipalOutstandingAmountSerializer(data=request.query_params)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response(
                {
                    "message": "Bad request"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        valid_data = serializer.validated_data
        entry = BBPSRepaymentSchedule.objects.filter(account_id=valid_data["account_id"], year=valid_data["year"],
                                                     month=valid_data["month"]).first()
        return Response(
            {
                "principal_outstanding_amount": entry.principal_outstanding_amount,
                "status": entry.status
            },
            status=status.HTTP_200_OK
        )


class ForeclosureAmountView(APIView):
    """
        Principal Outstanding Amount
    """

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        serializer = GetForeclosureAmountSerializer(data=request.query_params)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response(
                {
                    "message": "Bad request"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        valid_data = serializer.validated_data
        entry = BBPSRepaymentSchedule.objects.filter(account_id=valid_data["account_id"], year=valid_data["year"],
                                                     month=valid_data["month"]).first()
        return Response(
            {
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
        BBPSRepaymentSchedule.objects.filter(account_id=valid_data["account_id"], year=valid_data["year"],
                                             month=valid_data["month"]).update(status='PAID')
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
        return Response(
            model_to_dict(entry),
            status=status.HTTP_200_OK
        )
