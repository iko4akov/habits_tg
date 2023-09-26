import os

from django.core.management import BaseCommand
from dotenv import load_dotenv

from user.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        load_dotenv()
        super_user = User.objects.create(
            email='admin@admin.com',
            country='Russia',
            is_staff=True,
            is_superuser=True,
        )

        super_user.set_password(os.getenv('PASSWORD_SU'))
        super_user.save()
