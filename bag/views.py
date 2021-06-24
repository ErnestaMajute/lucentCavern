from django.shortcuts import render, redirect

# Create your views here.


# Function from BoutiqueAdo mini project
def view_bag(request):
    """ A view to to render the bag contents page """

    return render(request, 'bag/bag.html')


# Function from BoutiqueAdo mini project
def add_to_bag(request, item_id):
    """ 
    This view allows the user to add a certain amount of products
    """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    redirect_url = request.POST.get('redirect_url')

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
