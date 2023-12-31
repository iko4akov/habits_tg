# Generated by Django 4.2.4 on 2023-09-30 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=20, null=True, verbose_name='место')),
                ('time', models.TimeField(auto_now=True, verbose_name='время выполнения')),
                ('action', models.CharField(max_length=50, verbose_name='действие')),
                ('nice_habit', models.BooleanField(default=False, verbose_name='приятная привычка')),
                ('period', models.IntegerField(default=1, verbose_name='периодичность')),
                ('reward', models.CharField(max_length=100, verbose_name='награда')),
                ('work_time', models.IntegerField(verbose_name='время на выполнение')),
                ('public', models.BooleanField(default=False, verbose_name='публичность')),
                ('create_at', models.DateTimeField(auto_now=True, verbose_name='дата создания')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='habit.habit')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
            },
        ),
    ]
