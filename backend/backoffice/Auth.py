from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth import get_user_model


@login_required(login_url='/users/login') # Check login
def staff(request):
    return render(request, 'staff.html')


def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/dashboard')
        else:
            messages.warning(request, "Login Error !! Invalid Member number or Password try again !")
            return HttpResponseRedirect('/')

    context = {
    }
    return render(request, 'auth/login.html', context)


def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/')