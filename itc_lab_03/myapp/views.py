from django.shortcuts import render

# Create your views here.
<<<<<<< HEAD
def home(request):
    return render(request, 'index.html')  # hoặc tên template chính của bạn

# Có thể thêm các view khác sau
def about(request):
    return render(request, 'about.html')

def shop(request):
    return render(request, 'shop.html')  # hoặc tên template chính của bạn

# Có thể thêm các view khác sau
def contact(request):
    return render(request, 'contact.html')
=======
def index(request):
    return render(request, 'myapp/index.html')
def about(request):
    return render(request, 'myapp/about.html')
def contact(request):
    return render(request, 'myapp/contact.html')
def shop(request):
    return render(request, 'myapp/shop.html')
def shopSingle(request):
    return render(request, 'myapp/shop_single.html')
>>>>>>> e139c0d27c8a1c77d5f0abf76877e21ae1a2af65
