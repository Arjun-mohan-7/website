from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')
def about_us(request):
    return render(request, 'about.html')
def sign_in(request):
    return render(request, 'signin.html')
def sign_up(request):
    return render(request, 'signup.html')
def contact_us(request):
    return render(request, 'contact.html')
