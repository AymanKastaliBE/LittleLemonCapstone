from django.test import TestCase
from restaurant.models import Menu

#TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(name="IceCream", price=80, menu_item_description='test description')
        self.assertEqual(item.name, "IceCream")
        self.assertEqual(item.price, 80)
        self.assertEqual(item.menu_item_description, 'test description')