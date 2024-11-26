from . import views
from django.urls import path, include


urlpatterns = [
    path('orders/', views.OrderListView.as_view(), name='order_list'),
    path('create_order/', views.CreateOrderView.as_view(), name='create_order'),

]