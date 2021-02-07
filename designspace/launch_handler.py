import subprocess
from az.cli import az

def aks_connect(rg, cluster):
    """ Connects to AKS cluster. No auth as of now

    Args:
        rg (string): name of the resource group
        cluster (string): name of the AKS cluster
    """
    az("aks get-credentials --resource-group {} --name {}".format(rg, cluster))


def helm_repo_add(name):
    """ Add helm repo to the attached k8 cluster

    Args:
        name (string): name of workspace: kicad/freecad
    """
    subprocess.call(["helm", "repo", "add", name+"-stable","https://syashfr.github.io/"+name])
    
def launch_workspace(name, namespace):
    """ Install helm charts

    Args:
        name (string): name of workspace: kicad/freecad
        namespace (string): corresponds to users namespace
    """
    subprocess.call(["helm", "install", name+"-release", "{}-stable/{}".format(name,name), "-n", namespace])