# Generated by Django 4.1.4 on 2022-12-22 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bbpsrepaymentschedule",
            name="loan_id",
        ),
        migrations.RemoveField(
            model_name="bbpsrepaymentschedule",
            name="user",
        ),
        migrations.AlterField(
            model_name="bbpsrepaymentschedule",
            name="account_id",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="bbpsrepaymentschedule",
            name="due_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="bbpsrepaymentschedule",
            name="status",
            field=models.CharField(
                choices=[("PAID", "PAID"), ("DUE", "DUE")], max_length=64
            ),
        ),
    ]
