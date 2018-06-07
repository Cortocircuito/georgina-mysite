from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'myprofile/index.html', {})

def galeria(request):
    return render(request, 'myprofile/galeria.html', {})

def blog(request):
    return render(request, 'myprofile/blog.html', {})
