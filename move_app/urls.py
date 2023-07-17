from django.urls import path
# Import All_
from .views import All_moves

# remember all urls are prefaced by http://localhost:8000/api/v1/moves/
urlpatterns = [
    path('', All_moves.as_view(), name='all_views')
]