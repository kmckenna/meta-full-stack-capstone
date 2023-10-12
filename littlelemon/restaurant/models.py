from django.db import models
# import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
# from django.core.exceptions import ValidationError



# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField(
        validators=[
            MaxValueValidator(12),
            MinValueValidator(1)
        ])
    booking_date = models.DateField()
    booking_time = models.TimeField()

    def __str__(self):
        return f'{self.name} has booked {self.no_of_guests} for {self.booking_date} at {self.booking_time}'


class MenuItem(models.Model):
    title = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField(
        validators=[
            MaxValueValidator(50)
        ])
    category = models.ForeignKey('Category', on_delete=models.PROTECT, default=1)

    def get_item(self):
        return f'{self.title} : {str(self.price)}'

    def __str__(self):
        return f'{self.title} : {str(self.price)}'


class Category(models.Model):
    slug = models.SlugField(max_length=255, unique=True)
    title = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.title
