from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import BankAccount, Transaction

class BankAccountSerializer(ModelSerializer):
  transactions = PrimaryKeyRelatedField(many=True, queryset=Transaction.objects.all())
  class Meta:
    model = BankAccount
    fields = ['owner', 'name', 'type', 'transactions']