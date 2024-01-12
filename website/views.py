from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from user_management.models import AppUser
from food_truck_admin.models import FoodTruckLocation


def index(request):
    truck_locations = FoodTruckLocation.objects.all()  # TODO,  We will want a query that returns trucks close to user.  Not all trucks in the system.
    for loc in truck_locations:
        print(f'Lat: {loc.latitude}')
    user = request.user
    context = {
        'user': user,
        'truck_locations': truck_locations,
    }
    return render(request, 'website/index.html', context)


def user_login(request):
    if request.method == "POST":
        user_email = request.POST.get('')
        user_password = request.POST.get('')
        user = authenticate(user_email, user_password)
        login(request, user)
        return redirect('home')
    return render(request, 'website/login.html')


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
