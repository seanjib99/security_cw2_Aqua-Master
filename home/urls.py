from django.urls import path
from .views import home, productlist, productdetail, search, cart, Checkout, add_to_wishlist, wishlist, add_to_cart, remove_from_cart, delete_from_cart, place_order, orders, contact, subscription_email, terms, about

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('subscription-email/', subscription_email, name='subscription_email'),
    path('about/', about, name='about'),
    path('terms/', terms, name='terms'),
    path('products/', productlist, name='products'),
    path('productdetail/<int:id>/', productdetail, name='productdetail'),
    path('search/', search, name='search'),
    path('wishlist/', wishlist, name='wishlist'),
    path('cart/', cart, name='cart'),
    path('checkout/', Checkout.as_view(), name='checkout'),
    path('orders/', orders, name='orders'),
    path('add-to-wishlist/', add_to_wishlist, name='add_to_wishlist'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/', remove_from_cart, name='remove_from_cart'),
    path('delete-from-cart/', delete_from_cart, name='delete_from_cart'),
    path('place-order/', place_order, name='place_order'),
]