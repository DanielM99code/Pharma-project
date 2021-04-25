from django import forms
from main_pharma.models import *


class CategoryForm(forms.ModelForm):
    title = forms.CharField(max_length=15,
                            widget=forms.TextInput(attrs={'placeholder': "Category name", 'required': "required"}))
    category_order = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': "Order in category", 'required': "required"}))
    is_visible = forms.BooleanField(initial=True, required=False)

    class Meta:
        model = Category
        fields = ('title', 'category_order', 'is_visible')


class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=25,
                           widget=forms.TextInput(attrs={'placeholder': "Name", 'required': "required"}))
    price = forms.DecimalField(max_digits=6, decimal_places=2,
                               widget=forms.TextInput(attrs={'placeholder': "Product price", 'required': "required"}))
    slug = forms.CharField(max_length=25,
                           widget=forms.TextInput(attrs={'placeholder': "Slug", 'required': "required"}))
    image_full = forms.ImageField(widget=forms.FileInput())
    image_small = forms.ImageField(widget=forms.FileInput())
    material = forms.CharField(max_length=150,
                               widget=forms.TextInput(attrs={'placeholder': "Material", 'required': "required"}))
    description = forms.CharField(max_length=150,
                                  widget=forms.TextInput(attrs={'placeholder': "Description", 'required': "required"}))
    packaging = forms.CharField(max_length=25,
                                widget=forms.TextInput(attrs={'placeholder': "Packaging", 'required': "required"}))
    hpis_code = forms.CharField(max_length=25,
                                widget=forms.TextInput(attrs={'placeholder': "HPIS Code", 'required': "required"}))
    hc_provider = forms.BooleanField(required=False)
    latex_free = forms.BooleanField(required=False)
    med_route = forms.CharField(max_length=25,
                                widget=forms.TextInput(attrs={'placeholder': "Medication Route", 'required': "required"}
                                                       ))
    is_visible = forms.BooleanField(required=False)
    shop_order = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': "Product order in shop", 'required': "required"}))
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    is_popular = forms.BooleanField(required=False)
    is_new = forms.BooleanField(required=False)

    class Meta:
        model = Product
        fields = ('name', 'price', 'slug', 'image_full', 'image_small', 'material', 'description', 'packaging',
                  'hpis_code', 'hc_provider', 'latex_free', 'med_route', 'is_visible', 'shop_order', 'category',
                  'is_popular', 'is_new')
