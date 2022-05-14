from django.contrib import admin

from .models import Customers, Category, Product, Cart


# Register your models here.

class Cutomeradmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'zipcode', 'password')


admin.site.register(Customers, Cutomeradmin)


class Categoryadmin(admin.ModelAdmin):
    list_display = ('cat', 'pro_image')


admin.site.register(Category, Categoryadmin)


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cat', 'product_image', 'selling_price')


admin.site.register(Product, ProductModelAdmin)


class CartModelAdmin(admin.ModelAdmin):
    list_display = ('login_name', 'product_name', 'product_image', 'product_price', 'product_quantity','Total')


admin.site.register(Cart, CartModelAdmin)
