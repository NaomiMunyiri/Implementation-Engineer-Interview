from django.shortcuts import render
from .models import Event

def home(request):
    return render(request, 'events/home.html', {})

def all_expos(request):
    expo_list=Event.objects.all()
    return render(request, 'events/list.html',
    {'expo_list':expo_list})