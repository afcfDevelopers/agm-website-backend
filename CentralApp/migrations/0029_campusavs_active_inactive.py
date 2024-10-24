# Generated by Django 5.0.7 on 2024-07-26 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CentralApp", "0028_alter_campusavs_otherscheduleofservicedetails_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="campusavs",
            name="active_Inactive",
            field=models.CharField(
                choices=[("active", "active"), ("inactive", "inactive")],
                default="active",
                max_length=50,
                verbose_name="Active or Inactive",
            ),
            preserve_default=False,
        ),
    ]
