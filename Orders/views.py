import json

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationform
from .models import Customers, Category, Product, Cart
from django.http import JsonResponse

# Create your views here.


global i
i = 0


def Home(request):
    if 'search' in request.GET:
        search = request.GET['search']
        product = Product.objects.filter(name=search)
        print(product.selling_price)
    category = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'Orders/Home.html', {
        'data': category,
        'item': products
    })


def Register(request):
    if request.method == 'POST':
        form = UserRegistrationform(request.POST)

        if form.is_valid():
            username = request.POST['username']
            email = request.POST['email']
            address = request.POST['address']
            city = request.POST['city']
            zipcode = request.POST['zipcode']
            password = request.POST['password1']

            C1 = Customers(name=username, email=email, address=address, city=city, zipcode=zipcode, password=password)

            C1.save()
            return redirect('index')
    else:

        form = UserRegistrationform()

    return render(request, 'Orders/Register.html', {
        'form': form
    })


def Login(request):
    invalid = ""
    if request.POST:
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username=username, password=pwd)
        if user:
            login(request, user)

            return redirect('index')
        else:
            invalid = "Username and/or Password is/are Invalid"

    return render(request, 'Orders/Login.html', {
        'message': invalid
    })


def Logout(request):
    logout(request)
    return redirect('index')


def Indian(request):
    content = Category.objects.all()
    products = Product.objects.filter(cat='Indian')

    return render(request, 'Orders/Indian.html', {
        'data': content,
        'products': products

    })


def Chinese(request):
    content = Category.objects.all()
    products = Product.objects.filter(cat='Chinese')

    return render(request, 'Orders/Chinese.html', {
        'data': content,
        'products': products
    })


def Italian(request):
    content = Category.objects.all()

    products = Product.objects.filter(cat='Italian')
    return render(request, 'Orders/Italian.html', {
        'data': content,
        'products': products
    })


def FastFood(request):
    content = Category.objects.all()
    products = Product.objects.filter(cat='FastFood')

    return render(request, 'Orders/FastFood.html', {
        'data': content,
        'products': products
    })


def Tea(request):
    content = Category.objects.all()
    products = Product.objects.filter(cat='Tea')

    return render(request, 'Orders/Tea.html', {
        'data': content,
        'products': products
    })


def Dessert(request):
    content = Category.objects.all()
    products = Product.objects.filter(cat='Desserts')

    return render(request, 'Orders/Desserts.html', {
        'products': products,
        'data': content
    })


def update_item(request):
    data = json.loads(request.body)
    productID = data['productID']

    # Getting The Product Details
    productID_information = Product.objects.get(id=productID)
    bill = productID_information.selling_price * 1
    print(bill)
    adding_customer = Cart(login_name=request.user, product_name=productID_information.name,
                           product_image=productID_information.product_image,
                           product_price=productID_information.selling_price, Total=bill).save()

    return JsonResponse("Item Added", safe=False)


def Incre(request):
    data = json.loads(request.body)
    product_name = data['productID']
    action = data['action']

    get_cart = Cart.objects.get(product_name=product_name)
    if action == 'add':
        get_cart.product_quantity = (get_cart.product_quantity + 1)
        print(get_cart.product_quantity)
        get_cart.Total = (get_cart.product_quantity * get_cart.product_price)
        get_cart.save()
    elif action == 'Remove' and get_cart.product_quantity > 1:
        get_cart.product_quantity = (get_cart.product_quantity - 1)
        print(get_cart.product_quantity)
        get_cart.Total = (get_cart.product_quantity * get_cart.product_price)
        get_cart.save()
    elif action == 'Delete':
        print("Done")
        get_cart.delete()
    return JsonResponse("Item was Added", safe=False)


def ShowCart(request):
    product = Cart.objects.all()
    sum = 0
    for i in Cart.objects.all():
        sum += i.Total
    return render(request, 'Orders/Cart.html', {
        'item': product,
        'bill': sum
    })


def Checkout(request):
    sum=0
    for i in Cart.objects.all():
        sum+=i.Total
    return render(request,'Orders/Checkout.html',{
        'bill':sum
    })