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

def edit_form(request):
    template = loader.get_template('edit-contact.html')

    # id = request.GET.get('id')
    # fn = request.GET.get('fn')
    # ln = request.GET.get('ln')
    # email = request.GET.get('email')
    # comment = request.GET.get('comment')
    context = {
        'contact': {
            'id': request.GET.get('id'),
            'first_Name': request.GET.get('fn'),
            'last_Name': request.GET.get('ln'),
            'email': request.GET.get('email'),
            'comment': request.GET.get('comment')
        }
    }
    # print(id, fn, ln, email, comment)
    return HttpResponse(template.render(context, request))
