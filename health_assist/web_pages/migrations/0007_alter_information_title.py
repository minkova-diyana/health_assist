# Generated by Django 5.1.3 on 2025-01-02 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_pages', '0006_populate_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
    ]