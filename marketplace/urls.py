from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from .views import MarketplaceHomepage, MarketplaceSearchResult

urlpatterns = [
    path('', MarketplaceHomepage.as_view(), name='marketplace'),
    path('search/', MarketplaceSearchResult.as_view(), name='search_results')
]