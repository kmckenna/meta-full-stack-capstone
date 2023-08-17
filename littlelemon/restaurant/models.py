from django.db import models

# Create your models here.
class Booking(models.Model):

    name = models.CharField(max_length=255)
    no_of_quests = models.SmallIntegerField(max_length=6)
    booking_date = models.DateField()



class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField(max_length=5)

    def __str__(self):
        return self.name