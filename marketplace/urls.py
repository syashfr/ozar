from django.urls import path

from .views import marketplace_homepage, marketplace_search_result

urlpatterns = [
    path('', marketplace_homepage.as_view(), name='marketplace'),
    path('search/', marketplace_search_result.as_view(), name='search_results')
]