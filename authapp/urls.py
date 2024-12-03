from django.urls import path
from .views import *
urlpatterns = [
    
    path('',Home,name="Homepage"),
    path('admin/login/',admin_login,name="admin_login"),
    path('logout/',logout_view,name="logout"),
    path('programs/',gallery,name="gallery")
    
    
]