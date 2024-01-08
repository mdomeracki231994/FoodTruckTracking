from django.urls import path

from food_truck_admin import views

urlpatterns = [
    path('owner_signup/', views.food_truck_owner_signup, name='owner_signup')
]
