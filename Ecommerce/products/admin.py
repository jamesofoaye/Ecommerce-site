from django.contrib import admin
from .models import Product, Offer, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'date_added')
    search_fields = ('name', 'category')


admin.site.register(Offer)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
