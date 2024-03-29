from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from colorfield.fields import ColorField
from django.contrib.auth.models import User
from apps.base.models import BaseModel
from django.utils.safestring import mark_safe
from django.db.models import Avg
from django.template.defaultfilters import slugify  # new


class Category(BaseModel, MPTTModel):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='icons/', null=True, blank=True)  # icon ka qoyiladi
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"


class Brand(BaseModel):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='brands/')

    def __str__(self):
        return f"{self.name}"


class Color(BaseModel):
    COLOR_PALETTE = [
        ("#ff0000", "qizil",),
        ("#ffa500", "jigar rang",),
        ("#ffff00", "sariq",),
        ("#008000", "yashil",),
        ("#0000ff", "ko'k",),
        ("#4b0082", "binafsha",),
        ("#ee82ee", "pushti",),
        ("#000000", "qora",),
    ]
    name = models.CharField(max_length=50)
    color = ColorField(samples=COLOR_PALETTE)

    def __str__(self):
        return f"{self.name}"


class Tag(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Size(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Product(BaseModel):
    STATUS = (
        ('None', 'None'),
        ('HOT', 'HOT'),
        ('NEW', 'NEW'),
        ('SALE', 'SALE'),
    )
    name = models.CharField(max_length=250)
    slug = models.SlugField(null=True, blank=True, unique=True, max_length=250)
    status = models.CharField(choices=STATUS, max_length=250,
                              default='HOT')  # bunda uchta narsani tanlidi adashmasam yani new old top shular
    categories = models.ManyToManyField(Category, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)  # foreign
    description = models.TextField(null=True, blank=True)
    percentage = models.FloatField(null=True, blank=True, default=0)
    price = models.FloatField(default=0)
    views = models.IntegerField(default=1)
    availability = models.IntegerField(default=0)
    colors = models.ManyToManyField(Color, blank=True)  # foreign
    sizes = models.ManyToManyField(Size, blank=True)  # foreign
    has_size = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)  # foreign
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    @property
    def rate_percentage(self):
        rates = self.product_rates.all().aggregate(avarage=Avg("rate"))
        if rates['avarage']:
            return rates['avarage'] * 100 / 5
        return 0
    
    @property
    def rate_avg(self):
        rates = self.product_rates.all().aggregate(avarage=Avg("rate"))
        if rates['avarage']:
            return rates['avarage']
        return 0

    @property
    def get_new_price(self):
        if self.percentage == 0 or self.percentage is None:
            return self.price
        return self.price - (self.price * self.percentage / 100)
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})
    


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products')  # rasm yukliman
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product.name}"

    @property
    def get_image(self):
        if not self.image.url:
            return "No Image"
        return mark_safe('<img src="{}" height="100"/>'.format(self.image.url))


class AdditionalInfo(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='additional_info')
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.product.name}"


class Rate(BaseModel):
    RATING = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_rates')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, related_name='product_rates')
    rate = models.IntegerField(choices=RATING, default=0)
    comment = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.comment}"
