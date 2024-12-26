from django.urls import path
from .views import *


urlpatterns = [
    
    path('', dashboard, name='dashboard'),
    path('imageadd/',image_add,name='imageadd'),
    path('imagelist/',image_list,name='imagelist'),
    path('image/<int:image_id>/view/',image_view,name="imageview"),
    path('eventadd/',event_add,name='eventadd'),
    path('eventlist/',event_list,name='eventlist'),
    path('imageedit/<int:image_id>',image_edit,name='imageedit'),
    path('eventedit/<int:event_id>',event_edit,name='eventedit'),
    path('event/<int:event_id>',event_view,name="eventview"),
    path('imagedelete/<int:image_id>',image_delete,name="imagedelete"),
    path('eventdelete/<int:event_id>',event_delete,name="eventdelete"),
    path('addnews/',news_add,name="newsadd"),
    path('newslist/',news_list,name="newslist"),
    path('newsedit/<int:news_id>/',news_edit,name="newsedit"),
    
    
    
    
    

]
