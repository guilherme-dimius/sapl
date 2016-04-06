# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-19 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compilacao', '0045_auto_20160311_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='inconstitucionalidade',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=False, verbose_name='Declarado Inconstitucional'),
        ),
        migrations.AlterField(
            model_name='dispositivo',
            name='texto',
            field=models.TextField(blank=True, default='', verbose_name='Texto Original'),
        ),
    ]
