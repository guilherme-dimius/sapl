# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-10-31 12:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0032_auto_20181022_1743'),
        ('parlamentares', '0025_auto_20180924_1724'),
        ('sessao', '0029_auto_20181024_0952'),
    ]

    operations = [
        migrations.CreateModel(
            name='RetiradaPauta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacao', models.TextField(blank=True, verbose_name='Observações')),
                ('expediente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sessao.ExpedienteMateria')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materia.MateriaLegislativa')),
                ('ordem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sessao.OrdemDia')),
                ('parlamentar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='parlamentares.Parlamentar', verbose_name='Requerente')),
            ],
            options={
                'verbose_name_plural': 'Retirada de Pauta',
                'verbose_name': 'Retirada de Pauta',
            },
        ),
        migrations.CreateModel(
            name='TipoRetiradaPauta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição')),
            ],
            options={
                'verbose_name_plural': 'Tipos de Retirada de Pauta',
                'verbose_name': 'Tipo de Retidara de Pauta',
                'ordering': ['descricao'],
            },
        ),
        migrations.AddField(
            model_name='retiradapauta',
            name='tipo_de_retirada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sessao.TipoRetiradaPauta', verbose_name='Motivo de Retirada de Pauta'),
        ),
    ]
