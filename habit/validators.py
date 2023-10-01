from rest_framework.validators import ValidationError

from habit.models import Habit


class NiceHabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        parent = dict(value).get(self.field)
        if parent.nice_habit:
            raise ValidationError('Не верная привычка в nice_habit, необходимо прследоваться от полезных привычек, не от приятных')
