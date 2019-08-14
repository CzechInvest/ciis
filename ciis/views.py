from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "ciis/index.html"
    context_object_name = "index_context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context
