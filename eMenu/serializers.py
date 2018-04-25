from rest_framework import serializers
from .models import Menu, Dish


class DishSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length = 100)
    description = serializers.CharField(max_length = 255)
    preparation_time = serializers.IntegerField()
    date_added = serializers.DateTimeField()
    last_modified = serializers.DateTimeField()
    photo = serializers.ImageField()
    is_vegetarian = serializers.BooleanField()
    menus = serializers.PrimaryKeyRelatedField(queryset = Menu.objects.all(), many = True)

    class Meta:
        model = Dish
        fields = ('id', 'name', 'description', 'preparation_time', 'is_vegetarian', 'photo', 'date_added', 'last_modified')

class MenuSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length = 100)
    description = serializers.CharField(max_length = 255)
    date_added = serializers.DateTimeField()
    last_modified = serializers.DateTimeField()
    dishes = DishSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = ('id', 'name', 'description', 'dishes', 'dishes_count', 'date_added', 'last_modified')