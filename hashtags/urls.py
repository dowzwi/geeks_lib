from django.urls import path
from . import views

urlpatterns = [
    path("all_products/", views.all_products_list_view, name="all_products_list_view"),
    path(
        "old_products/", views.olds_products_list_view, name="olds_products_list_view"
    ),
    path(
        "youth_products/",
        views.youth_products_list_view,
        name="youth_products_list_view",
    ),
    path(
        "baby_products/", views.baby_products_list_view, name="baby_products_list_view"
    ),
]
