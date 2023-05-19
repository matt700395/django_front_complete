from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'coupang_login_app/index.html')

def login(request):
    return render(request, 'coupang_login_app/login.html')