from django.urls import path
from .views import BankAccountList

urlpatterns = [
    path('', BankAccountList.as_view())
]
