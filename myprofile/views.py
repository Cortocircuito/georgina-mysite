from django.shortcuts import render
from django.views.decorators.cache import never_cache

# Create your views here.
@never_cache
def index(request):
    return render(request, 'myprofile/index.html', {})

@never_cache
def galeria(request):
    return render(request, 'myprofile/galeria.html', {})

@never_cache
def insta(request):
    return render(request, 'myprofile/insta.html', {})
