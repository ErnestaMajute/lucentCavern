from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from products.models import Product
from django.contrib import messages
from .models import UserFavoriteslist
from profiles.models import UserProfile


# Functions samples taken from Stackoverflow (link in README.md)
def view_favoriteslist(request):
    """ A view that renders the bag contents page """
    # Fetch the list of products that the user favorited
    user_favourites = UserFavoriteslist.objects.filter(
        user_profile=request.user.userprofile).first()
    if user_favourites:
        products = Product.objects.filter(
            id__in=[val.id for val in user_favourites.favorited_products.all()])
    else:
        products = []
    context = {
        'favoritedproducts': products,
    }
    return render(request, 'favoriteslist/favoriteslist.html', context)


@login_required
def add_favorite(request, product_id):
    """Allows users to add/remove a product to/from Favorites list"""
    favorite = get_object_or_404(Product, pk=product_id)
    user = UserProfile.objects.get(user=request.user)
    favoriteslist_user, created = UserFavoriteslist.objects.get_or_create(
        user_profile=user)
    favoriteslist = Product.objects.filter(
        userfavoriteslists__user_profile=user)

    # Checks if Favorites list created and adds product to it
    if created:
        favorite.userfavoriteslists.add(favoriteslist_user.id)
        messages.success(request, ("Added to your Favorites list"))
    else:
        # Checks if product already in Favorites list and removes
        if favorite in favoriteslist:
            favorite.userfavoriteslists.remove(favoriteslist_user.id)
            messages.success(request, ("Removed from your Favorites list"))
        # Adds to Favorites list
        else:
            favorite.userfavoriteslists.add(favoriteslist_user.id)
            messages.success(request, ("Added to your Favorites list"))

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
