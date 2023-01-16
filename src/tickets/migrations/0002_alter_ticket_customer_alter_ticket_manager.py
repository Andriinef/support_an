# Generated by Django 4.1.5 on 2023-01-16 10:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tickets", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticket",
            name="customer",
            field=models.ForeignKey(
                default=3,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="customer_tickets",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="manager",
            field=models.ForeignKey(
                default=1,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="manager_tickets",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
