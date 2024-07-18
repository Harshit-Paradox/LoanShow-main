from rest_framework import serializers
from .models import Loan , HomeLoanData

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'



class HomeLoanDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeLoanData
        fields = '__all__'
