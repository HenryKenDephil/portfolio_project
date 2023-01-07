from django.contrib import admin
from django.urls import path, include
from members.views import create_member, edit_member, delete_member
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from users.views import register
urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', include('members.urls')),
    #path('create/', create_member),
    #path('edit/<int:id>/', edit_member),
    #path('update/<int:id>/', update_member),
    #path('delete/<int:id>/', delete_member),
    #path('users/', include('users.urls')),
    #path('register/', register),
    
]

urlpatterns += staticfiles_urlpatterns()
