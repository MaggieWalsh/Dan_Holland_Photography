from django.shortcuts import render, get_object_or_404
from .models import Frame

# Create your views here.

def all_frames(request):
    """ A view to show all frames, including sorting"""

    frames = Frame.objects.all()

    context = {
        'frames' : frames,
    }

    return render(request, 'frames/frames.html', context)

#     frames = Frame.objects.all()
#     categories = None

#     if request.GET:
#         if 'category' in request.GET:
#             categories = request.GET['category'].split(',')
#             frames = frames.filter(category__name__in=categories)
#             categories = Category.objects.filter(name__in=categories)

#     context = {
#         'frames': frames,
#         'current_categories': categories,
#     }

#     return render(request, 'frames/frames.html', context)


# def frame_detail(request, frame_id):
#     """ A view to show individual frame details """

#     frame = get_object_or_404(Frame, pk=frame_id)

#     context = {
#         'frame': frame,
#     }

#     return render(request, 'frames/frame_detail.html', context)