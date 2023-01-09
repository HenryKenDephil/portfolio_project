
from django.urls import path, include
from .import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('members/', views.members, name='members'),
    path('create/', views.create_member, name='create'),
    path('edit/<id>/', views.edit_members, name='edit'),
    path('delete/<id>/', views.delete_member, name='delete'), 
    #path('search/',views.search_members,name='search'),

]
