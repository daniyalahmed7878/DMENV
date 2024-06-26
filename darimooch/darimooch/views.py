from django.shortcuts import render
from products.models import Products
from carousel.models import Carousel
def home(request):
    productData=Products.objects.all()
    carousel2=Carousel.objects.all()
    print(productData)
    data = {
        "products":productData,
        "carousel":carousel2
    }
    return render(request, 'index.html', data)
