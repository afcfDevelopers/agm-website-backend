# Generated by Django 4.0.5 on 2024-07-10 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CentralApp', '0007_rename_program_campusavsreport_program_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campusavsreport',
            name='body1',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='campusavsreport',
            name='body2',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='campusavsreport',
            name='body3',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='campusavsreport',
            name='picture1',
            field=models.ImageField(blank=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='campusavsreport',
            name='picture2',
            field=models.ImageField(blank=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='campusavsreport',
            name='picture4',
            field=models.ImageField(blank=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='campusavsreport',
            name='picture5',
            field=models.ImageField(blank=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='campusavsreport',
            name='program_type',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
