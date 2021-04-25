from django.db import models
from django_resized import ResizedImageField
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=20, unique=True)
    category_order = models.IntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}:{self.category_order}'


class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=200, db_index=True)
    image_full = models.ImageField(upload_to='products/full/%Y/%m/%d', blank=True)
    image_small = ResizedImageField(size=[270, 370], upload_to='products/small/%Y/%m/%d', blank=True)
    material = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    packaging = models.CharField(max_length=10)
    hpis_code = models.CharField(max_length=20)
    hc_provider = models.BooleanField()
    latex_free = models.BooleanField()
    med_route = models.CharField(max_length=20)
    is_visible = models.BooleanField(default=True)
    shop_order = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_popular = models.BooleanField()
    is_new = models.BooleanField()

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return f'{self.name}, ${self.price}, {self.category}'


class Welcome(models.Model):
    title = models.CharField(max_length=30, unique=True)
    photo = models.ImageField(upload_to='welcome/%Y/%m/%d')
    desc = models.CharField(max_length=200, unique=True, default='SOME STRING')

    def __str__(self):
        return f'{self.title}'


class SpecOfferBlue(models.Model):
    title = models.CharField(max_length=15, unique=True)
    desc = models.CharField(max_length=200, unique=True, default='SOME STRING')

    def __str__(self):
        return f'{self.title}'


class SpecOfferGreen(models.Model):
    title = models.CharField(max_length=15, unique=True)
    desc = models.CharField(max_length=200, unique=True, default='SOME STRING')

    def __str__(self):
        return f'{self.title}'


class SpecOfferYellow(models.Model):
    title = models.CharField(max_length=15, unique=True)
    desc = models.CharField(max_length=200, unique=True, default='SOME STRING')

    def __str__(self):
        return f'{self.title}'


class Testimonials(models.Model):
    name = models.CharField(max_length=20, unique=True)
    quote = models.CharField(max_length=200, unique=True, default='SOME STRING')
    image = models.ImageField(upload_to='testimonials/%Y/%m/%d', blank=True)

    def __str__(self):
        return f'{self.name}'


class Rate(models.Model):
    title = models.CharField(max_length=15, unique=True)
    photo = models.ImageField(upload_to='rate/%Y/%m/%d')
    desc = models.CharField(max_length=200, unique=True, default='SOME STRING')

    def __str__(self):
        return f'{self.title}'


class Address(models.Model):
    address = models.CharField(max_length=100, blank=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.address}'


class Phone(models.Model):
    phone = models.CharField(max_length=13, unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.phone}'


class Email(models.Model):
    email = models.EmailField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.email}'


class AboutUs(models.Model):
    title = models.CharField(max_length=15, blank=True)
    desc = models.CharField(max_length=200, unique=True, default='SOME STRING')

    def __str__(self):
        return f'{self.title}'


class History(models.Model):
    title = models.CharField(max_length=30, unique=True)
    photo = models.ImageField(upload_to='history/%Y/%m/%d')
    desc = models.TextField(blank=True)

    def __str__(self):
        return f'{self.title}'


class OurOffer(models.Model):
    title = models.CharField(max_length=15, unique=True)
    desc = models.TextField(blank=True)

    def __str__(self):
        return f'{self.title}'


class OurTeam(models.Model):
    name = models.CharField(max_length=20, unique=True)
    position = models.CharField(max_length=20)
    desc = models.CharField(max_length=200, unique=True, default='SOME STRING')
    image = models.ImageField(upload_to='team/%Y/%m/%d', blank=True)

    def __str__(self):
        return f'{self.name}, {self.position}'


class Message(models.Model):
    user_fname = models.CharField(max_length=40, blank=True)
    user_lname = models.CharField(max_length=40, blank=True)
    user_email = models.EmailField(blank=True)
    user_subject = models.CharField(max_length=40, blank=True)
    user_message = models.TextField(blank=True)

    pub_date = models.DateField(auto_now_add=True, blank=True)
    is_processed = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f'{self.user_fname} : {self.user_lname} {self.user_email} : {self.user_message[:20]}'
