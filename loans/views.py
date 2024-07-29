from django.shortcuts import redirect, HttpResponse, render
from rest_framework import generics
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Loan, HomeLoanData, Profile 
from .serializers import LoanSerializer, HomeLoanDataSerializer
import random
from .helper import MessageHandler
from LoanShow.celery import add 
from loans.tasks import sub
from .forms import FeedbackForm

def index(request):
    return render(request, 'index.html')

def loginnew(request):
    result1=add.delay(10,20)
    print("Result 1 =", result1)
    result2=sub.delay(80,20)
    print("Result 2 =", result2)
    return render(request, 'login.html')



def handleSignup(request):
    if request.method == "POST":
        if User.objects.filter(username__iexact=request.POST['user_name']).exists():
            return HttpResponse("User already exists")

        user = User.objects.create_user(
            username=request.POST['user_name'],
            password=request.POST['password'],
            email=request.POST['email']
        )
        user.save()

        otp = random.randint(1000, 9999)
        phone_number = request.POST.get('phone_number')
        profile = Profile.objects.create(
            user=user,
            phone_number=phone_number,
            otp=f'{otp}',
        )

        messagehandler = MessageHandler(phone_number, otp)
        messagehandler.send_otp_via_message()

        red = redirect(f'otp/{profile.uid}/')
        red.set_cookie("can_otp_enter", True, max_age=600)
        return red

    return render(request, 'index.html')


def otpVerify(request, uid):
    if request.method == "POST":
        profile = Profile.objects.get(uid=uid)

        if request.COOKIES.get('can_otp_enter') is not None:
            if profile.otp == request.POST['otp']:
                messages.success(request, "Your Account is Created")
                red = redirect("home")
                red.set_cookie('verified', True)
                return red
            return HttpResponse("Wrong OTP")
        return HttpResponse("10 minutes passed")

    return render(request, "otp.html", {'id': uid})


def home(request):
    if request.COOKIES.get('verified') is not None:
        return render(request, 'index.html')
    else:
        return HttpResponse("Not verified.")


def handleLogin(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('loginpassword')

        try:
            profile = Profile.objects.get(user__username=user_name)
        except Profile.DoesNotExist:
            messages.error(request, "Username not found")
            return redirect('index')

        user = authenticate(request, username=user_name, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Your Account is Logged in")
            return redirect('index')
        else:
            messages.error(request, "Wrong details")
            return redirect('index')

    return HttpResponse("Not found")


def handleLogout(request):
    logout(request)
    messages.success(request, "Your Account is Logged Out")
    return redirect('index')


class LoanListView(generics.ListAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class HomeLoanDataListView(generics.ListAPIView):
    queryset = HomeLoanData.objects.all()
    serializer_class = HomeLoanDataSerializer






######################################################################################################

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save()  # Save the feedback to the database
            form.send_email()  # Send the email asynchronously
            return redirect('feedback_thank_you')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})



def thank_you_view(request):
    return render(request, 'thank_you.html')


###############################################################################################
# Contact page

from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def success_view(request):
    messages.success(request, "We will contact you shortly")
    return render(request, 'index.html')

######################################################################################################



