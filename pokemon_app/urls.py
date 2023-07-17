from django.urls import path
# Explicit imports
from .views import All_pokemon
# Remember all urls are prefaced by http://localhost:8000/api/v1/pokemon/
urlpatterns = [
    # Currently only takes GET requests
    path('', All_pokemon.as_view(), name='all_pokemon')
]