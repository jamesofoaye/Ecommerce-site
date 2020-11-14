from django.shortcuts import render, get_object_or_404
from cart.models import Cart
from django.contrib.auth import get_user_model
from django.contrib import messages
from favourites.models import Favourite
from products.models import Product

User = get_user_model()


def fav_number():
    return Favourite.objects.all().count()


def getTotalAmount():
    carts = Cart.objects.all()
    sumTotal = 0
    for cart in carts:
        sumTotal += (cart.quantity * cart.item.price)
    return sumTotal


def cart(request):
    totalAmount = getTotalAmount()
    search_results = get_serach_objs(request)

    context = {
        'totalAmount': totalAmount,
        'search_results': search_results,
    }
    if search_results:
        return render(request, 'searchresult.html', context)
    return render(request, 'cart.html', context)


def get_serach_objs(request):
    search_results = ''
    if request.method == 'POST':
        search_name = request.POST['search_objects']
        search_results = Product.objects.all().filter(name__contains=search_name)
        print('Search name is ', search_name)
        print('search result is', search_results)
        return search_results
