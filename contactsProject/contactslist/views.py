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

    context = {
        'contact': {
            'id': request.GET.get('id'),
            'first_Name': request.GET.get('fn'),
            'last_Name': request.GET.get('ln'),
            'email': request.GET.get('email'),
            'comment': request.GET.get('comment')
        }
    }
    
    return HttpResponse(template.render(context, request))

def change(request):
    print(request.POST.get("id"))
    contact_to_change = Contact.objects.get(id=int(request.POST.get('id')))
    contact_to_change.first_Name = request.POST.get("fn")
    contact_to_change.last_Name = request.POST.get("ln")
    contact_to_change.email = request.POST.get("email")
    contact_to_change.comment = request.POST.get("com")
    contact_to_change.save()
    return redirect(reverse('display-contacts'))

def add_form(request):
    template = loader.get_template('add-contact.html')
    return HttpResponse(template.render({},request))

def add(request):
    Contact.objects.create(
        first_Name=request.POST.get("fn"),
        last_Name=request.POST.get("ln",''),
        email=request.POST.get("email"),
        comment=request.POST.get("comment", '')
    )

    return redirect(reverse('display-contacts'))