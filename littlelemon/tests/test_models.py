from django.test import TestCase
from restaurant.models import MenuItem, Category

class MenuItemTest(TestCase):

    def test_get_item(self):
        category = Category.objects.get(title="Desserts")
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100, category=category)
        self.assertEqual(item.get_item(), "IceCream : 80.00")
