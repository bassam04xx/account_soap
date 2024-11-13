# account_app/urls.py
from django.urls import path
from .views import soap_page
from .views import bank_soap_app  # the view for handling SOAP requests

urlpatterns = [
    path('soap/', bank_soap_app, name='soap_service'),  # SOAP endpoint
    path('soap-page/', soap_page, name='soap_page'),  # Your SOAP page
]
