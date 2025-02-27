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


def car_insurance(request):
    return render(request, "anipages/car_insurance.html")

def home_insurance(request):
    return render(request, "anipages/home_insurance.html")


def health_insurance(request):
    return render(request, "anipages/health_insurance.html")