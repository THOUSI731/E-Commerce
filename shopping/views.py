from products.models import Product 
from category.models import Category
from django.shortcuts import render

# Create Your Views Here

def homePage(request):
    products = Product.objects.all().filter(is_available=True)
    categories = Category.objects.get(slug='games')
    context = {
        'products':products,
        'categories' : categories
    }
    return render(request, "home.html",context)