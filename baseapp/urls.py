from django.urls import path
from baseapp.views import battles, danger, death, movement, psionics, space_battles, economy

urlpatterns = [
    path('battles/', battles),
    path('danger/', danger),
    path('death/', death),
    path('movement/', movement),
    path('psionics/', psionics),
    path('spacebattles/', space_battles),
    path('economy/', economy)
]
