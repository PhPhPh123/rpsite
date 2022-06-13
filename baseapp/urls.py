from django.urls import path
from baseapp.views import battles

urlpatterns = [
    path('battles/', battles),
    # path('/danger', death),
    # path('/death', death),
    # path('/movement', movement),
    # path('/psionics', psionics),
    # path('/spacebattles', space_battles),
    # path('/economy', economy)
]
