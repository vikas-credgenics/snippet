from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from accounts.models import Accounts
from accounts.serializers import AccountsSerializer


class AccountManagement(APIView):
    """
        Account Management for User
    """

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        accounts = Accounts.objects.filter(user=request.user)
        serializer = AccountsSerializer(accounts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AccountsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
