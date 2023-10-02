from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions

from habit.models import Habit
from habit.paginators import HabitPaginator
from habit.permissions import IsOwner
from habit.serializers import HabitSerializer, HabitCreateUpdateSerializer
from user.models import User


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitCreateUpdateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = HabitPaginator
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('owner',)

    def get_queryset(self):
        if isinstance(self.request.user, User):
            if self.request.user.is_staff:
                return Habit.objects.all().order_by('pk')
            else:
                return Habit.objects.filter(owner=self.request.user).order_by('pk')


class HabitListPublicAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = HabitPaginator
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('owner',)

    def get_queryset(self):
        if isinstance(self.request.user, User):
            if self.request.user.is_staff:
                return Habit.objects.all().order_by('pk')
            else:
                queryset = Habit.objects.filter(public=True)
                queryset = queryset.exclude(owner=self.request.user).order_by('pk')
                return queryset


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitCreateUpdateSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]
