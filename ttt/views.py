from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h2> Hello </h2>")
def templateshow(request):
    return render(request,"index.html")
