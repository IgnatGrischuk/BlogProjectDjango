from django.shortcuts import render
from django.http import HttpResponse


def some_view(request):
    return HttpResponse('<h1>Hello Olga, are we going to play The Witcher '
                        'today??)))<h1>')
