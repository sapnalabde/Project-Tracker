from django.contrib import admin
from django.urls import path
#from django.conf.urls import url
from . import views


urlpatterns = [
    
    #url(r'^accounts/signin/$', login_site, name='login'),
    path('accounts/login/', views.login_site),
    path('accounts/logout/',views.auth_logout),
    path('accounts/detail/',views.detail),
]
