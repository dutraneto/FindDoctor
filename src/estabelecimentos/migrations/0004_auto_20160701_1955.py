# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-01 22:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estabelecimentos', '0003_auto_20160629_0845'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Estabelecimento',
            new_name='Local',
        ),
        migrations.RenameField(
            model_name='cidade',
            old_name='estado_id',
            new_name='estado',
        ),
        migrations.RenameField(
            model_name='cidade',
            old_name='nome',
            new_name='nomeCidade',
        ),
        migrations.RenameField(
            model_name='estado',
            old_name='nome',
            new_name='nomeEstado',
        ),
        migrations.RenameField(
            model_name='local',
            old_name='nome',
            new_name='nomeLocal',
        ),
    ]