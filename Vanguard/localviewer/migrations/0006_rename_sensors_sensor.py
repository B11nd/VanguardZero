# Generated by Django 4.2.7 on 2023-12-03 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('localviewer', '0005_alter_sensors_payload_alter_sensors_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='sensors',
            new_name='sensor',
        ),
    ]