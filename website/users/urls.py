from django.urls import path
from . import views
from .views import success

urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'), 
    path('success/', views.success, name='success'),
    path('expos/', views.expos, name='expo_list'),
]
