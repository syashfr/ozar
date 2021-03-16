from django.urls import path
from django.urls import include
from .views import DesignSpaceHomepage, HomeView, LaunchWorkSpace, View3D, DesignDetailView


urlpatterns = [
    #path('', DesignSpaceHomepage.as_view(), name='designspace'),
    path('', HomeView.as_view(), name = 'home'),
    path('view3d/', View3D.as_view(), name='view3d'),
    path('design/<slug>/', DesignDetailView.as_view(), name= 'design'),
    path('workspace/',LaunchWorkSpace.as_view(), name='workspace'),
]