# from curses.ascii import HT
from math import prod
import re
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.db.models import Sum
from .models import *
from .forms import ProductForm, CustomerForm, ServiceForm
from django.contrib.auth.models import auth
from django.contrib import messages
# login, logout
from django.contrib.auth.decorators import login_required


# from rest_framework import authentication
def loginPage(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    #
    #     if request.method == 'POST':
    #         username = request.POST.get('username')
    #         password = request.POST.get('password')
    #         user = auth.authenticate(request, username=username, password=password)
    #         if user:
    #             auth.login(request, user)
    #             return redirect('home')
    #     else:
    #         context = {}
    #         return render(request, 'accounts/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Wrong password")
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def logOut(request):
    auth.logout(request)
    return render(request, 'accounts/login.html')


# @login_required(login_url='login')
def home(request):
    return render(request, 'accounts/home.html')


# @login_required(login_url='login')
def products(request):
    product = Product.objects.all()
    return render(request, 'accounts/products_list.html', {'product': product})


# @login_required(login_url='login')
def customer(request):
    customer = Customer.objects.all()
    return render(request, 'accounts/customer_list.html', {'customer': customer})


# @login_required(login_url='login')
def single_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    product = Product.order_set.all()
    service = Service.order_set.all()
    context = {'customer': customer, "products": product, "service": service}
    print(context)
    return render(request, 'accounts/customer_list.html', context)


def service(request):
    service = Service.objects.all()
    return render(request, 'accounts/service_list.html', {'service': service})


def create_customer(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/customer')
    else:
        print("error occurresd")
    context = {'form': form}
    return render(request, 'accounts/create_customer.html', context)


def create_service(request):
    form = ServiceForm()
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/service')
    else:
        print("error occurresd")
    context = {'form': form}
    return render(request, 'accounts/create_service.html', context)


def create_product(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/product')
    else:
        print("error occurresd")
    context = {'form': form}
    return render(request, 'accounts/create_product.html', context)


def update_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/customer')
    else:
        print("error occurresd")
    context = {'form': form}
    return render(request, 'accounts/create_customer.html', context)


def update_service(request, pk):
    service = Service.objects.get(id=pk)
    form = ServiceForm(instance=service)
    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('/service')
    else:
        print("error occurresd")
    context = {'form': form}
    return render(request, 'accounts/create_service.html', context)


def update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/product')
    else:
        print("error occurresd")
    context = {'form': form}
    return render(request, 'accounts/create_product.html', context)


def delete_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == "POST":
        customer.delete()
        return redirect('/customer')
    context = {'item': customer}
    return render(request, 'accounts/delete_customer.html', context)


def delete_service(request, pk):
    service = Service.objects.get(id=pk)
    if request.method == "POST":
        service.delete()
        return redirect('/service')
    context = {'item': service}
    return render(request, 'accounts/delete_service.html', context)


def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        return redirect('/product')
    context = {'item': product}
    return render(request, 'accounts/delete_product.html', context)


def summary(request, pk):
    # customer = get_object_or_404(Customer, pk=pk)
    customer = Customer.objects.get(id=pk)
    services = Service.objects.filter(cust_name=pk)
    products = Product.objects.filter(cust_name=pk)
    sum_service_charge = \
        Service.objects.filter(cust_name=pk).aggregate(Sum('service_charge'))
    sum_product_charge = \
        Product.objects.filter(cust_name=pk).aggregate(Sum('charge'))

    # if no product or service records exist for the customer,
    # change the ‘None’ returned by the query to 0.00
    total = 0
    sum = sum_product_charge.get("charge__sum")
    if sum:
        total += int(sum)

    if sum == None:
        sum_product_charge = {'charge__sum': '0'}
    sum = sum_service_charge.get("service_charge__sum")
    if sum:
        total += int(sum)

    if sum == None:
        sum_service_charge = {'service_charge__sum': '0'}

    print(total)
    # total_expenditure ={tota}
    total_expenditure = {'total_expenditure': total}
    return render(request, 'accounts/summary.html',
                  {'customer': customer,
                   'products': products,
                   'services': services,
                   'sum_service_charge': sum_service_charge,
                   'sum_product_charge': sum_product_charge,
                   'total_expenditure': total_expenditure})
