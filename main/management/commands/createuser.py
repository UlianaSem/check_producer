from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        username = "User_producer"

        if not User.objects.filter(username=username).exists():
            user = User.objects.create(username=username)
            user.set_password('producer')
            user.save()
