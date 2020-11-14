from cart.models import Cart
from favourites.models import Favourite
from products.models import Product
from django.shortcuts import render, redirect

def fav_number():
    return Favourite.objects.all().count()


def cart_number():
    return Cart.objects.all().count()


def add_variable_to_context(request):
    carts = Cart.objects.all()
    cartnumber = carts.count()
    favnumber = fav_number()
    favs = Favourite.objects.all()

    return {
        'carts': carts,
        'cartnumber': cartnumber,
        'favnumber': favnumber,
        'favs': favs
    }

