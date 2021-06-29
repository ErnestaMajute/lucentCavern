from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('modify/<item_id>/', views.modify_bag, name='modify_bag'),
    path('delete/<item_id>/', views.delete_from_bag, name='delete_from_bag'),
]
