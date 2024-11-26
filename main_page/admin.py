from django.contrib import admin
from . import models

admin.site.register(models.books)
admin.site.register(models.ReviewBook)
