from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializers import DishSerializer, MenuSerializer
from .models import Menu, Dish
from django.views.generic import ListView
from django.views.generic.base import View
from django.db.models import Count
from django.template import loader
from django.http import HttpResponse

class MenuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows menus to be viewed
    """
    queryset = Menu.objects.exclude(dishes = None).annotate(dishes_count =
                                                            Count('dishes'))
    serializer_class = MenuSerializer
    http_method_names = ['get']


class DishesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows menus to be viewed
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    http_method_names = ['get']


def MenuList(request):
    """
    View that shows list of non-empty menus.
    Details data is taken from DRF endpoints, and shown as modal.
    """
    menus = Menu.objects.exclude(dishes = None).annotate(dishes_count =
                                                         Count('dishes'))
    return render(request, 'menu_list_detail.html', {'menus': menus})


def insert_sample_data(request):
    """
    View that removes all existing data in Menu and Dish model,
    and automatically add sample data (no photos included).
    Photos can be added via admin panel.
    Afterwards it redirects to MenuList view.
    (had issues with manage.py dumpdata and manage.py loaddata :) )
    """
    
    Dish.objects.all().delete()
    Menu.objects.all().delete()


    m1 = Menu(name = "Menu numer 1", description = "Opis menu numer 1")
    m1.save()
    m2 = Menu(name = "Menu numer 2", description = "Opis menu numer 2")
    m2.save()
    m3 = Menu(name = "Menu numer 3", description = "Opis menu numer 3")
    m3.save()
    m4 = Menu(name = "Menu numer 4", description = "Opis menu numer 4")
    m4.save()
    m5 = Menu(name = "Menu numer 5", description = "Opis menu numer 5")
    m5.save()
    m6 = Menu(name = "Menu numer 6", description = "Opis menu numer 6")
    m6.save()
    m7 = Menu(name = "Menu numer 7", description = "Opis menu numer 7")
    m7.save()
    m8 = Menu(name = "Menu numer 8", description = "Opis menu numer 8")
    m8.save()
    m9 = Menu(name = "Menu numer 9", description = "Opis menu numer 9")
    m9.save()
    m10 = Menu(name = "Menu numer 10", description = "Opis menu numer 10")
    m10.save()
    m11 = Menu(name = "Menu numer 11", description = "Opis menu numer 11")
    m11.save()
    m12 = Menu(name = "Menu numer 12", description = "Opis menu numer 12")
    m12.save()
    m13 = Menu(name = "Menu numer 13", description = "Opis menu numer 13")
    m13.save()
    m14 = Menu(name = "Menu numer 14", description = "Opis menu numer 14")
    m14.save()
    m15 = Menu(name = "Menu numer 15", description = "Opis menu numer 15")
    m15.save()

    d1 = Dish(name = 'Spaghetti', 
              description = 'Makaron z sosem i mięsem mielonym',
              preparation_time = 30, is_vegetarian = False)
    d1.save()
    d2 = Dish(name = 'Jajecznica', 
              description = 'Jajecznica z 3 jajek',
              preparation_time = 10, is_vegetarian = True)
    d2.save()
    d3 = Dish(name = 'Risotto', 
              description = 'Z pieczarkami i suszonymi pomidorami',
              preparation_time = 40, is_vegetarian = True)
    d3.save()
    d4 = Dish(name = 'Pierś z kurczaka', 
              description = 'Z frytkami i surówkami', 
              preparation_time = 25, is_vegetarian = False)
    d4.save()
    d5 = Dish(name = 'Kotlet schabowy', 
              description = 'Z ziemniakami i kapustą', 
              preparation_time = 30, is_vegetarian = False)
    d5.save()
    d6 = Dish(name = 'Pizza', 
              description = 'Z salami o średnicy 30cm', 
              preparation_time = 20, is_vegetarian = False)
    d6.save()
    d7 = Dish(name = 'Gulasz z indyka', 
              description = 'Podany z kaszą i buraczkami', 
              preparation_time = 30, is_vegetarian = False)
    d7.save()
    d8 = Dish(name = 'Łosoś grillowany', 
              description = 'Podany ze szpinakiem i frytkami', 
              preparation_time = 15, is_vegetarian = False)
    d8.save()

    d1.menus.add(m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15)
    d2.menus.add(m1, m2, m3, m4, m5, m6, m7, m8, m10, m11, m12, m13, m14, m15)
    d3.menus.add(m10, m11, m12, m13, m14, m15)
    d4.menus.add(m8, m9, m10, m11, m12, m13, m14, m15)
    d5.menus.add(m1, m2, m3, m4, m5, m6, m7, m8, m9)
    d6.menus.add(m1, m2, m3, m4, m5, m6, m7, m15)
    d7.menus.add(m1, m5, m6, m7, m8, m9, m10, m11)
    d8.menus.add(m4, m5, m6, m7, m8, m9)

    return redirect('/')