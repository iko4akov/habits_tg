from rest_framework import serializers

from habit.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

    def to_representation(self, instance):
        """ Если привычка не "nice", исключаем её из сериализации"""
        data = super().to_representation(instance)
        if not instance.nice_habit:
            data = None
        return data
