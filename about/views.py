from django.shortcuts import render
from .models import About

# Create your views here.

def about(request):
    """ A view to return the about page """

    about_image = About.objects.all()
    about_description = About.objects.all()

    template = 'about.html'
    context = {
        'about_image': about_image,
        'about_description': about_description,
    }

    return render(request, 'about.html')