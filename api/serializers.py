from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('roles', 'first_name', 'last_name',
                  'username', 'email', 'tel', 'password')

    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            tel=validated_data['tel'],
            username=validated_data['username'])

        user.set_password(validated_data['password'])
        user.is_staff = False
        user.save()
        slectedroles = validated_data['roles']
        roles = Roles.objects.filter(name__in=slectedroles)
        for role in roles:
            user.roles.add(role)
        user.save()
        Token.objects.create(user=user)
        return user


class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = '__all__'


class RidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rides
        fields = '__all__'


class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'
