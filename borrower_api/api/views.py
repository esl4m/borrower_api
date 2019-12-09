from rest_framework import viewsets
from .models import Borrower, Investor, Requests
from .serializers import BorrowerSerializer, InvestorSerializer, RequestsSerializer


class BorrowerView(viewsets.ModelViewSet):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer


class InvestorView(viewsets.ModelViewSet):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer


class RequestsView(viewsets.ModelViewSet):
    queryset = Requests.objects.all()
    serializer_class = RequestsSerializer
