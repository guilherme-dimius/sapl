from django.core.management.base import BaseCommand

from sapl.parlamentares.models import Legislatura
from sapl.s3.models import S3Legislatura


class Command(BaseCommand):

    def handle(self, *args, **options):

        legislaturas = S3Legislatura.objects.all()
        for leg in legislaturas:
            if leg.ind_excluido:
                continue

            legis = Legislatura()
            legis.id = leg.num_legislatura
            legis.numero = leg.num_legislatura
            legis.data_eleicao = leg.dat_eleicao
            legis.data_inicio = leg.dat_inicio
            legis.data_fim = leg.dat_fim
            legis.save()

            print(leg.num_legislatura)
