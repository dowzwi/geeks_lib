# Generated by Django 4.2.16 on 2024-11-25 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_page", "0002_reviewbook"),
    ]

    operations = [
        migrations.AddField(
            model_name="books",
            name="available_copies",
            field=models.PositiveIntegerField(
                default=0, null=True, verbose_name="Количество доступных экземпляров"
            ),
        ),
    ]
