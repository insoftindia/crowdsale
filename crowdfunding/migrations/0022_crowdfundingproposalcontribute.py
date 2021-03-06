# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-04 06:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crowdfunding', '0021_userextendedforfunding_ether_account_private_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrowdFundingProposalContribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('contributer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('proposal_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crowdfunding.CrowdFundingPostProposal')),
            ],
        ),
    ]
