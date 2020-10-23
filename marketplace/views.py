from marketplace.models import Service
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView


class MarketplaceHomepage(TemplateView):
    template_name = 'marketplace_homepage.html'

class MarketplaceSearchResult(ListView):
    template_name = 'search_results.html'

    def get_queryset(self): 
        query = self.request.GET.get('q')
        #get object list by category
        object_list = Service.objects.filter(category = query)
        return object_list

