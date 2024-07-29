from django.contrib import admin
from django.urls import path 
from .views import LoanListView , HomeLoanDataListView  , index , loginnew , feedback_view, thank_you_view , contact_view,success_view
from loans import views

urlpatterns = [
    path('', index, name='index'),
    path("admin/", admin.site.urls),
    path('signup',views.handleSignup, name='handleSignup'),
    path('login',views.handleLogin, name='handlelogin'),
    path('logout',views.handleLogout, name='handlelogout'),
    path('otp/<str:uid>/', views.otpVerify, name='otp'),
    path('home', views.home, name='home'),
    path('api/loans/', LoanListView.as_view(), name='loan-list'),
    path('api/loans/homeloan/', HomeLoanDataListView.as_view(), name='Homeloan-list'),
    path('login.html',loginnew, name= 'loginnew' ),
    path('feedback/', feedback_view, name='submit_feedback'),
    path('thank-you/', thank_you_view, name='feedback_thank_you'),
    path('contact/', contact_view, name='contact'),
    path('success/', success_view, name='success'),

]



