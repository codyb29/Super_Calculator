# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import PiForm

# Create your views here.
def home(request):
    return render(request, 'home/homepage.html') 

def pi_tool(request):
    # as of now, we're only dealing with get requests
    if (request.method == 'GET' and 'get_k' in request.GET) :
        # insert function here
        pi = u"\u03C0" + " = " + request.GET['get_k']
        return render(request, 'home/findnth/pi-tool.html', {'pi': pi}) 

    return render(request, 'home/findnth/pi-tool.html') 
