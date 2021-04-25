from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET

from main_pharma.models import *

from .cart import Cart


@require_GET
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1)
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    address = Address.objects.filter(is_visible=True)
    phone = Phone.objects.filter(is_visible=True)
    email = Email.objects.filter(is_visible=True)
    aboutus = AboutUs.objects.all()
    categories = Category.objects.filter(is_visible=True).order_by('category_order')
    return render(request, 'cart_detail.html',
                  {'cart': cart,
                   'address': address[0],
                   'phone': phone[0],
                   'email': email[0],
                   'aboutus': aboutus[0],
                   'categories': categories})
