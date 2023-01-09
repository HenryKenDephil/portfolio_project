from django.contrib import admin
from django.urls import path, include
from members.views import create_member, edit_members, delete_member
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from users.views import register
urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', include('members.urls')),
    
]

urlpatterns += staticfiles_urlpatterns()
