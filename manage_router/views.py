from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models

class IndexView(TemplateView):
    template_name = 'index.html'

class routerListView(ListView):
    context_object_name = 'router_list'
    model = models.router


class routerDetailView(DetailView):
    context_object_name = 'router_details'
    # fields = ("loopBack")
    model = models.properties
    template_name = 'manage_router/router_detail.html'


class routerCreateView(CreateView):
    fields = ("hostName",)
    model = models.router


class routerUpdateView(UpdateView):
    fields = ("sapId","hostName","macAddress")
    model = models.properties
    template_name = 'manage_router/router_form.html'

class routerDeleteView(DeleteView):
    model = models.router
    success_url = reverse_lazy("manage_router:list")
