# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-11 17:33
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.contrib.auth.models import User
from sva.models import Perfil
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


def create_superuser(apps, schema_editor):
    superuser = User()
    superuser.is_active = True
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.username = 'sva_dev'
    superuser.email = 'sva@sva.cefetmg.br'
    superuser.set_password('sva_dev_password')
    superuser.perfil = Perfil()
    superuser.save()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('cidade', models.CharField(choices=[('CONTAGEM', 'Contagem'), ('CURVELO', 'Curvelo'), ('DIVINOPOLIS', 'Divinópolis'), ('LEOPOLDINA', 'Leopoldina'), ('BELO HORIZONTE', 'Belo Horizonte'), ('ARAXA', 'Araxá'), ('NEPOMUCENO', 'Nepomuceno'), ('TIMOTEO', 'Timóteo'), ('VARGINHA', 'Varginha')], max_length=45)),
                ('sigla', models.CharField(max_length=5, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[a-zA-Z0-9]', 32), 'Valor inválido para sigla. Use apenas letras e números!', 'invalid')])),
            ],
            options={
                'verbose_name_plural': 'campi',
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('sigla', models.CharField(max_length=5, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[a-zA-Z0-9]', 32), 'Valor inválido para sigla. Use apenas letras e números!', 'invalid')])),
                ('nivel_ensino', models.IntegerField(choices=[(4, 'DOUTORADO'), (3, 'MESTRADO'), (5, 'ESPECIALIZACAO'), (2, 'GRADUACAO'), (1, 'TECNICO')])),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('telefone', models.CharField(max_length=20, null=True, validators=[django.core.validators.validate_integer])),
                ('curso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sva.Curso')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RunPython(create_superuser),
    ]
