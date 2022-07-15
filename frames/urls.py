from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_frames, name='frames'),
    # path('<frame_id>', views.frame_detail, name='frame_detail'),
]
