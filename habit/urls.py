from django.urls import path

from habit.apps import HabitConfig
from habit.views import HabitCreateAPIView, HabitListAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView, HabitListPublicAPIView

app_name = HabitConfig.name

urlpatterns = [
    path('create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('', HabitListAPIView.as_view(), name='habit-list'),
    path('public/', HabitListPublicAPIView.as_view(), name='habit-list'),
    path('<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit-retrieve'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit-update'),
    path('delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit-delete'),
]
