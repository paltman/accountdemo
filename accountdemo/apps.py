from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "accountdemo"

    def ready(self):
        import_module("accountdemo.receivers")
