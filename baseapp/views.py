from django.shortcuts import render
from django.http import HttpResponse


def resp(request):
    return HttpResponse('раздва')
