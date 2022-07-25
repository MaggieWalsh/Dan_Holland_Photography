from django.shortcuts import render
from .models import Abouts

# Create your views here.

def all_abouts(request):
    """ A view to show all products, including sorting and search queries """

    abouts = Abouts.objects.all()


    context = {
        'abouts': abouts,
    }

    return render(request, 'abouts.html', context)
