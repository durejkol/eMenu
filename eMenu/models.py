from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length = 100, unique = True)
    description = models.CharField(max_length = 255)
    date_added = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 255)
    preparation_time = models.PositiveSmallIntegerField()
    date_added = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    photo = models.ImageField(upload_to = 'media', blank = True)
    is_vegetarian = models.BooleanField()
    menus = models.ManyToManyField('Menu', related_name='dishes')

    def __str__(self):
        return self.name