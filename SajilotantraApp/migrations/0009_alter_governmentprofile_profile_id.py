# Generated by Django 5.0 on 2023-12-19 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SajilotantraApp', '0008_remove_governmentprofile_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='governmentprofile',
            name='profile_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
