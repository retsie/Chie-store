from django.contrib.auth.models import User
from django.db import models

from accounts.models import Account
from store.models import Product, Variation


class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation = models.ManyToManyField(Variation, blank=True) # will create new table with cart_item_id and variation_id
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)

    def subtotal(self):
        return self.product.price * self.quantity

    def __unicode__(self):
        return self.product



