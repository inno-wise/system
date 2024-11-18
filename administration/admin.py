from django.contrib import admin
from .models import Designation
from django.apps import AppConfig
from django.contrib.auth.models import User
import os
from django.db.models.signals import post_migrate

admin.site.register(Designation)
# administration/apps.py

class AdministrationConfig(AppConfig):
    name = 'administration'

    def ready(self):
        """
        Connect the post_migrate signal to ensure the superuser is created after migrations.
        """
        post_migrate.connect(self.create_superuser, sender=self)

    def create_superuser(self, sender, **kwargs):
        """
        Create a superuser if one does not exist.
        This function is connected to the `post_migrate` signal.
        """
        # Get superuser credentials from environment variables
        username = os.getenv('SUPERUSER_USERNAME', 'inno')  # Default username is 'inno'
        email = os.getenv('SUPERUSER_EMAIL', 'admin@domain.com')  # Default email
        password = os.getenv('SUPERUSER_PASSWORD', 'p@zzword')  # Default password

        # Check if the superuser already exists
        if not User.objects.filter(username=username).exists():
            # Create the superuser if not found
            User.objects.create_superuser(username=username, email=email, password=password)
            print(f"Superuser {username} created.")
        else:
            print(f"Superuser {username} already exists.")
