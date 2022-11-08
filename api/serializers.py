from uuid import uuid4
from django.contrib.auth.hashers import check_password, make_password
from django.db import transaction
from .utils import get_random_string, send_sms
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer

from .models import User


class UserRegisterSerializer(RegisterSerializer, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'phone',
            # 'image',
            'street',
            'country',
            'email',
            'delivery_address',
            'delivery_address_two',
            'delivery_address_two',
            'password1',
            'password2'
        ]
        extra_kwargs = {
            'password1': {'write_only': True},
        }

    @transaction.atomic
    def save(self, request, *args, **kwargs):
        data = self.data
        user = super().save(request)
        user.username = "{0}_{1}_{2}".format(
            data.get('first_name'),
            data.get('last_name'),
            get_random_string(6)
        ),
        user.first_name = data.get('first_name', '')
        user.last_name = data.get('last_name', '')
        user.phone = data.get('phone')
        user.email = data.get('email')
        user.save()
        return user


class UserLoginSerializer(LoginSerializer):
    id = serializers.UUIDField(default=uuid4)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    email = serializers.CharField(required=True)
    email_is_verified = serializers.BooleanField(default=False)

    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'first_name',
            'last_name',
            'id',
            'rc_number',
            'phone',
            'blood_group',
            'account_type',
            'center_name'
        ]
        read_only_fields = [
            'first_name',
            'last_name',
            'id',
            'rc_number',
            'phone',
            'blood_group',
            'account_type',
            'center_name'
        ]
