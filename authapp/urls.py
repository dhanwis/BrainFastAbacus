from django.urls import path
from .views import *
urlpatterns = [
    
    path('',Home,name="Homepage"),
    path('admin/login/',admin_login,name="admin_login"),
    path('logout/',logout_view,name="logout"),
    path('gallery/',gallery,name="gallery"),
    path('about/',about,name="about"),
    path('event/',event,name="event"),
    path('contact/',contact,name="contact"),
    path('abacuscourse/',abacuscourse,name="abacuscourse"),
    path('vedicmath/',vedicmath,name="vedicmath"),
    path('abacusttc/',abacusttc,name="abacusttc")
    
    
    
]