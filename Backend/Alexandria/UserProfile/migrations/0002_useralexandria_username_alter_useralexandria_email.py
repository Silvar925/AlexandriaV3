# Generated by Django 5.0.1 on 2024-01-17 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useralexandria',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Usename'),
        ),
        migrations.AlterField(
            model_name='useralexandria',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='E-mail'),
        ),
    ]
