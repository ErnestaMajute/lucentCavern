from django.contrib import admin
from .models import UserFavoriteslist


class UserFavoriteslistAdmin(admin.ModelAdmin):

    list_display = (
        'user_profile',
        'favorited_products',
        )


admin.site.register(UserFavoriteslist)
