# Generated by Django 3.2.6 on 2021-08-20 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google_keep', '0005_auto_20210806_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keepuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='keepuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='keepuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='keepuser',
            name='password',
            field=models.CharField(max_length=100, verbose_name='رمز'),
        ),
    ]
