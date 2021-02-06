from az.cli import az
from django.apps import AppConfig


class DesignspaceConfig(AppConfig):
    name = 'designspace'
    #IMP: AKS cluster with the name: ozar-d-designspace must be deployed
    #establish one time connection with AKS
    az("aks get-credentials --resource-group ozar-d-rg --name ozar-d-designspace")