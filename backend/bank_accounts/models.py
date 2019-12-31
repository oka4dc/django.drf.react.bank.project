from django.conf import settings
from django.db.models import Model, ForeignKey, CASCADE, CharField, IntegerField

# Create your models here.

account_types = (("CHK", "Checking"), ("SVG", "Savings"))

class BankAccount(Model):
  owner = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
  name = CharField(max_length=255)
  type = CharField(max_length=3, choices=account_types)

  def __str__(self):
    return self.name

transaction_types = (("DEP", "Deposit"), ("WTH", "Withdrawal"))

class Transaction(Model):
  account = ForeignKey(BankAccount, on_delete=CASCADE)
  type = CharField(max_length=3, choices=transaction_types)
  amount = IntegerField()