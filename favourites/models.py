from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item.name

    """def getname(self):
        return Product.objects.filter(name=self.item.name)"""
