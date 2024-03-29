"""
URL configuration for contactsProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contactslist import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("display-contacts/", views.display, name='display-contacts'),
    path("display-contacts/delete", views.delete),
    path("display-contacts/edit", views.edit_form),
    path("display-contacts/change", views.change, name='change'),
    path("display-contacts/add-contact-form", views.add_form),
    path("display-contacts/add", views.add, name="add"),

]
