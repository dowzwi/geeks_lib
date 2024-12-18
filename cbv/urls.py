from django.urls import path
from . import views


urlpatterns = [
    path('order_class/', views.BasketListView.as_view(), name='order_class_list'),
    path('order_class/<int:id>/update/', views.UpdateOrderView.as_view(), name='update'),
    path('order_class/<int:id>/delete/', views.DeleteOrderView.as_view(), name='delete'),
    path('create_orders/', views.CreateCBV.as_view(), name='create_order_list'),
]