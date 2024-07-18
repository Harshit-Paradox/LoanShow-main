from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Loan , HomeLoanData
from .serializers import LoanSerializer , HomeLoanDataSerializer 

# myapp/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


class LoanListView(generics.ListAPIView):
    queryset = Loan.objects.all()
    print(queryset)
    serializer_class = LoanSerializer
    # pagination_class = None  # You can set a custom pagination class if needed



class HomeLoanDataListView(generics.ListAPIView):
    queryset = HomeLoanData.objects.all()
    serializer_class = HomeLoanDataSerializer

