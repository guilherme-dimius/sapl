from django.apps import apps
from django.core.management.base import BaseCommand

from sapl.materia.models import MateriaLegislativa, DocumentoAcessorio
from sapl.norma.models import NormaJuridica
from sapl.parlamentares.models import Parlamentar
from sapl.protocoloadm.models import DocumentoAdministrativo,\
    DocumentoAcessorioAdministrativo
from sapl.s3 import mapa
from sapl.s3.migracao_documentos_via_request import migrar_docs_por_ids, erros


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.run()
        self.list_models_with_relation()
        self.migrar_documentos()

    def migrar_documentos(self):
        for model in [
            Parlamentar,
            # MateriaLegislativa,
            # DocumentoAcessorio,
            # NormaJuridica,
            # DocumentoAdministrativo,
            # DocumentoAcessorioAdministrativo,
        ]:
            migrar_docs_por_ids(model)

        for e in erros:
            print(e)

    def run(self):
        for item in mapa.mapa[1:]:

            old_list = item['s30_model'].objects.all()
            if 'ind_excluido' in item['fields']:
                old_list = old_list.filter(ind_excluido=0)

            for old in old_list:

                try:
                    new = item['s31_model'].objects.get(
                        pk=getattr(old, item['fields']['id']))
                except:
                    new = item['s31_model']()

                for new_field, old_field in item['fields'].items():
                    if new_field == 'ind_excluido':
                        continue
                    setattr(new, new_field, getattr(old, old_field))

                if 'adjust' in item:
                    item['adjust'](new, old)
                try:
                    new.save()
                except Exception as e:
                    print('ERRO:', item['s31_model']._meta.object_name, new, e)
            print('Migrado:', item['s31_model']._meta.object_name)

    def list_models_with_relation(self):
        sapl_apps = apps.get_app_configs()

        for app in sapl_apps:
            if app.name.startswith('sapl.') and app.name not in (
                    'sapl.s3',
                    'sapl.compilacao'):
                for name, model in app.models.items():
                    if self.is_model_mapeado(model):
                        continue
                    model_with_fk = []
                    for field in model._meta.fields:
                        if field.is_relation:
                            model_with_fk.append(field)

                    print(app.label,
                          model._meta.object_name,
                          len(model_with_fk))

    def is_model_mapeado(self, model):
        for item in mapa.mapa:
            if item['s31_model'] == model:
                return True
        for m in mapa.mapa[0]['s31_model']:
            if m == model or m == model._meta.object_name:
                return True
        return False
