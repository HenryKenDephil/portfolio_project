
from django.urls import path, include, re_path
from .import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('members/', views.members, name='members'),
    path('create/', views.create_member, name='create'),
    re_path(r'^edit/(?P<id>\d+)/$', views.edit_member, name='edit'),
    #path('', views.update_member, name='update'),
    path(r'^delete/(?P<id>[\w-]+)/$', views.delete_member, name='delete'), 
    re_path(r'^search/',views.search_members,name='search'),

]
