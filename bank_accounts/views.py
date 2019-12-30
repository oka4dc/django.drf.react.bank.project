from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from .models import BankAccount
from .serializers import BankAccountSerializer

class BankAccountList(ListCreateAPIView):
  queryset = BankAccount.objects.all()
  serializer_class = BankAccountSerializer
  
  def get_queryset(self):
    return BankAccount.objects.all().filter(owner=self.request.user)