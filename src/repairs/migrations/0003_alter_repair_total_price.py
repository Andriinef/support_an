# Generated by Django 4.1.4 on 2022-12-23 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("repairs", "0002_remove_parts_total_parts_total_price_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="repair",
            name="total_price",
            field=models.IntegerField(
                default=0.0,
                help_text="грн.",
                verbose_name="Загальна вартість робот та послуг",
            ),
        ),
    ]