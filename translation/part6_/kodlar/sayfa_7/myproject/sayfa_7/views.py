from django.shortcuts import render
from .models import Product

def product_search(request):
    query = request.GET.get('query', '')
    if query:
        products = Product.objects.filter(name__icontains=query)  # Assuming a Product model is defined
        return render(request, 'product_search.html', {'products': products})
    else:
        return render(request, 'product_search.html')


def home(request):
    return render(request, 'home.html')  # 'home.html' şablonunu render ediyoruz

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # index.html şablonunu döndür




#terminale sırasıyla
#cd C:\Users\hamza\OneDrive\Masaüstü\sayfa_6\myproject(cd myproject)
#python manage.py runserver
