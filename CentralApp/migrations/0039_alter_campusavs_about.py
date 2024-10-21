# Generated by Django 5.0.7 on 2024-08-14 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CentralApp", "0038_alter_campusavs_nrp_picture1_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="campusavs",
            name="about",
            field=models.TextField(
                help_text="State the reason why Fellowhip is not active, and give the details of who someone that we can reachout to.",
                verbose_name="Remarks or Report if Inactive",
            ),
        ),
    ]
