import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .launch_handler import *

# Create your views here.
class DesignSpaceHomepage(TemplateView):
    template_name = 'designspace_homepage.html'

class LaunchWorkSpace(TemplateView):
    template_name = 'launch_results.html'

    def get(self, request):
        if(request.GET['launch button']=='kicad'):  
            namespace = str(request.user)
            release_name = "kicad-"+str(request.user)
            #helm install kicad in users AKS namespace
            launch_kicad(release_name=release_name, namespace=request.user, action="install")
            
        elif(request.GET['launch button']=='freecad'):
            namespace = str(request.user)
            release_name = "freecad-"+str(request.user)
            #helm install freecad in users AKS namespace
            launch_freecad(release_name=release_name, namespace=request.user, action="install")
            
        """Access to workspace
                    current behavior
                        get ingress addrs from k8, log onto addr/kicad/

                    expected behavior
                        redirect to workspace: hostname/userid/kicad. No hostaname as of now"""
        return render(request, self.template_name)
    




