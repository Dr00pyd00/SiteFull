from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'convertisseur'

urlpatterns = [
        
        path('',  TemplateView.as_view(template_name='convertisseur/main.html'),
name='convertisseur'),

        
    





]
