# Generated by Django 3.2.13 on 2022-11-23 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='core/static/media/pfp'),
        ),
    ]
