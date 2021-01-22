from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the blog </h1>")

def about(request):
    return HttpResponse("<h1>Welcome to the about section of the blog </h1>")

