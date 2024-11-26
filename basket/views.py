from django.shortcuts import render
from .models import Order
from basket.forms import OrderForm
from django.views import generic
from django.shortcuts import get_object_or_404


class OrderListView(generic.ListView):
    template_name = 'order/order_list.html'
    context_object_name = 'orders'
    model = Order

    def get_queryset(self):
        return Order.objects.all()


class CreateOrderView(generic.CreateView):
    form_class = OrderForm
    template_name = 'order/create_order.html'
    success_url = '/basket/orders/'

    def form_valid(self, form):
        return super(CreateOrderView, self).form_valid(form)
