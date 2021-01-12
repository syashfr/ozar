from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.home_page, name='designspace'),
    path('kicad/',views.create_kicad_workspace, name='kicad'),
]