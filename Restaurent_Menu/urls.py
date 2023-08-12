from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),  # Home is having empty string,,, as_view() is not used in func based view
    path('item/<int:pk>/', views.MenuItemDetail.as_view(), name="menu_item")
]