import logging

from rest_framework import serializers
from rest_framework.response import Response

from accounting.models import Customer, Account, Transaction
from user.models import User


class CustomerSerializer(serializers.ModelSerializer):
    """
     Class for Customer serializer
    """

    class Meta:
        model = Customer
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    """
     Class for Account serializer
    """

    class Meta:
        model = Account
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    """
     Class for Transaction serializer
    """

    class Meta:
        model = Transaction
        fields = "__all__"