# Generated by Django 4.1 on 2022-08-25 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_collegeusers_project"),
        ("teachers", "0004_final_report"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="final_report",
            new_name="FinalReport",
        ),
    ]
