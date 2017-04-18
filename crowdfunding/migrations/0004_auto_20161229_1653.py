# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-29 11:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crowdfunding', '0003_crowdfundingpostproposal_num_votes'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrowdFundingProposalVoting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('upvotes', models.BooleanField()),
                ('downvotes', models.BooleanField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='crowdfundingpostproposal',
            name='num_votes',
        ),
    ]