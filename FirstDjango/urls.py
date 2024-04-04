from django.contrib import admin
from django.urls import path
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.info, name='about'),
    path('item/<int:id>', views.item_info, name='item-detail'),
    path('items/', views.get_items, name='items-list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
