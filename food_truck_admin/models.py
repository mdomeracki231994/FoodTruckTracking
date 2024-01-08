from django.db import models

from user_management.models import AppUser


class FoodTruckInfo(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    is_payment_successful = models.BooleanField(
        default=True)  # TODO when we add stripe, we will need the default to be false
    food_truck_name = models.CharField(max_length=50)
