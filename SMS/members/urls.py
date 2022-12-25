
from django.urls import path, include
from .import views 

urlpatterns = [
    path('', views.members, name='members'),
    path('', views.member_details, name='members_details'),
    
]
