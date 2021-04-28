from django.urls import path
from django.urls import include
from .views import DesignSpaceHomepage, HomeView, LaunchWorkSpace, DesignDetailView , UploadFiles, fork_file


urlpatterns = [
    #path('', DesignSpaceHomepage.as_view(), name='designspace'),
    path('', HomeView.as_view(), name = 'home'),
    path('upload/', UploadFiles.as_view(), name= 'upload'),
    path('design/<slug>/', DesignDetailView.as_view(), name= 'design'),
    path('workspace/',LaunchWorkSpace.as_view(), name='workspace'),
    path('fork/', fork_file, name='fork')
]