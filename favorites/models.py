from django.db import models
from products.models import Product
from profiles.models import UserProfile


class UserFavoriteslist(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE,
                                        null=False, blank=False)
    favorited_products = models.ManyToManyField(
        Product, related_name='userfavoriteslists')

    def __str__(self):
        return '{} Favorites list'.format(self.user_profile.user.username)
