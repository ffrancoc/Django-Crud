from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact

from datetime import datetime


def index(request):
    return render(request, 'contacts/index.html', {})


def contact_list(request):
    contacts = Contact.objects.all()

    context = {
        'contacts': contacts
    }

    return render(request, 'contacts/list.html', context)


def test(request):
    # Contact.objects.create(
    #     first_name='Annie Chantelle',
    #     last_name='Mollei Troy',
    #     address='STA ROSA, GUSTAVO A MADERO, 07620',
    #     phone_number='+506 26400724',
    #     email='annchantromoy@email.com',
    #     birthday_date=datetime.strptime('28/11/1989', '%d/%m/%Y')
    # )
    return HttpResponse('Registro Guardado')
