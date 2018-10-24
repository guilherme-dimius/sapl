from django import apps
from django.utils.translation import ugettext_lazy as _


class AppConfig(apps.AppConfig):
    name = 'sapl.s3'
    label = 's3'
    verbose_name = _('S3 Import Sapl 3.0 de Jataí')
