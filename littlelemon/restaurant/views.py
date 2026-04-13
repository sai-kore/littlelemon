from django.shortcuts import render, get_object_or_404
from .models import MenuItem
from rest_framework import generics
from .serializers import MenuItemSerializer

# Homepage
def home(request):
    return render(request, 'home.html')

# Menu page (alphabetical order)
def menu(request):
    items = MenuItem.objects.all().order_by('title')
    return render(request, 'menu.html', {'items': items})

# Detail page
def menu_item_detail(request, id):
    item = get_object_or_404(MenuItem, id=id)
    return render(request, 'detail.html', {'item': item})

# API
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer