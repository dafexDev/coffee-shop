from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    photo = models.ImageField(upload_to="logos", null=True, blank=True)

    def __str__(self):
        return self.name
