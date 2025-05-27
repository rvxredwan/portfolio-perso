from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),           
    path('chakir/', views.contact, name='chakir'),     
    path('oussama/', views.oussama, name='oussama'),   
]
