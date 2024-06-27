from django.shortcuts import render
from products.models import Products
from carousel.models import Carousel

def home(request):
    productData=Products.objects.all()
    Carousel2=Carousel.objects.all()
    print(productData)
    data = {
        "products":productData,
        "carousel":Carousel2
    }
    return render(request, 'index.html', data)
