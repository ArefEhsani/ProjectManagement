# Generated by Django 4.1 on 2022-08-26 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teachers", "0007_finalreport_project"),
    ]

    operations = [
        migrations.RenameField(
            model_name="reportparts",
            old_name="report2",
            new_name="is_active",
        ),
        migrations.RemoveField(
            model_name="reportparts",
            name="report1",
        ),
        migrations.RemoveField(
            model_name="reportparts",
            name="report3",
        ),
        migrations.RemoveField(
            model_name="reportparts",
            name="report4",
        ),
        migrations.RemoveField(
            model_name="reportparts",
            name="report5",
        ),
        migrations.RemoveField(
            model_name="reportparts",
            name="report6",
        ),
        migrations.RemoveField(
            model_name="reportparts",
            name="report7",
        ),
        migrations.RemoveField(
            model_name="reportparts",
            name="report8",
        ),
        migrations.AddField(
            model_name="reportparts",
            name="number",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]