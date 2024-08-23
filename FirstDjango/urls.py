
from django.contrib import admin
from django.urls import path
from MainApp import views


urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('items/', views.items_list, name='items_list'),
]
