# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-30 07:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdfunding', '0009_userextendedforfunding'),
    ]

    operations = [
        migrations.AddField(
            model_name='userextendedforfunding',
            name='group_type',
            field=models.CharField(blank=True, choices=[(b'GROUP_A', b'Group A'), (b'GROUP_B', b'Group B'), (b'GROUP_C', b'Group C'), (b'GROUP_D', b'Group D'), (b'GROUP_E', b'Group E')], max_length=2),
        ),
        migrations.AddField(
            model_name='userextendedforfunding',
            name='user_type',
            field=models.CharField(blank=True, choices=[(b'FR', b'Facilitator'), (b'MR', b'Member')], max_length=2),
        ),
    ]
