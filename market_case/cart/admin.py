from django.contrib import admin

from cart.models import Cart, CartItem


# Register your models here.

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    fields = ['user']
    list_display = ['user']


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    fields = ['product', 'quantity', 'cart']
    list_display = ['product', 'quantity', 'cart']
