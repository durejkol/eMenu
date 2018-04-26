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
    Details data is taken from DRF endpoint and it is shown as modal.
    """
    menus = Menu.objects.exclude(dishes = None).annotate(dishes_count =
                                                         Count('dishes'))
    return render(request, 'menu_list_detail.html', {'menus': menus})