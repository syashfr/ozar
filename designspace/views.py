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
        flag=0
        """Connect to aks only once
               Current behavior:
                 using flags for onetime connection, user namespaces created manually
                Expected behavior
                 connection to be established on app deployment. user namespace created when on boarded"""
        if(flag==0):
            connect_aks()
            flag=1
        if(request.GET['launch button']=='kicad'):   
            namespace = str(request.user)
            release_name = "kicad-"+str(request.user)
            #helm install in users AKS namespace
            launch_kicad(release_name=release_name, namespace=request.user)

            """Connecting to workspace
                    current behavior
                        get ingress addrs from k8, log onto addr/kicad/

                    expected behavior
                        redirect to workspace: hostname/userid/kicad. No hostaname as of now"""

        elif(request.GET['launch button']=='freecad'):
            print("##########the request is: freecad")
            print(request.user)
        return render(request, self.template_name)
    




