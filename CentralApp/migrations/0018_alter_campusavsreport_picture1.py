# Generated by Django 3.2.25 on 2024-07-13 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CentralApp', '0017_alter_campusavsreport_picture1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campusavsreport',
            name='picture1',
            field=models.ImageField(blank=True, upload_to='report_images/'),
        ),
    ]