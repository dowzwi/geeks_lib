from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="Укажите ТЭГ")

    def __str__(self):
        return self.name


class clothes(models.Model):
    title = models.CharField(max_length=50, null=True)
    price = models.FloatField(default=100)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
