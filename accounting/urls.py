from django.urls import path
from . import views


urlpatterns = [
    path('customer/', views.CreateCustomer.as_view(), name='customer'),
    path('account/', views.CreateAccount.as_view(), name='account'),
    path('transaction/', views.CreateTransactions.as_view(), name='transaction'),




]