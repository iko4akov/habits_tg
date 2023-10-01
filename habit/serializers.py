from rest_framework import serializers

from habit.models import Habit
from habit.validators import NiceHabitValidator, WorkTimeValidator, PeriodValidator


class HabitCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            NiceHabitValidator(parent='parent', nice_habit='nice_habit', reward='reward'),
            WorkTimeValidator(work_time='work_time'),
            PeriodValidator(period='period')
        ]


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
