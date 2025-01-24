from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = "anipages/home.html"


def contacts(request):
    return render(request, "anipages/contacts.html")


class Insurance(TemplateView):
    template_name = "anipages/insurance.html"

def information_form(request):
    return render(request, "anipages/information_form.html")