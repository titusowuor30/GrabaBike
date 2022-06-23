from django.db import models
import datetime
from traitlets import default
from location_field.models.plain import PlainLocationField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    # Create Role model separately and add ManyToMany if user has more than one role
    roles = models.ManyToManyField(
        'Roles', related_name='users')
    tel = PhoneNumberField(default="+2547000000000", max_length=15)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['roles', 'first_name', 'last_name', ]


class Rider(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='riders')
    roles = models.ManyToManyField('Roles')
    id_number = models.CharField(max_length=8)
    address = models.CharField(max_length=100)
    bike_model = models.CharField(max_length=100)
    bike_img = models.ImageField(
        upload_to="bike_imgs", blank=True, null=True)
    city = models.CharField(max_length=50)
    location = PlainLocationField(based_fields=['city'], zoom=8)

    class Meta:
        db_table = "Riders"
        verbose_name_plural = "Riders"

    def __str__(self):
        return self.user.username


class Rides(models.Model):
    rider = models.ForeignKey(
        'Rider', on_delete=models.CASCADE, related_name='rides')
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='rides', blank=True, null=True)
    sorce = models.CharField(max_length=100, blank=True, null=True)
    #PlainLocationField(based_fields=['city'], zoom=8, default="0,0")
    destination = models.CharField(max_length=100, blank=True, null=True)
    confirmed = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    rating = models.IntegerField(max_length=1, validators=[
                                 MinValueValidator(0), MaxValueValidator(5)], default=0)
    comments = models.TextField(
        max_length=255, default="", blank=True, null=True)

    class Meta:
        db_table = "Rides"
        verbose_name_plural = "Ride History"

    def __str__(self):
        return self.rider.user.username


class Transactions(models.Model):
    transaction_code = models.CharField(
        max_length=255, default="G45DS8982GDF", blank=True, null=True)
    pyment_method = models.CharField(
        max_length=20, choices=(("Mpesa", "Mpesa"), ("Cash", "Cash")), default="Mpesa")
    amount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    rideid = models.CharField(max_length=100)

    class Meta:
        db_table = "Transactions"
        verbose_name_plural = "Transaction History"

    def __str__(self):
        return self.transaction_code


class Roles(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "Roles"
        verbose_name_plural = "User Roles"

    def __str__(self):
        return self.name
