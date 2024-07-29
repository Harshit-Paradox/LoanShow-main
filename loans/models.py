from django.db import models
import uuid
from django.contrib.auth.models import User

class Loan(models.Model):
    bank = models.CharField(max_length=100)
    loan_type = models.CharField(max_length=100)
    loan_amount = models.CharField(max_length=100)
    interest_rate = models.CharField(max_length=100)
    tenure = models.CharField(max_length=100)
    processing_fee = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.bank} - {self.loan_type}"

class HomeLoanData(models.Model):
    bank_name = models.CharField(max_length=255)
    interest_rate = models.CharField(max_length=255)
    processing_fee = models.CharField(max_length=255)
    loan_amount_tenure = models.CharField(max_length=255)

    def __str__(self):
        return self.bank_name
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone_number = models.CharField(max_length=15)
    otp = models.CharField(max_length=100, null=True, blank=True)
    uid = models.CharField(default=uuid.uuid4, max_length=200)




class Feedback(models.Model):
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_no = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.name
