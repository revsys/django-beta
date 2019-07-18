# Generated by Django 2.2.3 on 2019-07-18 04:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BetaSignup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=75, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('contacted', models.BooleanField(default=False, verbose_name='Contacted')),
                ('registered', models.BooleanField(default=False, verbose_name='Registered')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='Created')),
            ],
            options={
                'verbose_name': 'Beta Signup',
                'verbose_name_plural': 'Beta Signups',
            },
        ),
    ]