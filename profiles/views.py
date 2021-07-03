from django.shortcuts import render


# Function from BoutiqueAdo mini project
def profile(request):
    """ Display the user's profile. """

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
