from django.contrib import admin

from habit.models import Habit


class HabitModelAdmin(admin.ModelAdmin):
    list_filter = ('public', 'owner')
    search_fields = ('public', 'owner')


admin.site.register(Habit, HabitModelAdmin)
