from rest_framework.validators import ValidationError


class NiceHabitValidator:
    def __init__(self, nice_habit, parent, reward):
        self.nice_habit = nice_habit
        self.parent = parent
        self.reward = reward

    def __call__(self, value):
        parent = dict(value).get(self.parent)
        nice_habit = dict(value).get(self.nice_habit)
        reward = dict(value).get(self.reward)
        if nice_habit:
            if parent is not None:
                raise ValidationError(
                    "У приятной привычки не может быть связанной"
                )
            if reward:
                raise ValidationError(
                    "У приятной привычки не может быть вознаграждения"
                )

        else:
            if parent:
                if parent.nice_habit:
                    raise ValidationError(
                        'Не верная привычка в nice_habit,'
                        ' необходимо наследоваться от полезных привычек')


class WorkTimeValidator:

    def __init__(self, work_time):
        self.work_time = work_time

    def __call__(self, value):
        work_time = dict(value).get(self.work_time)
        if work_time:
            if int(work_time) >= 120:
                raise ValidationError(
                    "Время на выполнение привычки должно быть не больше 120"
                )


class PeriodValidator:
    def __init__(self, period):
        self.period = period

    def __call__(self, value):
        period = dict(value).get(self.period)
        if period:
            if int(period) > 7:
                raise ValidationError(
                    "Привычка не может иметь периодичность"
                    " выполнения реже чем раз в неделю"
                )
