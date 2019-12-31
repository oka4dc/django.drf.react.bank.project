from django.contrib.admin import register, ModelAdmin, TabularInline
from .models import BankAccount, Transaction

class TransactionInline(TabularInline):
  model = Transaction

# Register your models here.
@register(BankAccount)
class BankAccountAdmin(ModelAdmin):
  inlines = [TransactionInline]
