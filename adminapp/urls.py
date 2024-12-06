from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    
    path('', dashboard, name='dashboard'),
    path('imageadd/',image_add,name='imageadd'),
    path('imagelist/',image_list,name='imagelist'),
    path('image/<int:image_id>/view/',image_view,name="imageview"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)