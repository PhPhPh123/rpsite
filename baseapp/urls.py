from django.urls import path
from baseapp.views import render_battles, render_danger, render_death_and_ht
from baseapp.views import render_movement, render_psionics, render_trade_and_economy

# url-паттерны для пункта меню: "Правила", данные паттерны расширяются include из 'rpsite/urls.py'
urlpatterns = [
    path('battles/', render_battles, name='battles'),
    path('danger/', render_danger, name='danger'),
    path('death/', render_death_and_ht, name='death'),
    path('movement/', render_movement, name='movement'),
    path('psionics/', render_psionics, name='psionics'),
    path('economy/', render_trade_and_economy, name='economy')
]
