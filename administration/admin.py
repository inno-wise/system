from django.contrib import admin
from .models import Designation
from django.apps import AppConfig
from django.contrib.auth.models import User


admin.site.register(Designation)
# administration/apps.py

class AdministrationConfig(AppConfig):
    name = 'administration'

    def ready(self):
        # Check and create superuser if not exists
        from django.db.models.signals import post_migrate
        post_migrate.connect(self.create_superuser, sender=self)

    def create_superuser(self, sender, **kwargs):
        username = 'inno'
        email = 'admin@domain.com'
        password = 'p@zzword'
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
