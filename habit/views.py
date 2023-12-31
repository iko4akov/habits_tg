from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions

from habit.models import Habit
from habit.paginators import HabitPaginator
from habit.permissions import IsOwner
from habit.serializers import HabitSerializer, HabitCreateUpdateSerializer
from habit.tasks import set_schedule
from user.models import User
from habit.services import format_date_time


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitCreateUpdateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()
        if new_habit.owner.telegram_id:
            format_date = format_date_time(new_habit.time)
            data = {
                'tg': new_habit.owner.telegram_id,
                'action': new_habit.action,
                'time': format_date,
                'work_time': new_habit.work_time,
                'location': new_habit.location,
                'period': new_habit.period
            }
            set_schedule.delay(**data)


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
                habits = Habit.objects.filter(owner=self.request.user)
                return habits.order_by('pk')


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
                queryset = queryset.exclude(owner=self.request.user)

                return queryset.order_by('pk')


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
