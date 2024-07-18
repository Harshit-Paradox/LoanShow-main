from django.db import models

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