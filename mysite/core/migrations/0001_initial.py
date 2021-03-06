# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-25 16:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('gcm', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('mobile', models.BigIntegerField(null=True, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('picture', models.CharField(blank=True, max_length=1024, null=True)),
                ('thumbnail', models.CharField(blank=True, max_length=1024, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=1, null=True)),
                ('referral_code', models.CharField(blank=True, max_length=15, null=True)),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('is_player', models.BooleanField(default=False)),
                ('is_contractor', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
