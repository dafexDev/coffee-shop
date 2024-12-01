from django.urls import re_path

from .views import ProductFormView, ProductListView


app_name = "products"


urlpatterns = [
    re_path(r"^$", ProductListView.as_view(), name="list_product"),
    re_path(r"^add/$", ProductFormView.as_view(), name="add_product"),
]
