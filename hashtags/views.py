from django.shortcuts import render
from . import models


def all_products_list_view(request):
    if request.method == "GET":
        products_list = models.clothes.objects.filter().order_by("-id")
        context = {"products_list": products_list}
        return render(request, "all_products_list_view.html", context=context)


def olds_products_list_view(request):
    if request.method == "GET":
        old = models.clothes.objects.filter(tags__name="Старики").order_by("-id")
        context = {"old": old}
        return render(request, "old.html", context=context)


def youth_products_list_view(request):
    if request.method == "GET":
        youth = models.clothes.objects.filter(tags__name="Молодые").order_by("-id")
        context = {"youth": youth}
        return render(request, "youth.html", context=context)


def baby_products_list_view(request):
    if request.method == "GET":
        baby = models.clothes.objects.filter(tags__name="Дети").order_by("-id")
        context = {"baby": baby}
        return render(request, "baby.html", context=context)
