from django.shortcuts import render

# Create your views here.


# Function from Boutique Ado miniprojecct
def index(request):
    """ A view to return index page """

    return render(request, 'home/index.html')
