# myapp/views.py
from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    # return HttpResponse("Hello World")
    return render(request,'base.html')

def name(request):
    return HttpResponse('My Name is ...')