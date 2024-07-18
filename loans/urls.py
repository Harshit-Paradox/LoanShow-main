from django.contrib import admin
from django.urls import path 
from .views import LoanListView , HomeLoanDataListView  , index

urlpatterns = [
    path('', index, name='index'),
    path("admin/", admin.site.urls),
    path('api/loans/', LoanListView.as_view(), name='loan-list'),
    path('api/loans/homeloan/', HomeLoanDataListView.as_view(), name='Homeloan-list'),
]
