from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import BankAccount
from .serializers import BankAccountSerializer

class BankAccountList(APIView):
  def get(self, request, format=None):
    bank_accounts = BankAccount.objects.all()
    serializer = BankAccountSerializer(bank_accounts, many=True)
    return Response(serializer.data)