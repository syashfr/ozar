from django.urls import path
from django.urls import include
from .views import DesignSpaceHomepage, LaunchWorkSpace


urlpatterns = [
    path('', DesignSpaceHomepage.as_view(), name='designspace'),
    path('workspace/',LaunchWorkSpace.as_view(), name='workspace'),
]