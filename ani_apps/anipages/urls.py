from django.urls import path
from django.utils.translation import gettext_lazy as _
from .views import HomeTemplateView, Insurance, contacts, information_form


app_name = "anipages"
 
urlpatterns = [
    path("", view=HomeTemplateView.as_view(), name="home"),
    path("contacts/", view=contacts, name="contacts"),
    path("insurance/", view=Insurance.as_view(), name="insurance"),
    path("get-started/", view=information_form, name="get_started")

]
