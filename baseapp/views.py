from django.shortcuts import render
from django.http import HttpResponse

title = 'Вархаммер40к-РП-Ролка'

main_menu_list = ['О ролке',
                  'Правила',
                  'Карты',
                  'Бестиарий',
                  'Расписание игр']

rules_list = ['Сложность зон и угроза противников',
              'Передвижение в варпе, космосе и на земле',
              'Наземный бой и сражения на технике',
              'Космические сражения',
              'Торговля и экономика',
              'Психосилы и угрозы варпа',
              'Живучесть игроков, предсмертные состояния и смерть']


def index(request):
    return render(request, 'index.html', {'title': title, 'main_menu': main_menu_list})


def about(request):
    return render(request, 'main_menu/about_rp.html', {'title': title, 'main_menu': main_menu_list})


def enemies(request):
    return render(request, 'main_menu/enemy_units_rp.html', {'title': title, 'main_menu': main_menu_list})


def rules(request):
    return render(request, 'main_menu/main_rules_rp.html', {'title': title, 'main_menu': main_menu_list, 'rules': rules_list})


def maps(request):
    return render(request, 'main_menu/map_rp.html', {'title': title, 'main_menu': main_menu_list})


def schedule(request):
    return render(request, 'main_menu/schedule_rp.html', {'title': title, 'main_menu': main_menu_list})


def battles(request):
    return render(request, 'main_menu/rules/battles.html', {'title': title, 'main_menu': main_menu_list, 'rules': rules_list})