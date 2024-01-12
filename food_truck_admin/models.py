from django.db import models

from user_management.models import AppUser


class FoodTruckInfo(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    is_payment_successful = models.BooleanField(
        default=True)  # TODO when we add stripe, we will need the default to be false
    food_truck_name = models.CharField(max_length=50)
    cuisine_type = models.CharField(max_length=50)


class Menu(models.Model):
    food_truck = models.ForeignKey(FoodTruckInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    is_vegetarian = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class FoodTruckLocation(models.Model):
    food_truck = models.ForeignKey(FoodTruckInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default=None, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name
