from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('expos',views.all_expos, name='list_of_expos'),
]
