from rest_framework import serializers, viewsets
from .models import MenuItem, Booking
# from rest_framework.validators import UniqueTogetherValidator, UniqueValidator
from django.contrib.auth.models import User
# import bleach

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']



class MenuItemSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = MenuItem
        fields =  '__all__'
        # fields = ['user', 'id', 'title', 'price','inventory'] #, 'category', 'category_id']


class BookingSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Booking
        fields =  '__all__'



# class CategorySerializer (serializers.ModelSerializer):
#     created_by = serializers.HiddenField(
#         default=serializers.CurrentUserDefault())
#
#     class Meta:
#         model = Category
#         fields = ['created_by', 'id', 'title']
#
#         validators = [
#             UniqueValidator(
#                 queryset=Category.objects.all()
#             )
#         ]
#
