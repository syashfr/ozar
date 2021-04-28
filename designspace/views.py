import os
import json
from .models import Design, User
from django.shortcuts import redirect
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from .design_handler import plot_mesh
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView
from django.template.response import TemplateResponse
from django.template import Context, Template
from .launch_handler import *
from .forms import UploadForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from django.http import JsonResponse

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

class UploadFiles(TemplateView):
    def get(self, request):
        form = UploadForm()
        return render(request, 'upload.html', {
            'form': form
        })

    def post(self, request):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            design = form.save(commit=False)
            design.author = self.request.user
            design.save()
            return redirect('home')

@login_required  
def fork_file(request):
        # retrieve original design
        design_id = int(request.GET.get('pk'))
        design = Design.objects.get(pk = design_id)
        slug = design.slug
        current_user = request.user
        # fork if the user is not the author
        if(current_user != design.author):
            already_forked = False
            # fork if the not already forked
            user_designs = Design.objects.filter(author = current_user)
            for user_design in user_designs:
                 print(type(user_design.forked_from), type(design_id))
                 if (user_design.forked_from == design_id):
                    already_forked = True
                    break
            if(already_forked):
                messages.info(request, "Cannot fork: design already forked")
            else:
                #fork = copy and change - author, forked, forked_from 
                design_forked = design
                design_forked.pk = None
                design_forked.author = current_user
                design_forked.forked = True
                design_forked.forked_from = design_id
                #save forked design
                design_forked.save() 
                messages.info(request, "design forked")
        else:
            messages.info(request, "Cannot fork: you are the author of this design")
        return redirect("designspace:design", slug=slug)
        