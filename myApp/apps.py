
# myapp/apps.py

from django.apps import AppConfig

class MyappConfig(AppConfig):
    name = 'myapp'
    verbose_name = "My Application"

    def ready(self):
        import myapp.signals
 