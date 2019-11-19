from django.db import models
from datetime import datetime


class Borrower(models.Model):
    name = models.CharField(max_length=50)
    amount = models.FloatField(null=False, blank=False, default=None)  # models.DecimalField(max_digits=8)
    period = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Investor(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=8)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Requests(models.Model):
    # loan_status = models.BooleanField(default=True)
    loan_status = (
        (1, "Funded"),
        (2, "Completed")
    )

    borrower_id = models.ForeignKey('Borrower', on_delete=models.PROTECT)
    investor_id = models.ForeignKey('Investor', on_delete=models.PROTECT)
    investor_balance = models.DecimalField(max_digits=8)
    loan_amount = models.DecimalField(max_digits=8)
    due_date = models.DateTimeField(blank=False)
    paid_amount = models.DecimalField(max_digits=8)
    # date = models.DateTimeField(default=datetime.now, blank=False)
    date = models.DateTimeField(auto_now=True, auto_now_add=True, blank=False)
