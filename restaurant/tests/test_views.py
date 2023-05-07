# import json
# from django.test import TestCase
# from restaurant.models import Menu
# from django.core.serializers import serialize

# class MenuViewTest(TestCase):
#     def setUp(self):
#         self.menu1 = Menu.objects.create(name="Menu 1", price=10, menu_item_description="Description 1")
#         self.menu2 = Menu.objects.create(name="Menu 2", price=20, menu_item_description="Description 2")

#     def test_getall(self):
#         menu_items = Menu.objects.all()
#         serialized_data = json.dumps(list(menu_items.values()), sort_keys=True)
#         expected_data = '[{"fields": {"menu_item_description": "Description 1", "name": "Menu 1", "price": 10}, "model": "restaurant.menu", "pk": 1}, {"fields": {"menu_item_description": "Description 2", "name": "Menu 2", "price": 20}, "model": "restaurant.menu", "pk": 2}]'
#         self.assertEqual(serialized_data, expected_data)
