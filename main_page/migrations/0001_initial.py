# Generated by Django 4.2.16 on 2024-11-23 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Books",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="books/", verbose_name="Загрузите обложку книги"
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=100, verbose_name="Укажите название книги"
                    ),
                ),
                ("price", models.FloatField(verbose_name="Укажите цену")),
                (
                    "release_date",
                    models.DateField(verbose_name="Укажите дату написания"),
                ),
                (
                    "genre",
                    models.CharField(
                        choices=[
                            ("Манга", "Манга"),
                            ("Комедия", "Комедия"),
                            ("Сказка", "Сказка"),
                        ],
                        default="Комедия",
                        max_length=100,
                        verbose_name="Укажите жанр книги",
                    ),
                ),
                (
                    "author",
                    models.CharField(max_length=100, verbose_name="Укажите имя автора"),
                ),
                (
                    "audio",
                    models.URLField(
                        verbose_name="Вставьте ссылку на аудио книгу с YouTube"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, verbose_name="Укажите почту автора"
                    ),
                ),
            ],
            options={
                "verbose_name": "Книга",
                "verbose_name_plural": "Книги",
            },
        ),
    ]
