# Generated by Django 3.2.6 on 2021-08-06 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('google_keep', '0002_alter_note_todos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='todos',
        ),
    ]
