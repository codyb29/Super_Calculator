from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/homepage.html') 

def pi_tool(request):
    return render(request, 'home/findnth/pi-tool.html') 
