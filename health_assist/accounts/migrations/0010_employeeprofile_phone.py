# Generated by Django 5.1.3 on 2024-11-28 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_employeeprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeprofile',
            name='phone',
            field=models.ImageField(blank=True, max_length=11, null=True, upload_to=''),
        ),
    ]