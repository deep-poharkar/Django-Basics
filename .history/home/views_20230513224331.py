from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("This is homepage")

def about(request):
    return HttpResponse("This is about page")

def contact(request):
    return HttpResponse("This is contact page")
