from django.db import models

# Create your models here.
class Booking(models.Model):

    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField()
    booking_date = models.DateField()
    booking_time = models.TimeField(null=True)



class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT, default=1)

    def get_item(self):
        return f'{self.title} : {str(self.price)}'

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
        # return self.name

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, unique=True)

    # created = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(
    #     User, on_delete=models.CASCADE, default=1)

    # modified = models.DateTimeField(auto_now_add=True)
    # modified_by = models.ForeignKey(
    #     User, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.title


# class MenuItem(models.Model):
#     title = models.CharField(max_length=255, unique=True)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     inventory = models.SmallIntegerField()
#     # category = models.ForeignKey('Category', on_delete=models.PROTECT, default=1)
#
    #
    # def __str__(self) -> str:
    #     return self.title
    #
