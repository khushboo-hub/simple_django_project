from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def printresult(request):
    return HttpResponse("Hello World")