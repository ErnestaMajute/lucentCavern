from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_favoriteslist, name='favoriteslist'),
    path('add_favorite/<product_id>', views.add_favorite, name="add_favorite"),
]
