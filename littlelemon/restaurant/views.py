
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status, viewsets
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    # permission_classes = IsAuthenticated


# @api_view(['POST', 'GET'])
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    # ordering_fields = ['price', 'inventory']
    # filterset_fields = ['price', 'inventory']

    # search_fields = ['category']

    # def get_permissions(self):
    #     if (self.request.method == 'GET'):
    #         return []
    #
    #     return [IsAuthenticated()]


class SingleMenuItemView(generics.RetrieveAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    # def get_permissions(self):
    #     if (self.request.method == 'GET'):
    #         return []
    #
    #     return [IsAuthenticated()]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()