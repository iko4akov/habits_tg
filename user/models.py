from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')

    avatar = models.ImageField(upload_to='user/', verbose_name='Аватар', **NULLABLE)
    name = models.CharField(verbose_name='Имя', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='Country', **NULLABLE)

    check_email = models.BooleanField(default=False, verbose_name='Подтверждение почты')
    verify_number = models.CharField(max_length=150, verbose_name='verify_number', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return "%s %s" % ("Пользователь: ", self.email)

    class Meta:
        permissions = [
            (
                'view_users',
                'Can view users'
            ),
        ]
