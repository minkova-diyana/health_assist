# Generated by Django 5.1.3 on 2024-11-22 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_pages', '0003_alter_information_type_insurance'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='information',
            name='partner_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]