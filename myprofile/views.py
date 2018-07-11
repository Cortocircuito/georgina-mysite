# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.cache import never_cache
import sendgrid
import os
from sendgrid.helpers.mail import Email, Content, Mail


# Create your views here.
@never_cache
def index(request):
    errors = []

    nombre = request.POST.get('nombre', '')
    email = request.POST.get('email', '')
    mensaje = request.POST.get('mensaje', '')

    if request.method == 'POST':
        if not nombre:
            errors.append('Por favor introduce un nombre')
        if not email:
            errors.append('Por favor introduce un correo electrónico')
        if not mensaje:
            errors.append('Por favor introduce un mensaje')

        if not errors:
            sg = sendgrid \
                 .SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

            from_email = Email(email)
            to_email = Email("mejorcomertepara@gmail.com")
            subject = "Consulta del paciente " + nombre
            content = Content("text/plain", mensaje)

            mail = Mail(from_email, subject, to_email, content)
            response = sg.client.mail.send.post(request_body=mail.get())

            print(response.status_code)
            print(response.body)
            print(response.headers)

    return render(request, 'myprofile/index.html', {'errors': errors,
                                                    'nombre': nombre,
                                                    'email': email,
                                                    'mensaje': mensaje})


def galeria(request):
    return render(request, 'myprofile/galeria.html', {})


def insta(request):
    return render(request, 'myprofile/insta.html', {})
