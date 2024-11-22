from django.shortcuts import render
def index(request):
    return render(request, "main/index.html")
def autumn(request):
    return render(request, "main/autumn.html")
def colottype(request):
    return render(request, "templates/colottype.html")
def log(request):
    return render(request, "templates/log.html")
def razdeli(request):
    return render(request, "templates/razdeli.html")
def spring(request):
    return render(request, "templates/spring.html")
def summer(request):
    return render(request, "templates/summer.html")
def winter(request):
    return render(request, "templates/winter.html")    
