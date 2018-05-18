# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import PiForm
from home.findnth import *

# Create your views here.
def home(request):
    return render(request, 'home/homepage.html') 

def pi_tool(request):
    # as of now, we're only dealing with get requests
    if (request.method == 'GET' and 'get_k' in request.GET) :
        k = int(request.GET['get_k'])
        pi = u"\u03C0" + ": " + getPi(k)
        return render(request, 'home/findnth/pi-tool.html', {'pi': pi}) 

    return render(request, 'home/findnth/pi-tool.html') 
