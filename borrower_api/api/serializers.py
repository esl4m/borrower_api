from rest_framework import serializers
from .models import Borrower, Investor, Requests


class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = ('id', 'name', 'amount', 'period')


class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = ('id', 'name', 'balance', 'interest_rate')


class RequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = ('id', 'borrower_id', 'investor_id', 'investor_balance', 'loan_amount', 'due_date', 'paid_amount',
                  'date', 'loan_status')
