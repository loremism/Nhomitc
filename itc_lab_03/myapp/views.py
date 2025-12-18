from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'myapp/index.html')  # hoặc tên template chính của bạn
# Có thể thêm các view khác sau
def about(request):
    return render(request, 'myapp/about.html')
def shop(request):
    return render(request, 'smyapp/hop.html')  # hoặc tên template chính của bạn
# Có thể thêm các view khác sau
def contact(request):
    return render(request, 'myapp/contact.html')
def index(request):
    return render(request, 'myapp/index.html')
def about(request):
    return render(request, 'myapp/about.html')
def contact(request):
    return render(request, 'myapp/contact.html')
def shop(request):
    return render(request, 'myapp/shop.html')
def shop_single(request):
    return render(request, 'myapp/shop_single.html')

