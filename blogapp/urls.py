from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path('read/<int:blogid>',views.read,name='read'),
    path('upload/',views.upload , name="upload"),
]
