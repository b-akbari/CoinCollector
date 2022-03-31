from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#defining home view
def home(request):
    return render(request,'home.html')
    # return HttpResponse('<h1>coin collecta<h1>')

def about(request):
    return render(request,'about.html')
