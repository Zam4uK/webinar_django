from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    text = "Контент из вью"
    return render(request, 'index.html', locals())
