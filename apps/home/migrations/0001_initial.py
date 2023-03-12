# Generated by Django 3.2.13 on 2023-01-23 01:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, default='no registrado', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ComputoRegistrado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('modelo', models.CharField(blank=True, max_length=200, null=True)),
                ('ip_dir', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('mac_dir', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('date_registed', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('Area', models.ForeignKey(default='no registrado', on_delete=django.db.models.deletion.CASCADE, to='home.area')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('ip_dir', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('mac_dir', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('status', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Taken by staff', 'Taken by staff'), ('Solved', 'Solved')], default='Pending', max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('screenshot', models.ImageField(blank=True, default=None, null=True, upload_to='static/media/screenshot')),
                ('habilited', models.BooleanField(default=True)),
                ('Area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.area')),
                ('ComputoRegistrado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.computoregistrado')),
                ('customer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='related_customerl_user', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('takenby', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_takenby_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_software', models.CharField(blank=True, max_length=200, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('ServiceRequest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.servicerequest')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('screenshot', models.ImageField(blank=True, default=None, null=True, upload_to='static/media/screenshot')),
                ('ServiceRequest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.servicerequest')),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_equipo', models.CharField(blank=True, max_length=200, null=True)),
                ('modelo', models.CharField(blank=True, max_length=200, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('ServiceRequest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.servicerequest')),
            ],
        ),
    ]
