from django.test import TestCase
from .models import Menu, Dish
from django.db.utils import IntegrityError

class MenuCreateTestCase(TestCase):
    def setUp(self):
        Menu.objects.create(name="Menu 1", description="Opis menu 1")
        Menu.objects.create(name="Menu 2", description="Opis menu 2")

    def test_menu_create(self):
        """Menu creation test"""
        menu1 = Menu.objects.get(name="Menu 1")
        menu2 = Menu.objects.get(name="Menu 2")
        self.assertEqual(menu1.description, 'Opis menu 1')
        self.assertEqual(menu2.description, 'Opis menu 2')


class MenuUniqueCreateTestCase(TestCase):
    def test_unique_menu_create(self):
        """Try to create 2 menus with same name"""
        Menu.objects.create(name="Menu 1", description="Opis menu 1")
        with self.assertRaises(IntegrityError):
            Menu.objects.create(name="Menu 1", description="Opis menu 1")

    
class MenuRemoveTestCase(TestCase):
    def setUp(self):
        Menu.objects.create(name="Menu 1", description="Opis menu 1")
        Menu.objects.create(name="Menu 2", description="Opis menu 2")

    def test_menu_create(self):
        """Menu creation test"""
        menu1 = Menu.objects.all().delete()
        self.assertEqual(Menu.objects.count(), 0)


class DishCreateTestCase(TestCase):
    def setUp(self):
        dish1 = Dish(name="Dish 1", description="Opis dania 1", 
                     is_vegetarian = True, preparation_time = 30)
        dish1.save()
        dish2 = Dish(name="Dish 2", description="Opis dania 2", 
                     is_vegetarian = False, preparation_time = 15)
        dish2.save()
        menu1 = Menu(name="Menu 1", description="Opis menu 1")
        menu1.save()
        dish1.menus.add(menu1)

    def test_Dish_create(self):
        """Dish creation test"""
        Dish1 = Dish.objects.get(name="Dish 1")
        Dish2 = Dish.objects.get(name="Dish 2")
        self.assertEqual(Dish1.description, 'Opis dania 1')
        self.assertEqual(Dish2.description, 'Opis dania 2')
        self.assertEqual(Dish1.is_vegetarian, True)
        self.assertEqual(Dish2.is_vegetarian, False)
        self.assertEqual(Dish1.preparation_time, 30)
        self.assertEqual(Dish2.preparation_time, 15)
        self.assertEqual(Dish1.menus.all()[0].name, "Menu 1")
    

class DishRemoveTestCase(TestCase):
    def setUp(self):
        dish1 = Dish(name="Dish 1", description="Opis dania 1", 
                     is_vegetarian = True, preparation_time = 30)
        dish1.save()
        dish2 = Dish(name="Dish 2", description="Opis dania 2", 
                     is_vegetarian = False, preparation_time = 15)
        dish2.save()
        menu1 = Menu(name="Menu 1", description="Opis menu 1")
        menu1.save()
        dish1.menus.add(menu1)

    def test_Dish_create(self):
        """Dish creation test"""
        Dish.objects.all().delete()
        self.assertEqual(Dish.objects.count(), 0)
