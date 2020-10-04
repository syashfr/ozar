from django.urls import path

from .views import MarketplaceHomepage, MarketplaceSearchResult

urlpatterns = [
    path('', MarketplaceHomepage.as_view(), name='marketplace'),
    path('search/', MarketplaceSearchResult.as_view(), name='search_results')
]