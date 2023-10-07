from django.db import models

from config.settings import NULLABLE


class Habit(models.Model):
    owner = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    location = models.CharField(max_length=20, verbose_name='место', **NULLABLE)
    time = models.TimeField(default='12-00-00', verbose_name='время выполнения')
    action = models.CharField(max_length=50, verbose_name='действие')

    nice_habit = models.BooleanField(verbose_name='приятная привычка', default=False)
    parent = models.ForeignKey('self', related_name='children', **NULLABLE, on_delete=models.CASCADE)

    period = models.IntegerField(default=1, verbose_name='периодичность')
    reward = models.CharField(max_length=100, verbose_name='награда', **NULLABLE)
    work_time = models.IntegerField(verbose_name='время на выполнение')
    public = models.BooleanField(default=False, verbose_name='публичность')

    create_at = models.DateTimeField(auto_now=True, verbose_name='дата создания')

    def __str__(self):
        return f'{self.action} - {self.reward}'

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
