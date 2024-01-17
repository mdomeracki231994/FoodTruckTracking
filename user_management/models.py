from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser


class AppUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.username = user.email
        user.save()
        return user

    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.username = user.email
        user.is_admin = True
        user.save()
        return user


class AppUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=50)
    is_food_truck_owner = models.BooleanField(default=False)
    is_food_truck_employee = models.BooleanField(default=False)
    is_food_truck_customer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    username = models.CharField(max_length=50)
    subscription = models.ForeignKey(
        'djstripe.Subscription', null=True, blank=True, on_delete=models.SET_NULL,
        help_text="The user's Stripe Subscription object, if it exists"
    )
    customer = models.ForeignKey(
        'djstripe.Customer', null=True, blank=True, on_delete=models.SET_NULL,
        help_text="The user's Stripe Customer object, if it exists"
    )
    USERNAME_FIELD = 'email'
    objects = AppUserManager()

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return self.username
