from django.apps import apps
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):

        sapl_apps = apps.get_app_configs()

        for app in sapl_apps:
            if app.name.startswith('sapl.') and not app.name.endswith('s3'):
                for name, model in app.models.items():
                    model_with_fk = False
                    for field in model._meta.fields:
                        if field.is_relation:
                            model_with_fk = True
                    if not model_with_fk:
                        print(app.label, model._meta.object_name)
