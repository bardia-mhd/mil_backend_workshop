# Generated by Django 3.2.6 on 2021-08-06 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Checkbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('done', models.BooleanField(default=False)),
                ('todo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='KeepUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=100, null=True)),
                ('lastname', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('note', models.CharField(blank=True, max_length=1000, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('archived', models.BooleanField(default=False)),
                ('todos', models.ManyToManyField(related_name='todos', to='google_keep.Checkbox')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='google_keep.keepuser')),
            ],
        ),
    ]
