from django.shortcuts import render
from django.http import HttpResponse

"""
Контекстные переменные для рендера в шаблонах hmtl
"""
title = 'Вархаммер40к-РП-Ролка'

main_menu_list = [{'menu_name': 'О ролке', 'url_name': 'about'},
                  {'menu_name': 'Правила', 'url_name': 'rules'},
                  {'menu_name': 'Карта', 'url_name': 'maps'},
                  {'menu_name': 'Введение', 'url_name': 'introduction'}]

rules_list = ['Система сложности',
              'Локации',
              'Боевая система',
              'Торговля и экономика',
              'Психосилы и угрозы варпа',
              'Механика выживания']

context = {'title': title,
           'main_menu': main_menu_list,
           'rules': rules_list}


def index(request):
    """
    Данная функция рендерит основную, базовую страницу сайта
    """
    return render(request, 'baseapp/index.html', context=context)


def about(request):
    """
    Данная функция рендерит страницу о ролке
    """
    return render(request, 'baseapp/main_menu/about_rp.html', context=context)


def rules(request):
    """
    Данная функция рендерит страницу с селекторами правил
    """
    return render(request, 'baseapp/main_menu/main_rules_rp.html', context=context)


def maps(request):
    """
    Данная фукнция рендерит страницу с основной картой субсектора
    """
    return render(request, 'baseapp/main_menu/map_rp.html', context=context)


def introduction(request):
    """
    Данная функция рендерит страницу с введением в игру
    """
    return render(request, 'baseapp/main_menu/introduction_rp.html', context=context)


def battles(request):
    """
    Данная функция рендерит страницу с правилами боев внутри селектора правил
    """
    return render(request, 'baseapp/main_menu/rules/battles.html', context=context)


def danger(request):
    """
    Данная функция рендерит страницу с правилами по угрозам врагов и опасностям зон внутри селектора правил
    """
    return render(request, 'baseapp/main_menu/rules/danger_and_threat.html', context=context)


def death(request):
    """
    Данная функция рендерит страницу с механиками выживания внутри селектора правил
    """
    return render(request, 'baseapp/main_menu/rules/HT_and_death.html', context=context)


def movement(request):
    """
    Данная функция рендерит страницу с механикой перемещения по локациям внутри селектора правил
    """
    return render(request, 'baseapp/main_menu/rules/movement.html', context=context)


def psionics(request):
    """
    Данная функция рендерит страницу с псионикой внутри селектора правил
    """
    return render(request, 'baseapp/main_menu/rules/Psionics_and_warp.html', context=context)


def economy(request):
    """
    Данная функция рендерит страницу с описанием экономической системы внутри селектора правил
    """
    return render(request, 'baseapp/main_menu/rules/trade_and_economy.html', context=context)
