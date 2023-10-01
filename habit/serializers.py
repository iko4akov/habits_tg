from rest_framework import serializers

from habit.models import Habit
from habit.validators import NiceHabitValidator


class HabitCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [NiceHabitValidator(field='parent')]

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

