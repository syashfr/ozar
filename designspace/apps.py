from django.apps import AppConfig
from .launch_handler import aks_connect, helm_repo_add

class DesignspaceConfig(AppConfig):
    name = 'designspace'

    # Currently not deploying any workspace 
    #def ready(self):
    #     """ Initialisation tasks
    #     """
    #     # IMP: AKS cluster with the name: ozards-d-aks must be deployed
    #     # Establish one time connection with AKS
    #     aks_connect("ozar-d-rg", "ozards-d-aks")

    #     # IMP: helm must be installed on the application environment (to be containerised in future)
    #     # Add kicad and freecad helm repos
    #     helm_repo_add("kicad")
    #     helm_repo_add("freecad")