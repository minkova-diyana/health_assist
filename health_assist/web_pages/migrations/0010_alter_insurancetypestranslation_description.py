# Generated by Django 5.1.3 on 2025-03-27 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_pages', '0009_insurancetypes_alter_informationtranslation_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurancetypestranslation',
            name='description',
            field=models.TextField(max_length=100),
        ),
    ]
