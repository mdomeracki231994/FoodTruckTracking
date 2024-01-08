from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from user_management.models import AppUser


def index(request):
    return render(request, 'website/index.html')


def user_login(request):
    pass


def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        is_signup_for_owner = request.POST.get('is_owner_signup') == 'on'
        user = AppUser.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone,
            password=password
        )
        user.save()
        authenticated_user = authenticate(username=email, password=password)
        if authenticated_user is not None:
            login(request, authenticated_user)
            if is_signup_for_owner == 'on':
                return redirect('owner_signup')
            else:
                return HttpResponseRedirect('home')

    return render(request, 'website/signup.html')
