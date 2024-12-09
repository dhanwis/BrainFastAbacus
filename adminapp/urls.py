from django.urls import path
from .views import *


urlpatterns = [
    
    path('', dashboard, name='dashboard'),
    path('imageadd/',image_add,name='imageadd'),
    path('imagelist/',image_list,name='imagelist'),
    path('image/<int:image_id>/view/',image_view,name="imageview")
]
