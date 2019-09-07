from django.urls import path
from search.views import SearchQueryView, SearchQueryAutocomplete

app_name = 'search'

urlpatterns = [
    path('', SearchQueryView, name='search'),
    path('autocomplete/', SearchQueryAutocomplete, name='searchauto')
]
