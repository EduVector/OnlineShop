from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from colorfield.fields import ColorField
from django.contrib.auth.models import User
from apps.base.models import BaseModel


class Category(BaseModel, MPTTModel):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='icons/', null=True, blank=True)  # icon ka qoyiladi
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"


class Brand(BaseModel):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"


class Color(BaseModel):
    COLOR_PALETTE = [
        ("#ff0000", "qizil"),
        ("#FFFEFA", "oq"),
        ("#ffff00", "sariq"),
        ("#008000", "yashil"),
        ("#0000ff", "ko'k"),
        ("#4b0082", "binafsha"),
        ("#ee82ee", "pushti"),
        ("#000000", "qora"),

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
        ('OLD', 'OLD'),
        ('TOP', 'TOP'),
        ('SALE', 'SALE'),
        ('DISCOUNT', 'DISCOUNT'),
    )
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    status = models.CharField(choices=STATUS, max_length=250,
                              default='HOT')  # bunda uchta narsani tanlidi adashmasam yani new old top shular
    categories = models.ManyToManyField(Category, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)  # foreign
    description = models.TextField(null=True, blank=True)
    percentage = models.FloatField(null=True, blank=True)
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


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=None)  # rasm yukliman
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product.name}"


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
