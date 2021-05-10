from django.apps import AppConfig

class UpdaterConfig(AppConfig):
    name = 'updater'
    def ready(self):
        from updater import scheduler
        scheduler.start()