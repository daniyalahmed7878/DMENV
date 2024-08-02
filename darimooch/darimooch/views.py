from django.shortcuts import render , redirect
from products.models import Products
from carousel.models import Carousel
from contact.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login as user_login ,logout

def home(request):
    productData=Products.objects.all()
    Carousel2=Carousel.objects.all()
    print(productData)
    data = {
        "products":productData,
        "carousel":Carousel2
    }
    return render(request, 'index.html', data)
def contactPage(request):
    #  try:
          
    #     name=request.GET.get('fullname')
    #     email=request.GET.get('email')
    #     phone=request.GET.get('phone') 
    #     message=request.GET.get('message')
        
    #     if name == '' or email == '' or phone == '' or message == '' :
           
    #         return render(request, 'contact.html')
        
    #     contact=Contact(fullname=name, email=email, phone=phone, message=message)
    #     contact.save()
    #  except:
    #     print('error')  
     return render(request, 'contact.html')

def saveContact(request):
     try:
          
        name=request.POST.get('fullname')
        email=request.POST.get('email')
        phone=request.POST.get('phone') 
        message=request.POST.get('message')
        if name == '' or email == '' or phone == '' or message == '' :
            return render(request, 'contact.html')
        contact=Contact(fullname=name, email=email, phone=phone, message=message)
        contact.save()
     except:
        print('error') 
     return render(request, 'contact.html')
def productDetail(request, id):
    print(id)
    product=Products.objects.get(id__exact=id)
    data={
        'product': product
    }
    return render(request, 'product.html',data)

def search(request):
    SearchTerm= request.GET['search']
    products=Products.objects.filter(title__icontains=SearchTerm)
    data={
        'products': products
    }
    return render(request, 'search.html', data)
def register(request):
    return render(request, 'register.html')
def login(request):
    return render(request, 'login.html')


def registerUser(request):
    uname = request.POST.get('username')
    uemail = request.POST.get('email')
    upassword = request.POST.get('password')
    
    user = User.objects.create_user(username=uname, email=uemail, password=upassword)

    return render(request, 'register.html')




def loginUser(request):
    
    uname = request.POST['username']
    upassword = request.POST['password']
    user = authenticate(request, username=uname, password=upassword)
  
    if user is not None:
         user_login(request, user)
         request.session['username'] = user.username
         request.session['email'] = user.email
         return redirect('/')
    else:
        print('user does not exit')
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)

    return render(request, 'login.html')