from django.shortcuts import render, redirect , HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



def show_login(request):
    return render(request,'login/login.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)




        if user is not None:
            if user.is_active and user.is_staff:
                login(request,user)
                return redirect('main:homepage')

            messages.info(request, 'Sorry.. You are not staff anymore....Please contact to admin.')
            return redirect('/')

        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('/')




def user_logout(request):
    logout(request)
    messages.info(request,'user logged out')
    return redirect('/')




