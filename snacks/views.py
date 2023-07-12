from django.shortcuts import render
from django.views.generic import TemplateView,SnackView,SnackView
from .models import Snack
# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'

class ThingsListView(SnackView):
    template_name = 'Snack_list.html'
    model = Snack
    context_object_name = "data"

class ThingDetailsView(SnackView):
    template_name = 'Snack_details.html'
    model = Snack
