from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .models import Product, Category
from cart.models import Cart, Order_Details
from favourites.models import Favourite
from django.contrib import messages
from django.contrib.auth import get_user_model
import json
from .forms import ProductFilter
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings


def fav_number():
    return Favourite.objects.all().count()


def cart_number():
    return Cart.objects.all().count()


def getTotalAmount():
    carts = Cart.objects.all()
    sumTotal = 0
    for cart in carts:
        sumTotal += (cart.quantity * cart.item.price)
    return sumTotal


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['user_password']
        user = authenticate(request,
                            username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('shop')
        else:
            messages.warning(request, 'Log in failed')

    return render(request, 'signin.html')


def signout(request):
    logout(request)
    return redirect('shop')


def signup(request):
    """creating user/ customer"""
    if request.method == 'POST':
        firstname = request.POST['full_name']
        last_name = request.POST['last']
        username = request.POST.get('user_name', False)
        email = request.POST['user_email']
        password = request.POST['user_password']

        user = User.objects.create_user(
            last_name=last_name, first_name=firstname, username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Account created')
        return redirect('sign_in')

    return render(request, 'signup.html')


def home(request):
    products = Product.objects.all().order_by('date_added')
    search_results = get_serach_objs(request)

    context = {
        'products': products,
        'search_results': search_results
    }
    if search_results:
        return render(request, 'searchresult.html', context)
    return render(request, 'index.html', context)


def shop(request):
    products = Product.objects.all().order_by('date_added')
    categories = Category.objects.all()
    cart = Cart.objects.all()
    search_results = get_serach_objs(request)

    productnumber = Product.objects.all().count()
    paginator = Paginator(products, 9)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    p = paginator.page(page_number)
    totalpageitems = p.object_list.count()

    context = {
        'products': products,
        'productnumber': productnumber,
        'page_obj': page_obj,
        'totalpageitems': totalpageitems,
        'categories': categories,
        'search_results': search_results,
    }
    if search_results:
        return render(request, 'searchresult.html', context)
    return render(request, 'shop.html', context)


def detail(request, pk):
    product = Product.objects.get(name=pk)
    products = Product.objects.all().order_by('date_added')
    search_results = get_serach_objs(request)

    context = {
        'product': product,
        'products': products,
        'search_results': search_results,

    }
    if search_results:
        return render(request, 'searchresult.html', context)
    return render(request, 'detail.html', context)


def checkout(request):
    carts = Cart.objects.all()
    totalAmount = getTotalAmount()
    search_results = get_serach_objs(request)

    user = request.user

    context = {
        'carts': carts,
        'totalAmount': totalAmount,
        'search_results': search_results,
    }
    if search_results:
        return render(request, 'searchresult.html', context)
    if Cart.objects.all().count() < 1:
        messages.info(request, 'No item in cart')
        return redirect('cart')
    else:
        if request.user.is_authenticated:
            if request.method == 'POST':
                firstname = request.POST['user_firstName']
                lastname = request.POST['user_lastName']
                user_email = request.POST['user_eamil']
                phone = request.POST['user_contact']
                company = request.POST['user_company']
                address1 = request.POST['address1']
                address2 = request.POST['address2']
                town = request.POST['user_town']
                country = request.POST['user_country']

                order = Order_Details.objects.create(user=user, first_name=firstname, last_name=lastname, email=user_email,
                                                     phone_number=phone, total_amount=totalAmount, conmpany=company, address_line_1=address1, address_line_2=address2, town=town, country=country)
                order.order_items.set(carts)
                if order.DoesNotExist():
                    order.save()
                    # send_mail(
                    #     "New order",
                    #     "New order has been placed by a customer",
                    #     user_email,
                    #     ['apunguray@gmail.com'],
                    #     fail_silently=False
                    # )
                    messages.success(request, 'Oerder created!!')
                    return redirect('shop')
                else:
                    messages.info(request, 'Oerder failed!!')

            return render(request, 'checkout.html', context)
        else:
            return redirect('sign_in')


def contact(request):
    search_results = get_serach_objs(request)
    context = {
        'search_results': search_results,
    }
    if search_results:
        return render(request, 'searchresult.html', context)
    return render(request, 'contact.html')


def favourites(request):
    favs = Favourite.objects.all()
    search_results = get_serach_objs(request)
    context = {
        'search_results': search_results,
    }
    if search_results:
        return render(request, 'searchresult.html', context)
    if favs.count() < 1:
        messages.info(request, 'Wishlist is empty')
        return redirect('shop')
    else:
        return render(request, 'favourites.html')


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    productQuantity = None
    user = request.user

    if action == 'add':
        try:
            productQuantity = data['quantity']
        except KeyError:
            productQuantity = 1
        product = Product.objects.get(id=productId)
        if not Cart.objects.filter(user=user, item=product).exists():
            cartItem = Cart.objects.create(
                user=user, item=product, quantity=productQuantity)
            cartItem.save()
        """if not Order.objects.filter(user=user, ordered=False).exists():
            orderitem = Order.objects.create(user=user, ordered=False)
            if orderitem:
                orderitem.orderitems.set(product)
                orderitem.save()"""

    return JsonResponse('Item added to cart', safe=False)


def removeItem(request):
    data = json.loads(request.body)
    productId = data['productId']

    user = request.user
    product = Product.objects.get(id=productId)

    if Cart.objects.filter(user=user, item=product).exists():
        cartItem = Cart.objects.get(item=product)
        cartItem.delete()

    return JsonResponse('Item removed', safe=False)


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['filter'] = ProductFilter(
        self.request.GET, queryset=self.get_queryset())
    return context


def addToFav(request):
    data = json.loads(request.body)
    product_name = data['productName']
    action = data['action']
    user = request.user

    if action == 'wishlist':
        product = Product.objects.get(name=product_name)
        if not Favourite.objects.filter(user=user, item=product).exists():
            favourite = Favourite.objects.create(user=user, item=product)
            favourite.save()
    return JsonResponse('Added to wish list', safe=False)


def removeFavourite(request):
    data = json.loads(request.body)
    product_name = data['productName']
    action = data['action']
    user = request.user

    if action == 'remove-fav':
        product = Favourite.objects.get(name=product_name)
        if Favourite.objects.filter(user=user, item=product).exists():
            item = Favourite.objects.get(item=product)
            item.delete()

    return JsonResponse('Remove successfully', safe=False)


"""    if action == 'add':
        cartItem = Cart.objects.get(item=product)
        if cartItem in carts:
            cartItem.quantity += 1
            cartItem.save()
        else:
            cartItem.quantity = 1
            cartItem.save()
"""


# def serach_result_page(request):
#     if request.method == 'POST':
#         search_name = request.POST['search_objects']
#         search_results = Product.objects.all().filter(name__contains=search_name)
#         print('Search name is ', search_name)
#         print('search result is', search_results)
#     return render(request, 'searchresult.html')


def get_serach_objs(request):
    search_results = ''
    if request.method == 'POST':
        search_name = request.POST['search_objects']
        search_results = Product.objects.all().filter(name__contains=search_name)
        print('Search name is ', search_name)
        print('search result is', search_results)
        return search_results
