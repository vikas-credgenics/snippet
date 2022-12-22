from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

# from accounts.events import UserChangePassword
from user.serializers import LoginSerializer, RegisterSerializer


class Register(generics.CreateAPIView):
    """
        Register a new user to system
    """

    serializer_class = RegisterSerializer
    model = User

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                serializer.data['username'],
                serializer.data['email'],
                serializer.data['password']
            )

            user.first_name = serializer.data.get('first_name', '')
            user.last_name = serializer.data.get('last_name', '')
            user.save()

            new_user = authenticate(username=serializer.data['username'],
                                    password=serializer.data['password'])

            # login(request, new_user)

            token = Token.objects.get_or_create(user=user)[0].key

            return Response(
                {
                    'token': token,
                    'first_name': new_user.first_name,
                    'last_name': new_user.last_name
                },
                status=status.HTTP_200_OK
            )

        else:
            return Response(
                {
                    'user': serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class Login(generics.GenericAPIView):
    """
        Login a existing user to system
    """
    serializer_class = LoginSerializer
    token_model = Token

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = authenticate(username=serializer.data['username'],
                                password=serializer.data['password'])
            print (user)
            if user and user.is_authenticated:
                if user.is_active:
                    # login(request, user)

                    token = self.token_model.objects.get_or_create(user=user)[0].key

                    # Update last login time
                    user.last_login = timezone.now()
                    user.save(update_fields=['last_login'])

                    return Response(
                        {
                            'token': token,
                            'first_name': user.first_name,
                            'last_name': user.last_name
                        },
                        status=status.HTTP_200_OK
                    )
                else:
                    return Response(
                        {
                            'error': ['This account is disabled.']
                        },
                        status=status.HTTP_401_UNAUTHORIZED
                    )
            else:
                return Response(
                    {
                        'error': ['Invalid Username/Password.']
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    """
        Logout a logged in user to system
    """

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        try:
            # request.user.auth_token.delete()
            logout(request)
            return Response({'success': 'Successfully logged out.'},
                            status=status.HTTP_200_OK)
        except Exception as e:
            print (e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
from django.shortcuts import render

# Create your views here.
