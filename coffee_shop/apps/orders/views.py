from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Order
from .forms import OrderProductForm


class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/my_order.html"
    context_object_name = "order"
    
    def get_object(self, queryset=None):
        user = self.request.user
        return get_object_or_404(Order.objects.filter(user=user, is_active=True))


class CreateOrderProductView(LoginRequiredMixin, CreateView):
    template_name = "orders/create_order_product.html"
    form_class = OrderProductForm
    success_url = reverse_lazy("orders:my_order")
    
    def form_valid(self, form: OrderProductForm):
        order, _ = Order.objects.get_or_create(
            is_active=True,
            user=self.request.user
        )
        form.instance.order = order
        form.instance.quantity = 1
        form.save()
        return super().form_valid(form)