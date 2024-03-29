import stripe
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from food_truck_admin.models import FoodTruckInfo
from djstripe.models import Product, APIKey


def food_truck_owner_signup(request):
    if request.user.is_authenticated:
        is_user = True
        if request.method == "POST":
            food_truck_name = request.POST.get('food_truck_name')
            FoodTruckInfo.objects.create(
                user=request.user,
                food_truck_name=food_truck_name,
                is_payment_successful=True
            )
            request.user.is_food_truck_owner = True
        context = {
            'is_user': is_user,
            'products': Product.objects.all()
        }
        return render(request, 'food_truck_admin/signup.html', context)
    else:
        return redirect('signup')


@login_required
def subscription_confirm(request):
    stripe.api_key = APIKey.objects.all().filter()
