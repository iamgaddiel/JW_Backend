from typing import Any
from uuid import uuid4

from django.shortcuts import render
from django import http
from django.views.generic import TemplateView, ListView, DetailView

from api.models import (
    Jersey,
)


class Index(TemplateView):
    template_name = "core/index.html"

    def get(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        if not (self.request.session.has_key('user_session')):
            self.request.session['user_session'] = str(uuid4())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class JerseyStoreView(ListView):
    template_name = 'core/store.html'

    def get_queryset(self):
        category: str = self.kwargs.get('category')
        queryset = Jersey.objects.filter(category__title=category)
        return queryset

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        category: str = self.kwargs.get('category')
        context = super().get_context_data(**kwargs)
        context['category'] =  category
        return context


class JerseyDetailView(DetailView):
    template_name = 'core/jersey_detail.html'
    model = Jersey

