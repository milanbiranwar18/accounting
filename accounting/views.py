import logging

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from accounting.models import Customer, Account, Transaction
from accounting.serializers import CustomerSerializer, AccountSerializer, TransactionSerializer




class CreateCustomer(APIView):
    """
     Class for customer curd operation
    """

    def post(self, request):
        try:
            serializer = CustomerSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Customer Created Successfully", "data": serializer.data, "status": 201})
        except Exception as e:
            logging.error(e)
            return Response({"message": str(e)}, status=400)

    def get(self, request):
        try:
            customer = Customer.objects.filter(user=request.user.id)
            serializer = CustomerSerializer(customer, many=True)
            return Response({"message": "All Customers are", "data": serializer.data, "status": 200})
        except Exception as e:
            logging.error(e)
            return Response({"message": str(e)}, status=400)

    def put(self, request, id):
        try:
            customer = Customer.objects.get(id=id)
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Customer Updated Successfully", "data": serializer.data, "status": 200})
        except Exception as e:
            logging.error(e)
            return Response({"message": str(e)}, status=400)

    def delete(self, request, id):
        try:
            customer = Customer.objects.get(id=id)
            customer.delete()
            return Response({"message": "Customer deleted Successfully", "status": 200})
        except Exception as e:
            logging.error(e)
            return Response({"message": str(e)}, status=400)


class CreateAccount(APIView):
    """
     Class for account curd operation
    """

    def post(self, request):
        try:
            serializer = AccountSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Account Created Successfully", "data": serializer.data, "status": 201})
        except Exception as e:
            logging.error(e)
            return Response({"message": str(e)}, status=400)

    def get(self, request):
        try:
            account = Account.objects.filter(user=request.user.id)
            serializer = CustomerSerializer(account, many=True)
            return Response({"message": "All accounts are", "data": serializer.data, "status": 200})
        except Exception as e:
            logging.error(e)
            return Response({"message": str(e)}, status=400)

    def put(self, request, id):
        try:
            account = Account.objects.get(id=id)
            serializer = CustomerSerializer(account, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Account Updated Successfully", "data": serializer.data, "status": 200})
        except Exception as e:
            logging.error(e)
            return Response({"message": str(e)}, status=400)

    def delete(self, request, id):
        try:
            account = Account.objects.get(id=id)
            account.delete()
            return Response({"message": "Customer deleted Successfully", "status": 200})
        except Exception as e:
            logging.error(e)
            return Response({"message": str(e)}, status=400)


class CreateTransactions(APIView):
    """
     Class for Transaction curd operation
    """

    def post(self, request):
        try:
            serializer = TransactionSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Transaction Created Successfully", "data": serializer.data, "status": 201})
        except Exception as e:
            logging.error(e)
            return Response({"message": str(e)}, status=400)

    def get(self, request):
        try:
            transaction = Transaction.objects.filter(user=request.user.id)
            serializer = TransactionSerializer(transaction, many=True)
            return Response({"message": "All Transactions are", "data": serializer.data, "status": 200})
        except Exception as e:
            logging.error(e)
            return Response({"message": str(e)}, status=400)

    def put(self, request, id):
        try:
            transaction = Transaction.objects.get(id=id)
            serializer = TransactionSerializer(transaction, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Transaction Updated Successfully", "data": serializer.data, "status": 200})
        except Exception as e:
            logging.error(e)
            return Response({"message": str(e)}, status=400)

    def delete(self, request, id):
        try:
            transaction = Transaction.objects.get(id=id)
            transaction.delete()
            return Response({"message": "Transaction deleted Successfully", "status": 200})
        except Exception as e:
            logging.error(e)
            return Response({"message": str(e)}, status=400)

