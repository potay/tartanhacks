# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picrank', '0002_remove_picture_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='image',
            field=models.ImageField(default='', upload_to=b''),
            preserve_default=False,
        ),
    ]
