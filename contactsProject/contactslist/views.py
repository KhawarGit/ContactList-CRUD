from django.shortcuts import render, redirect, reverse
from .models import Contact
# Create your views here.

from django.http import HttpResponse
from django.template import loader

def display(request):
    template = loader.get_template('contact-display.html')

    contacts = Contact.objects.all()

    contact = []
    for c in contacts:

        contact.append(c)
    context = {
        'contacts': contact
    }

    return HttpResponse(template.render(context, request))

def delete(request):
    id = request.GET.get('id')
    contact_to_delete = Contact.objects.get(id=id)
    contact_to_delete.delete()

    return redirect(reverse('display-contacts'))