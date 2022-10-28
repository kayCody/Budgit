from django.shortcuts import render
from .models import Addproducts
from stores.models import Melcom
# import requests
# from bs4 import BeautifulSoup

# url = "https://frankotrading.com/?s=samsung&post_type=product"
# link = requests.get(url)

# soup = BeautifulSoup(link.content, 'html.parser')
# lists = soup.find_all('div', class_="type-product")
# with open('text.txt', 'a') as files:
#     for list in lists:
#         title = list.find('h3', class_="product-title").text
#         #productLabel = list.find('span', class_="new")
#         #image = list.find('img', class_="attachment-woocommerce_thumbnail size-woocommerce_thumbnail front-image")
#         price = list.find('bdi').text
        
#         info = [title, price]
#         print(title, price)
#         files.write(info[0][1])
       
            
    # Create your views here.
def home(request):
    # products = Melcom()
    # products.productName = title
    # products.productPrice = price
    # products.save()
    return render(request, 'home.html')
    
    
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