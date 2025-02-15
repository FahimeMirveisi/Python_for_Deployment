from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def product(request, product_id: int):
    return render(request, 'product.html')
