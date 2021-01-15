import json
from django.http import HttpResponse
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes

# Create your views here.
class DesignSpaceHomepage(TemplateView):
    template_name = 'designspace_homepage.html'


class LaunchWorkSpace(TemplateView):
    template_name = 'search_results.html'

# def home_page(TemplateView):    
#    return HttpResponse("Welcome to the design space")

# @api_view(['GET'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def create_kicad_workspace(request, format=None):
#     content = {
#         'user': request.user,  # `django.contrib.auth.User` instance.
#         'auth': request.auth,  # None
#                 }
#     return Response(content)
