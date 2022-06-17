from django.urls import path
from baseapp.views import battles, danger, death, movement, psionics, space_battles, economy

urlpatterns = [
    path('battles/', battles, name='home'),
    path('danger/', danger, name='about'),
    path('death/', death, name='death'),
    path('movement/', movement, name='movement'),
    path('psionics/', psionics, name='psionics'),
    path('spacebattles/', space_battles, name='spacebattles'),
    path('economy/', economy, name='economy')
]
