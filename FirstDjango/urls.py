from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('about/', views.info),
    path('item/<int:id>', views.item_info),
    path('items/', views.get_items),
]
