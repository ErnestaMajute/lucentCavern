from django.shortcuts import render
from products.models import Product
from .models import UserFavoriteslist
from profiles.models import UserProfile

# Create your views here.


def view_favoriteslist(request):
    """ A view that renders the bag contents page """
    user = UserProfile.objects.get(user=request.user)
    favoriteslist = Product.objects.filter(
        userfavoriteslists__user_profile=user)
    context = {
        'favoriteslist': favoriteslist,
    }
    return render(request, 'favorites/favorites.html', context)
