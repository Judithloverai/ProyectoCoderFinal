from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Esto es un primer inento")