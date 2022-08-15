from django.shortcuts import render , redirect , HttpResponse
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User


def redirect_to_auth(request):

    if request.user.is_authenticated:
        return redirect('main:homepage')

    return redirect('auth/')

