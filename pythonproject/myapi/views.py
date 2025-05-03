from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def sec(request):
    return render(request,'website/all_index.html')