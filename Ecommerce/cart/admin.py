from django.contrib import admin
from .models import Cart, Order_Details


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'quantity', 'date_created')
    search_fields = ('item', 'user')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'phone_number',
                    'address_line_1', 'town', 'date_ordered')


admin.site.register(Cart, CartAdmin)
admin.site.register(Order_Details, OrderAdmin)
