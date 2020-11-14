from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('detail/<str:pk>', views.detail, name='detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('remove_item/', views.removeItem, name='remove_item'),
    path('add_fav/', views.addToFav, name='add_fav'),
    path('contact/', views.contact, name='contact'),
    path('sign_up/', views.signup, name='sign_up'),
    path('sign_in/', views.signin, name='sign_in'),
    path('sign_out/', views.signout, name='sign_out'),
    path('favourit/', views.favourites, name='favourit'),
    path('remove_favorite/', views.removeFavourite, name='remove_favorite'),
    path('serach_results/', views.get_serach_objs, name='serach_results'),
]
