import csv
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from portal.models import Profile


class Command(BaseCommand):

    help = "Import users from CSV"

    def handle(self, *args, **kwargs):

        with open('users.csv') as file:

            reader = csv.DictReader(file)

            for row in reader:

                username = row['username']
                email = row['email']
                password = row['password']
                role = row['role']

                if not User.objects.filter(username=username).exists():

                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=password
                    )

                    Profile.objects.create(
                        user=user,
                        role=role
                    )

                    print(f"{username} created")