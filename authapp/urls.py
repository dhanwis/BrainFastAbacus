from django.urls import path
from .views import *
urlpatterns = [
    
    path('',Home,name="Hpmepage"),
    path('dashboard/',dashboard,name="dashboard"),
    path('logout/',logout,name="logout"),
    
]