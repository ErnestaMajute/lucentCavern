from django.urls import path

from newsletter import views


urlpatterns = [
    path('subscriptions_join/', views.subscriptions_join,
         name='subscriptions_join'),
]
