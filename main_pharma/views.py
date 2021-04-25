from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *
from .forms import FormMessage
from django.views.decorators.csrf import csrf_exempt
from cart.cart import Cart
from django.core.paginator import Paginator
from .filter import ProductFilter


def main_page_view(request):
    categories = Category.objects.filter(is_visible=True).order_by('category_order')
    products_pop = Product.objects.filter(is_popular=True)
    products_new = Product.objects.filter(is_new=True)
    welcome = Welcome.objects.all()
    specofferblue = SpecOfferBlue.objects.all()
    specoffergreen = SpecOfferGreen.objects.all()
    specofferyellow = SpecOfferYellow.objects.all()
    testimonials = Testimonials.objects.all()
    rate = Rate.objects.all()
    address = Address.objects.filter(is_visible=True)
    phone = Phone.objects.filter(is_visible=True)
    email = Email.objects.filter(is_visible=True)
    aboutus = AboutUs.objects.all()

    return render(request, 'index.html', context={

        'categories': categories,
        'products_pop': products_pop,
        'products_new': products_new,
        'welcome': welcome[0],
        'specofferblue': specofferblue[0],
        'specoffergreen': specoffergreen[0],
        'specofferyellow': specofferyellow[0],
        'testimonials': testimonials,
        'rate': rate,
        'address': address[0],
        'phone': phone[0],
        'email': email[0],
        'aboutus': aboutus[0]

    })


def shop_page_view(request):
    product = Product.objects.filter(is_visible=True)
    address = Address.objects.filter(is_visible=True)
    phone = Phone.objects.filter(is_visible=True)
    email = Email.objects.filter(is_visible=True)
    aboutus = AboutUs.objects.all()
    categories = Category.objects.filter(is_visible=True).order_by('category_order')
    myFilter = ProductFilter(request.GET, queryset=Product.objects.all())
    product = myFilter.qs

    return render(request, 'shop.html', context={

        'product': product,
        'address': address[0],
        'phone': phone[0],
        'email': email[0],
        'aboutus': aboutus[0],
        'categories': categories,
        'myFilter': myFilter

    })


def prod_page_view(request, slug):
    product = Product.objects.get(slug=slug)
    address = Address.objects.filter(is_visible=True)
    phone = Phone.objects.filter(is_visible=True)
    email = Email.objects.filter(is_visible=True)
    aboutus = AboutUs.objects.all()
    categories = Category.objects.filter(is_visible=True).order_by('category_order')

    return render(request, 'product.html', context={

        'product': product,
        'address': address[0],
        'phone': phone[0],
        'email': email[0],
        'aboutus': aboutus[0],
        'categories': categories

    })


def about_page_view(request):
    welcome = Welcome.objects.all()
    history = History.objects.all()
    ouroffer = OurOffer.objects.all()
    ourteam = OurTeam.objects.all()
    address = Address.objects.filter(is_visible=True)
    phone = Phone.objects.filter(is_visible=True)
    email = Email.objects.filter(is_visible=True)
    aboutus = AboutUs.objects.all()
    categories = Category.objects.filter(is_visible=True).order_by('category_order')

    return render(request, 'about_us.html', context={

        'welcome': welcome[0],
        'history': history,
        'ouroffer': ouroffer,
        'ourteam': ourteam,
        'address': address[0],
        'phone': phone[0],
        'email': email[0],
        'aboutus': aboutus[0],
        'categories': categories

    })


@csrf_exempt
def contact_us_page_view(request):

    if request.method == 'POST':
        form = FormMessage(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    form = FormMessage
    address = Address.objects.filter(is_visible=True)
    phone = Phone.objects.filter(is_visible=True)
    email = Email.objects.filter(is_visible=True)
    aboutus = AboutUs.objects.all()
    categories = Category.objects.filter(is_visible=True).order_by('category_order')

    return render(request, 'contact_us.html', context={

        'form': form,
        'address': address[0],
        'phone': phone[0],
        'email': email[0],
        'aboutus': aboutus[0],
        'categories': categories

    })


def product_list(request, category_slug=None):
    cart = Cart(request)
    products = Product.objects.filter(available=True)
    address = Address.objects.filter(is_visible=True)
    phone = Phone.objects.filter(is_visible=True)
    email = Email.objects.filter(is_visible=True)
    aboutus = AboutUs.objects.all()
    categories = Category.objects.filter(is_visible=True).order_by('category_order')
    return render(request, 'shop.html', {
        'products': products,
        'cart': cart,
        'address': address[0],
        'phone': phone[0],
        'email': email[0],
        'aboutus': aboutus[0],
        'categories': categories
    })


def product_detail(request, id, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request,
                  'product.html',
                  {'product': product, 'cart': cart}
                  )


def search_product(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Product.objects.filter(name__contains=query_name)
            return render(request, 'product-search.html', {"results":results})

    return render(request, 'product-search.html')