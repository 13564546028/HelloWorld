from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def t1(request):
    return render(request,'t1.html')

def t2(request):
    return render(request,'t2.html')