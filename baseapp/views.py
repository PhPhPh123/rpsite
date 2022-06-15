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
    return render(request, 'baseapp/index.html', {'title': title, 'main_menu': main_menu_list})


def about(request):
    return render(request, 'baseapp/main_menu/about_rp.html', {'title': title, 'main_menu': main_menu_list})


def enemies(request):
    return render(request, 'baseapp/main_menu/enemy_units_rp.html', {'title': title, 'main_menu': main_menu_list})


def rules(request):
    return render(request, 'baseapp/main_menu/main_rules_rp.html', {'title': title, 'main_menu': main_menu_list, 'rules': rules_list})


def maps(request):
    return render(request, 'baseapp/main_menu/map_rp.html', {'title': title, 'main_menu': main_menu_list})


def schedule(request):
    return render(request, 'baseapp/main_menu/schedule_rp.html', {'title': title, 'main_menu': main_menu_list})


def battles(request):
    return render(request, 'baseapp/main_menu/rules/battles.html', {'title': title, 'main_menu': main_menu_list, 'rules': rules_list})


def danger(request):
    return render(request, 'baseapp/main_menu/rules/danger_and_threat.html', {'title': title, 'main_menu': main_menu_list, 'rules': rules_list})


def death(request):
    return render(request, 'baseapp/main_menu/rules/HT_and_death.html', {'title': title, 'main_menu': main_menu_list, 'rules': rules_list})


def movement(request):
    return render(request, 'baseapp/main_menu/rules/movement.html', {'title': title, 'main_menu': main_menu_list, 'rules': rules_list})


def psionics(request):
    return render(request, 'baseapp/main_menu/rules/Psionics_and_warp.html', {'title': title, 'main_menu': main_menu_list, 'rules': rules_list})


def space_battles(request):
    return render(request, 'baseapp/main_menu/rules/space_battles.html', {'title': title, 'main_menu': main_menu_list, 'rules': rules_list})


def economy(request):
    return render(request, 'baseapp/main_menu/rules/trade_and_economy.html', {'title': title, 'main_menu': main_menu_list, 'rules': rules_list})
