# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-03 07:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crowdfunding', '0014_auto_20170102_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextendedforfunding',
            name='group_type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='crowdfunding.CrowdFundingMemberGroup'),
        ),
    ]