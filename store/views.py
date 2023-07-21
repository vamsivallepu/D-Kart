from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from django.http import HttpResponse

# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None
    
    if category_slug :
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    context = {
        'products': products,
        'number_of_products': product_count,
    } 

    return render(request, 'store/store.html', context)

def product_detail(request, category_slug=None, product_slug=None):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except:
        return HttpResponse("Product not found")
    context = {
        'product': single_product,
    }
    return render(request, 'store/product_details.html', context)
