import os
import json
from .models import Design
from django.conf import settings
from django.shortcuts import render
from .design_handler import plot_mesh
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.template.response import TemplateResponse
from django.template import Context, Template
from .launch_handler import *

# Create your views here.
class HomeView(ListView):
    model = Design
    template_name = 'home.html'

class DesignDetailView(DetailView):
    model = Design
    template_name = "design.html"

class DesignSpaceHomepage(TemplateView):
    template_name = 'designspace_homepage.html'

class LaunchWorkSpace(TemplateView):
    template_name = 'launch_results.html'

    def get(self, request):
        namespace = str(request.user)
        if(request.GET['launch button']=='kicad'):
            #helm install kicad in users AKS namespace
            launch_workspace(name="kicad", namespace=namespace)
            
        elif(request.GET['launch button']=='freecad'):
            #helm install freecad in users AKS namespace
            launch_workspace(name="freecad", namespace=namespace)
            
        """Access to workspace
                    current behavior
                        get ingress addrs from k8, log onto addr/kicad/

                    expected behavior
                        redirect to workspace: hostname/userid/kicad. No hostaname as of now"""
        return render(request, self.template_name)
    




