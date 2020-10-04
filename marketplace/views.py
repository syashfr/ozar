from marketplace.models import Service
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView


class MarketplaceHomepage(TemplateView):
    template_name = 'marketplace_homepage.html'

class MarketplaceSearchResult(ListView):
    template_name = 'search_results.html'
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Service.objects.filter(name = query)
        return object_list