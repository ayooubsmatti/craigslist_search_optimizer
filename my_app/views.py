from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'base.html')

def new_search(request):
    return render(request,'my_app/new_search.html')
