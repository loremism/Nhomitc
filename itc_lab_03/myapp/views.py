from django.shortcuts import render
from .models import Products,Category
# Create your views here
def home(request):
    products = Products.objects.all()[:3]
    return render(request, 'myapp/index.html', {
        'products': products
    })
def contact(request):
    return render(request, 'myapp/contact.html')
def about(request):
    return render(request, 'myapp/about.html')
def contact(request):
    return render(request, 'myapp/contact.html')
def shop(request):
    products = Products.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'myapp/shop.html', context)
def shop_detail(request):
    return render(request, 'myapp/shop_detail.html')

