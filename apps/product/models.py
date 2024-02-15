from django.db import models

class Category(models.Model):
    type_categories = models.CharField(max_length=50)
    icon =  models.FileField(upload_to=None ) # icon ka qoyiladi
    parent = models.IntegerField()
    
class ProductImage(models.Model):
    image = models.ImageField(upload_to=None ) # rasm yukliman
    is_active = models.BooleanField()
    
class Brand(models.Model):
    name = models.CharField(max_length=250)
    
class AdditionalInfo(models.Model):
    key = models.CharField(max_length=50)
    value = models.CharField( max_length=50)

class Color(models.Model):
    name = models.CharField( max_length=50)
    code = models.CharField( max_length=50)

class Tag(models.Model):
    name = models.CharField( max_length=50)
    
class Size(models.Model):
    name = models.CharField(max_length=50)
    
class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    messege = models.TextField()
    
class User(models.Model):
    name = models.CharField(max_length=50)
    
class Branch(models.Model):
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    location = models.URLField(max_length=200)
            
class Product(models.Model):
    STATUS = (
        ('HOT', 'hot'),
        ('NEW', 'new'),
        ('OLD', 'old'),
        ('TOP', 'top'),
        ('SALE', 'sale'),
        ('DISCOUNT', 'discount'),
    )
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    status = models.CharField(choices=STATUS,max_length=250, default='HOT') # bunda uchta narsani tanlidi adashmasam yani new old top shular
    category = models.ManyToManyField(Category)
    brand = models.ForeignKey( Brand , on_delete=models.CASCADE) # foreign
    discription = models.TextField()
    percentage = models.FloatField(null = True  , blank = True)
    price = models.FloatField()
    views = models.IntegerField(default=1)
    availability = models.IntegerField()
    color = models.ForeignKey(Color , on_delete=models.CASCADE)# foreign
    sizes = models.ManyToManyField(Size) # foreign
    has_size = models.BooleanField()
    tags = models.ManyToManyField(Tag) # foreign
    is_active = models.BooleanField()  
    
class Rate(models.Model):
    RATING = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey( Product, on_delete=models.CASCADE)
    rate = models.IntegerField(choices=RATING , default=0)
    comment = models.CharField(max_length=50)