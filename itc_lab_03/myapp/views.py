from django.shortcuts import render

# Create your views here.
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