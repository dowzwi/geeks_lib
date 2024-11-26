from django.db import models
from main_page.models import books


class Order(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    book = models.ForeignKey(books, on_delete=models.CASCADE, related_name="orders")

    def __str__(self):
        return self.name
