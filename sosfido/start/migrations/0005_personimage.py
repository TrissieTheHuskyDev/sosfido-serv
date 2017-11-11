# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-20 00:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0004_auto_20171003_0317'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='photos/users/profile')),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start.Person')),
            ],
        ),
    ]