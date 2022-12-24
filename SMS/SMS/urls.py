from django.contrib import admin
from django.urls import path, include
from .import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('members/', include('members.urls')),
    path('loans/', views.loans, name='loans'),
    path('accounts/', views.accounts, name='accounts'),
]

urlpatterns += staticfiles_urlpatterns()
