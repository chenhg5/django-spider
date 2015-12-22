#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse(u"Welcome")

def add(request):
	c = int(request.GET['a'])+int(request.GET['b'])
	return HttpResponse(str(c))

def index(request):
    return render(request, 'home.html')