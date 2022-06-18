from django.urls import path
from baseapp.views import battles, danger, death, movement, psionics, space_battles, economy

urlpatterns = [
    path('battles/', battles, name='battles'),
    path('danger/', danger, name='danger'),
    path('death/', death, name='death'),
    path('movement/', movement, name='movement'),
    path('psionics/', psionics, name='psionics'),
    path('spacebattles/', space_battles, name='spacebattles'),
    path('economy/', economy, name='economy')
]
