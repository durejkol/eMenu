from django.contrib import admin
from .models import Menu, Dish

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_added', 'last_modified')
    list_filter = ('name', 'description', 'date_added', 'last_modified')
    search_fields = ('name', 'description')
    ordering = ['id']


class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'preparation_time',
                    'is_vegetarian', 'date_added', 'last_modified')
    list_filter = ('name', 'description', 'preparation_time', 
                   'is_vegetarian', 'date_added', 'last_modified')
    search_fields = ('name', 'description')
    ordering = ['id']

admin.site.register(Menu, MenuAdmin)
admin.site.register(Dish, DishAdmin)