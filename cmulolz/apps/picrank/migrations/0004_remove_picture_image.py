# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picrank', '0003_picture_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='image',
        ),
    ]
