from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status, viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer, UserSerializer, GroupSerializer
from django.contrib.auth.models import User, Group


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# @api_view(['POST', 'GET'])
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    permission_classes = [permissions.IsAuthenticated]
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
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]