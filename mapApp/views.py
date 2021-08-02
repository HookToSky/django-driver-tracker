from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class MapView(TemplateView):
    """map view."""

    template_name = "map.html"

