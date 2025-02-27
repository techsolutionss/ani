from django.urls import path
from django.utils.translation import gettext_lazy as _
from .views import (HomeTemplateView, Insurance, contacts, information_form,
                     car_insurance, home_insurance, health_insurance)


app_name = "anipages"
 
urlpatterns = [
    path("", view=HomeTemplateView.as_view(), name="home"),
    path("contacts/", view=contacts, name="contacts"),
    path("insurance/", view=Insurance.as_view(), name="insurance"),
    path("get-started/", view=information_form, name="get_started"),
    path("car-insurance/", view=car_insurance, name="car_insurance"),
    path("home-insurance/", view=home_insurance, name="home_insurance"),
    path("health-insurance/", view=health_insurance, name="health_insurance")

]
