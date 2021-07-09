from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from products.models import Product
from django.contrib import messages
from .models import UserFavoriteslist
from profiles.models import UserProfile


# Functions samples from https://stackoverflow.com/questions/56580696/how-to-implement-add-to-wishlist-for-a-product-in-django
def view_favoriteslist(request):
    """ A view that renders the bag contents page """
    # Fetch the list of products that the user favorited
    user_favourites = UserFavoriteslist.objects.get(
        user_profile=request.user.profile)
    products = Product.objects.filter(
        id__in=[val.id for val in user_favourites.favorited_products.all()])
    context = {
        'favoritedproducts': products,
    }

    return render(request, 'favoriteslist/favoriteslist.html', context)


@login_required
def add_favorite(request, product_id):
    """Allows users to add or remove a product to/from Favorites list"""
    favorite = get_object_or_404(Product, pk=product_id)
    user = UserProfile.objects.get(user=request.user)
    favoriteslist_user, created = UserFavoriteslist.objects.get_or_create(
        user_profile=user)
    favoriteslist = Product.objects.filter(
        userfavoriteslists__user_profile=user)

    if created:
        favorite.userfavoriteslists.add(favoriteslist_user.id)
        messages.success(request, ("Added to your Favorites list"))
    else:
        if favorite in favoriteslist:
            favorite.userfavoriteslists.remove(favoriteslist_user.id)
            messages.success(request, ("Removed from your Favorites list"))
        else:
            favorite.userfavoriteslists.add(favoriteslist_user.id)
            messages.success(request, ("Added to your Favorites list"))

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
