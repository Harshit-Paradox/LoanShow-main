from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Loan , HomeLoanData

admin.site.register(Loan)
admin.site.register(HomeLoanData)

