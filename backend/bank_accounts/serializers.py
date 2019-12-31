from rest_framework.serializers import ModelSerializer
from .models import BankAccount

class BankAccountSerializer(ModelSerializer):
  class Meta:
    model = BankAccount
    fields = ['owner', 'name', 'type']