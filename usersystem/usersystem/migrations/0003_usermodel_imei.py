# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersystem', '0002_remove_usermodel_passwordchanged'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='imei',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
