from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item.name

    @property
    def total(self):
        return self.quantity * self.item.price


class Order_Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_items = models.ManyToManyField(Cart)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    conmpany = models.CharField(max_length=200, null=True, blank=True)
    address_line_1 = models.CharField(max_length=200)
    address_line_2 = models.CharField(max_length=200, null=True, blank=True)
    town = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_amount = models.FloatField()

    class Meta:
        verbose_name_plural = "Order details"

    def __str__(self):
        return self.first_name
