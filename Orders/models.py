from django.db import models


# Create your models here.
class Customers(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, default=" ")
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    password = models.CharField(max_length=200, default=" ")

    def __str__(self):
        return self.name


class Category(models.Model):
    cat = models.CharField(max_length=200)
    pro_image = models.ImageField(upload_to='Images/Categories')


class Product(models.Model):
    name = models.CharField(max_length=200)
    cat = models.CharField(max_length=100, default="")
    product_image = models.ImageField(upload_to='Images/Products')
    selling_price = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name


class Cart(models.Model):
    login_name = models.CharField(max_length=200,default="")
    product_name = models.CharField(max_length=200,default="")
    product_image = models.ImageField(upload_to='media')
    product_price = models.PositiveIntegerField(default=1)
    product_quantity = models.IntegerField(default=1)
    Total = models.IntegerField(default=0)
