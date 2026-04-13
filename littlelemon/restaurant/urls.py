from django.urls import path
from .views import home, menu, menu_item_detail, MenuItemsView

urlpatterns = [
    path('', home),
    path('menu/', menu),
    path('menu/<int:id>/', menu_item_detail),
    path('menu-items/', MenuItemsView.as_view()),
]