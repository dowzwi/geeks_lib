from basket.models import Order
from basket.forms import OrderForm
from django.shortcuts import get_object_or_404
from django.views import generic


class BasketListView(generic.ListView):
    template_name = "order/order_list.html"
    context_object_name = "orders"
    model = Order

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')

class CreateCBV(generic.CreateView):
    template_name = 'order/create_order.html'
    form_class = OrderForm
    success_url = 'order_class/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateCBV, self).form_valid(form=form)


class UpdateOrderView(generic.UpdateView):
    template_name = 'order/update_order.html'
    form_class = OrderForm
    success_url = 'order_class/'

    def from_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateOrderView, self).form_valid(form=form)

    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(Order, id=todo_id)


class DeleteOrderView(generic.DeleteView):
    template_name = 'order/delete_order.html'
    success_url = 'order_class/'


    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(Order, id=todo_id)
