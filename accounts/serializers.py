from django.contrib.auth.models import User
from rest_framework import serializers

from accounts.models import Accounts
# from rest_framework.compat import MinLengthValidator


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128)


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, max_length=100)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'username')
        write_only_fields = ('password',)

    def update(self, instance, validated_data):
        """hack for pwdValidationError

        :param validated_data:
        :param instance:
        """

        assert instance is None, 'Cannot update users with RegisterSerializer'
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        return user

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    @staticmethod
    def validate_email(value):
        if value and User.objects.filter(email=value).count():
            raise serializers.ValidationError("Email Already Exist")
        else:
            return value


class AccountsSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Accounts
        fields = ("id", 'account_type', 'account_category', 'account_id', 'provider_name')
