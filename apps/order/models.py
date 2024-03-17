from django.db import models
from django.contrib.auth.models import User
from apps.base.models import BaseModel
from apps.product.models import Product


class WishList(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_wishlists')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlists')

    def __str__(self):
        return f"{self.user} - {self.product}"
    
class ShopCart(BaseModel):
    is_complated = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_carts')

    def __str__(self):
        return f"{self.user} - {self.is_complated}"


    def add_to_cart(self, product, quantity, result, color, size):
        cart_item = OrderItem.objects.create(
            cart=self, 
            size=size,
            color=color, 
            price=result, 
            product=product,
            quantity=quantity
        )
        return cart_item



class Order(BaseModel):
    STATUS = (
        ('PENDING', 'PENDING'),
        ('COMPLETED', 'COMPLETED'),
        ('CANCELED', 'CANCELED'),
    )
    status = models.CharField(max_length=50, choices=STATUS, default='PENDING')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_orders')
    phone_number = models.CharField(max_length=50)
    


class OrderItem(BaseModel):
    cart = models.ForeignKey(ShopCart, on_delete=models.CASCADE, related_name='cart_items')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    color = models.CharField(max_length=50, null=True, blank=True)
    size = models.CharField(max_length=50, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.cart} - {self.product} - {self.quantity}"
