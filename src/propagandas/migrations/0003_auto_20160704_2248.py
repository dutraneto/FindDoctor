# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-04 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propagandas', '0002_auto_20160704_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propaganda',
            name='urlImgPropaganda',
            field=models.ImageField(blank=True, max_length=80, null=True, upload_to='propagandas/images', verbose_name='Numero'),
        ),
    ]