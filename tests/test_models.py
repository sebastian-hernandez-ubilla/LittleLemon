from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_create_menu_item(self):
        menu_item = Menu.objects.create(title="pizza",price=5.76,inventory=5)
        self.assertEqual(menu_item.__str__(), "pizza : 5.76")
    