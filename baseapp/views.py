from django.shortcuts import render
from django.http import HttpResponse

title = 'Вархаммер40к-РП-Ролка'

main_menu_list = [{'menu_name': 'О ролке', 'url_name': 'about'},
                  {'menu_name': 'Правила', 'url_name': 'rules'},
                  {'menu_name': 'Карты', 'url_name': 'maps'},
                  {'menu_name': 'Бестиарий', 'url_name': 'enemies'},
                  {'menu_name': 'Расписание', 'url_name': 'schedule'}]

rules_list = ['Сложность зон и угроза противников',
              'Передвижение в варпе, космосе и на земле',
              'Наземный бой и сражения на технике',
              'Космические сражения',
              'Торговля и экономика',
              'Психосилы и угрозы варпа',
              'Живучесть игроков, предсмертные состояния и смерть']

context = {'title': title,
           'main_menu': main_menu_list,
           'rules': rules_list}


def index(request):
    return render(request, 'baseapp/index.html', context=context)


def about(request):
    return render(request, 'baseapp/main_menu/about_rp.html', context=context)


def enemies(request):
    return render(request, 'baseapp/main_menu/enemy_units_rp.html', context=context)


def rules(request):
    return render(request, 'baseapp/main_menu/main_rules_rp.html', context=context)


def maps(request):
    return render(request, 'baseapp/main_menu/map_rp.html', context=context)


def schedule(request):
    return render(request, 'baseapp/main_menu/schedule_rp.html', context=context)


def battles(request):
    return render(request, 'baseapp/main_menu/rules/battles.html', context=context)


def danger(request):
    return render(request, 'baseapp/main_menu/rules/danger_and_threat.html', context=context)


def death(request):
    return render(request, 'baseapp/main_menu/rules/HT_and_death.html', context=context)


def movement(request):
    return render(request, 'baseapp/main_menu/rules/movement.html', context=context)


def psionics(request):
    return render(request, 'baseapp/main_menu/rules/Psionics_and_warp.html', context=context)


def space_battles(request):
    return render(request, 'baseapp/main_menu/rules/space_battles.html', context=context)


def economy(request):
    return render(request, 'baseapp/main_menu/rules/trade_and_economy.html', context=context)
