# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-08 01:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estabelecimentos', '0002_local_cnpj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='cnpj',
            field=models.IntegerField(blank=True, null=True, verbose_name='CNPJ'),
        ),
    ]
