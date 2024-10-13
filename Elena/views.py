from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, "home.html")
def index1(request):
    return render (request, "name.html")
def index2(request):
    return render (request, "age.html")

def index3(request):
    return render (request, "group.html")

def index4(request):
    return render (request, "common.html")