from django.shortcuts import render
from django.views.decorators.cache import never_cache
import sendgrid
import os
from sendgrid.helpers.mail import Email, Content, Mail


# Create your views here.
@never_cache
def index(request):
    return render(request, 'myprofile/index.html', {})


def contacto(request):
    # Aqui toca recoger Nombre Email y Mensaje
    nombre = request.POST['nombre']
    email = request.POST['email']
    mensaje = request.POST['mensaje']

    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

    from_email = Email(email)
    to_email = Email("mejorcomertepara@gmail.com")
    subject = "Consulta del paciente " + nombre
    content = Content("text/plain", mensaje)

    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())

    print(response.status_code)
    print(response.body)
    print(response.headers)

    return render(request, 'myprofile/index.html', {})


def galeria(request):
    return render(request, 'myprofile/galeria.html', {})


def insta(request):
    return render(request, 'myprofile/insta.html', {})
