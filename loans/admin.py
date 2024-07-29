from django.contrib import admin


from django.contrib import admin
from .models import Loan , HomeLoanData , Feedback , Contact
from .models import Profile 

admin.site.register(Loan)
admin.site.register(HomeLoanData)
admin.site.register(Profile)
admin.site.register(Feedback)
admin.site.register(Contact)

