from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView



class Index(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

