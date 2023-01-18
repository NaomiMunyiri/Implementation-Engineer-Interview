from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect ('success')
        else:
            messages.success(request, ("There was an error logging in. Try Again"))
            return redirect ('login')    
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out"))
    return redirect ('home')

@login_required
def success(request):
    messages.success(request, ("Successful Login"))
    return render(request,'success.html')

@login_required
def expos(request):
    return render(request,'list.html')


