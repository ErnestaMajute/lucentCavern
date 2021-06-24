from django.shortcuts import render

# Create your views here.

# Function from BoutiqueAdo mini project
def view_bag(request):
    """ A view to to render the bag contents page """

    return render(request, 'bag/bag.html')
