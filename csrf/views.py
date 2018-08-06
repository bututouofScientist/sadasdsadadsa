from django.shortcuts import render
from django.views.generic.list import ListView


def index(request):
    return render(request, 'csrf.html')


def index1(request):
    return render(request, 'csrf2.html.')


def index2(request):
    return render(request, 'csrf2.html.html')