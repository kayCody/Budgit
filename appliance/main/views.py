from django.shortcuts import render
from .models import Addproducts
from stores.models import Melcom

# Create your views here.
def home(request):    
    products = Addproducts.objects.all()
    prod = Melcom.objects.all()
    context = {
        'products':products, 
        'prod':prod
    }
    return render(request, 'home.html', context)
def about(request):
    return render(request, 'pages/about_us.html')

def cart(request, acart):
    products = Addproducts.objects.get(Productsid = acart)
    context = {
        'products':products
    }
    return render(request, 'pages/cart.html', context)
def contact(request):
    return render(request, 'pages/contact_us.html')
def success(request):
    return render(request, 'pages/successful.html')

def search(request):
    if request.method =='POST':
        search = request.POST['search']
        prod = Melcom.objects.filter(productName__contains = search)
        return render(request, 'pages/results.html', {'search':search, 'prod':prod})
    else:
        return render(request, 'pages/results.html', {})    