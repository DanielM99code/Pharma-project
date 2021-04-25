from django.contrib import admin
from .models import *

admin.site.register(SpecOfferBlue)
admin.site.register(SpecOfferGreen)
admin.site.register(SpecOfferYellow)
admin.site.register(Testimonials)
admin.site.register(Rate)
admin.site.register(Email)
admin.site.register(Address)
admin.site.register(Phone)
admin.site.register(AboutUs)
admin.site.register(History)
admin.site.register(OurOffer)
admin.site.register(OurTeam)
admin.site.register(Message)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price']
    list_filter = ['is_new', 'is_popular']
    list_editable = ['price']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_order', 'is_visible']
    list_filter = ['is_visible']


@admin.register(Welcome)
class WelcomeAdmin(admin.ModelAdmin):
    list_display = ['title', 'desc']








