from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DeleteView, UpdateView, CreateView, DetailView
from admin_pharma.forms import *
from main_pharma.models import *
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from braces.views import GroupRequiredMixin
from order.models import Order, OrderItem


def is_member(user):
    return user.groups.filter(name='manager').exists() or \
           user.is_staff


@login_required(login_url='/login/')
@user_passes_test(is_member)
def main_admin_view(request):
    address = Address.objects.filter(is_visible=True)
    phone = Phone.objects.filter(is_visible=True)
    email = Email.objects.filter(is_visible=True)
    aboutus = AboutUs.objects.all()
    categories = Category.objects.filter(is_visible=True).order_by('category_order')
    return render(request, 'main_admin.html', context={

        'address': address[0],
        'phone': phone[0],
        'email': email[0],
        'aboutus': aboutus[0],
        'categories': categories

    })


@login_required(login_url='/login/')
@user_passes_test(is_member)
def list_of_messages(request):
    address = Address.objects.filter(is_visible=True)
    phone = Phone.objects.filter(is_visible=True)
    email = Email.objects.filter(is_visible=True)
    aboutus = AboutUs.objects.all()
    categories = Category.objects.filter(is_visible=True).order_by('category_order')
    messages = Message.objects.filter(is_processed=False).order_by('pub_date')
    paginator = Paginator(messages, 2)
    page = request.GET.get('page')
    messages = paginator.get_page(page)
    return render(request, 'messages.html', context={

        'messages': messages,
        'address': address[0],
        'phone': phone[0],
        'email': email[0],
        'aboutus': aboutus[0],
        'categories': categories

    })


@login_required(login_url='/login/')
@user_passes_test(is_member)
def update_message(request, pk):
    Message.objects.filter(pk=pk).update(is_processed=True)
    return redirect('/admin-panel/messages/')


@login_required(login_url='/login/')
@user_passes_test(is_member)
def list_of_products(request):
    product = Product.objects.all()
    address = Address.objects.filter(is_visible=True)
    phone = Phone.objects.filter(is_visible=True)
    email = Email.objects.filter(is_visible=True)
    aboutus = AboutUs.objects.all()
    categories = Category.objects.filter(is_visible=True).order_by('category_order')
    return render(request, 'products.html', context={

        'product': product,
        'address': address[0],
        'phone': phone[0],
        'email': email[0],
        'aboutus': aboutus[0],
        'categories': categories

    })


class ProductAddView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = ["manager", 'admin']
    model = Product
    form_class = ProductForm
    template_name = 'product_add.html'
    success_url = reverse_lazy('list_of_products')
    success_message = 'Product has been successfully created!'


class ProductDeleteView(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = ["manager", 'admin']
    model = Product
    success_url = reverse_lazy('list_of_products')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Product has been deleted successfully!')
        return self.post(request, *args, **kwargs)


class ProductUpdateView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = ["manager", 'admin']
    model = Product
    form_class = ProductForm
    template_name = 'product_update.html'
    success_url = reverse_lazy('list_of_products')
    success_message = 'Product has been changed successfully!'


@login_required(login_url='/login/')
@user_passes_test(is_member)
def list_of_categories(request):
    address = Address.objects.filter(is_visible=True)
    phone = Phone.objects.filter(is_visible=True)
    email = Email.objects.filter(is_visible=True)
    aboutus = AboutUs.objects.all()
    category = Category.objects.all
    return render(request, 'categories.html', context={

        'address': address[0],
        'phone': phone[0],
        'email': email[0],
        'aboutus': aboutus[0],
        'category': category

    })


class CategoryAddView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = ["manager", 'admin']
    model = Category
    form_class = CategoryForm
    template_name = 'category_add.html'
    success_url = reverse_lazy('list_of_categories')
    success_message = 'Category has been successfully created!'


class CategoryDeleteView(DeleteView, LoginRequiredMixin, GroupRequiredMixin):
    login_url = reverse_lazy('login')
    group_required = ["manager", 'admin']
    model = Category
    success_url = reverse_lazy('list_of_categories')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Category was deleted successfully!')
        return self.post(request, *args, **kwargs)


class CategoryUpdateView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = ["manager", 'admin']
    model = Category
    form_class = CategoryForm
    template_name = 'category_update.html'
    success_url = reverse_lazy('list_of_categories')
    success_message = 'Category changed successfully!'


@login_required(login_url='/login/')
@user_passes_test(is_member)
def list_of_orders(request):
    order = Order.objects.all()
    for item in order:
        item.Orderitem = OrderItem.objects.filter(order=item.pk)
    context = {'orders': order}
    return render(request, 'orders.html', context)





