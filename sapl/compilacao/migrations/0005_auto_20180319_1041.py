# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-03-19 13:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def adjust_dispositivo_raiz(apps, schema_editor):
    Dispositivo = apps.get_model('compilacao', 'Dispositivo')

    articulacoes = Dispositivo.objects.filter(
        dispositivo_pai__isnull=True)

    def adicionar_raiz_aos_filhos(raiz, dispositivo):
        for d in dispositivo.dispositivos_filhos_set.all():
            d.dispositivo_raiz = raiz
            d.save()
            adicionar_raiz_aos_filhos(raiz, d)

    for artic in articulacoes:
        adicionar_raiz_aos_filhos(artic, artic)


class Migration(migrations.Migration):

    dependencies = [
        ('compilacao', '0004_auto_20171031_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispositivo',
            name='dispositivo_raiz',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='nodes', to='compilacao.Dispositivo', verbose_name='Dispositivo Raiz'),
        ),
        migrations.AlterUniqueTogether(
            name='dispositivo',
            unique_together=set([('ta', 'dispositivo0', 'dispositivo1', 'dispositivo2', 'dispositivo3', 'dispositivo4', 'dispositivo5',
                                  'tipo_dispositivo', 'dispositivo_raiz', 'dispositivo_pai', 'dispositivo_atualizador', 'ta_publicado', 'publicacao'), ('ta', 'ordem')]),
        ),
        migrations.RunPython(adjust_dispositivo_raiz),
    ]