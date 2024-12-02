from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Order


class MyOrderViewTests(TestCase):
    def test_no_logged_user_should_redirect(self):
        url = reverse("orders:my_order")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/auth/login?next=/orders/my-order/")
    
    def test_logged_user_should_return_404(self):
        url = reverse("orders:my_order")
        user = get_user_model().objects.create(username="test")
        self.client.force_login(user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        
    def test_logged_user_with_order_created_should_return_200(self):
        url = reverse("orders:my_order")
        user = get_user_model().objects.create(username="test")
        order = Order.objects.create(is_active=True, user=user)
        self.client.force_login(user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["order"].id, order.id)
        self.assertEqual(response.context["order"].orderproduct_set.count(), 0)
