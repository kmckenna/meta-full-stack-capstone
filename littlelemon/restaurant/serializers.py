from rest_framework import serializers, viewsets
from .models import MenuItem, Booking, Category
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator
from django.contrib.auth.models import User, Group


# import bleach

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
        # fields = ['user', 'id', 'title', 'price','inventory'] #, 'category', 'category_id']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'title']

        validators = [
            UniqueValidator(
                queryset=Category.objects.all()
            )
        ]