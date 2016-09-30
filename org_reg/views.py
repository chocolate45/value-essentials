from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home_page(request):
    return render(request, 'home.html')
