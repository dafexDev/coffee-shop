from django.urls import re_path

from .views import MyOrderView, CreateOrderProductView


app_name = "orders"


urlpatterns = [
    re_path(r"^my-order/$", MyOrderView.as_view(), name="my_order"),
    re_path(r"^add-product/$", CreateOrderProductView.as_view(), name="add_product")
]
