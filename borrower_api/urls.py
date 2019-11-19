from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('borrower', views.BorrowerView)  # borrower is the endpoint
router.register('investor', views.InvestorView)  # investor is the endpoint
router.register('requests', views.RequestsView)  # requests is the endpoint

urlpatterns = [
    path('', include(router.urls))
]
