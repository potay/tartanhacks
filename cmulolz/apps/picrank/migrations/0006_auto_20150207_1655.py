# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picrank', '0005_picture_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='timestamp',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
