from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, DetailView, ListView
from rest_framework import viewsets
from models import Route
from serializers import RouteSerializer


class Home(TemplateView):
    template_name = 'my_maze/home.html'


class Learning(TemplateView):
    template_name = 'my_maze/learning.html'


class Other(TemplateView):
    template_name = 'my_maze/other.html'


class RouteView(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer