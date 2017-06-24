from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Slider,School_Services, Company_Services, IT_Services
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.


def search(request, user):
    categories = Category.objects.all()
    query = request.GET['q']
    if query:
        products = Product.objects.filter(name__icontains=query) |  Product.objects.filter(company__icontains=query) | Product.objects.filter(short_description__icontains=query)  | Product.objects.filter(type__name__icontains=query)
        return render(request, 'szukaj.html', {'products': products, 'categories': categories})
    else:
        sliders = Slider.objects.all()
        return render(request, 'index.html', {'categories': categories, 'sliders': sliders})


def main_page(request):
    categories = Category.objects.all()
    sliders = Slider.objects.all()
    return render(request, 'index.html', {'categories': categories, 'sliders': sliders})

def get_product(request, name):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True, category__name=name).order_by('type','company', 'name')
    return render(request, 'produkty.html', {'products': products, 'categories': categories})

def product_detail(request, name):
    categories = Category.objects.all()
    product = get_object_or_404(Product, name=name)
    # product = Product.objects.get(name=name)
    return render(request, 'product_detail.html', {'product': product, 'categories': categories})

def szkoly(request):
    categories = Category.objects.all()
    school_services = School_Services.objects.all()
    return render(request, 'szkoly.html', {'categories': categories, 'school_services': school_services})

def firmy(request):
    categories = Category.objects.all()
    company_services = Company_Services.objects.all()
    return render(request, 'firmy.html', {'categories': categories, 'company_services': company_services})

def uslugi(request):
    categories = Category.objects.all()
    it_services = IT_Services.objects.all()
    return render(request, 'uslugi_informatyczne.html', {'categories': categories, 'it_services': it_services})

def kontakt(request):
    categories = Category.objects.all()
    return render(request, 'kontakt.html', {'categories': categories})