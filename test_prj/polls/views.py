#coding=utf-8

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("hello, world. Yor're at the polls index."
                        "<p>嗨，我在这里</p>")


# Create your views here.
