from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.core.mail import send_mail

# Create your views here.
@never_cache
def index(request):
    return render(request, 'myprofile/index.html', {})

@never_cache
def contacto(request):
    send_mail('Subject here', 'Here is the message.', 'from@example.com', ['isdsate@gmail.com'], fail_silently=False)
    return render(request, 'myprofile/index.html', {})

@never_cache
def galeria(request):
    return render(request, 'myprofile/galeria.html', {})

@never_cache
def insta(request):
    return render(request, 'myprofile/insta.html', {})
