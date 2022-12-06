from django.shortcuts import render, get_object_or_404
from .models import *

"""
Контекстные переменные для рендера в шаблонах hmtl
"""

title = 'Вархаммер40к-РП-Ролка'  # титульное название сайта

# Список пунктов главного меню боковой левой панели
main_menu_list = [{'menu_name': 'О ролке', 'url_name': 'about'},
                  {'menu_name': 'Правила', 'url_name': 'rules'},
                  {'menu_name': 'Карта', 'url_name': 'maps'},
                  {'menu_name': 'Введение', 'url_name': 'introduction'}]

# список плиток grid для пункта меню "Правила"
rules_list = ['Система сложности',
              'Локации',
              'Боевая система',
              'Торговля и экономика',
              'Психосилы и угрозы варпа',
              'Механика выживания']

# переменная контекста для передачи в шаблон функций представлений
context = {'title': title,
           'main_menu': main_menu_list,
           'rules': rules_list}


def render_index(request):
    """
    Данная функция рендерит основную, базовую страницу сайта
    """
    return render(request, 'baseapp/index.html', context=context)


def render_about(request):
    """
    Данная функция рендерит страницу о ролке
    """
    return render(request, 'baseapp/main_menu/about_rp.html', context=context)


def render_rules(request):
    """
    Данная функция рендерит страницу с селекторами правил
    """
    return render(request, 'baseapp/main_menu/main_rules_rp.html', context=context)


def render_maps(request):
    """
    Данная фукнция рендерит страницу с основной картой субсектора
    """
    return render(request, 'baseapp/main_menu/map_rp.html', context=context)


def render_introduction(request):
    """
    Данная функция рендерит страницу с введением в игру
    """
    return render(request, 'baseapp/main_menu/introduction_rp.html', context=context)


def render_battles(request):
    """
    Данная функция рендерит страницу с правилами боев внутри селектора правил
    """
    return render(request, 'baseapp/main_menu/rules/battles.html', context=context)


def render_danger(request):
    """
    Данная функция рендерит страницу с правилами по угрозам врагов и опасностям зон внутри селектора правил
    """
    return render(request, 'baseapp/main_menu/rules/danger_and_threat.html', context=context)


def render_death_and_ht(request):
    """
    Данная функция рендерит страницу с механиками выживания внутри селектора правил
    """
    return render(request, 'baseapp/main_menu/rules/HT_and_death.html', context=context)


def render_movement(request):
    """
    Данная функция рендерит страницу с механикой перемещения по локациям внутри селектора правил
    """
    return render(request, 'baseapp/main_menu/rules/movement.html', context=context)


def render_psionics(request):
    """
    Данная функция рендерит страницу с псионикой внутри селектора правил
    """
    return render(request, 'baseapp/main_menu/rules/Psionics_and_warp.html', context=context)


def render_trade_and_economy(request):
    """
    Данная функция рендерит страницу с описанием экономической системы внутри селектора правил
    """
    return render(request, 'baseapp/main_menu/rules/trade_and_economy.html', context=context)


def render_system(request, system_slug):
    """
    Данная функция рендерит страницы с системами внутри карты
    Args:
        system_slug:
        request:

    Returns:
    """

    system = get_object_or_404(System, system_slug=system_slug)
    worlds_in_system = World.objects.filter(system_id=system.pk)
    system_context = {'title': title,
                      'main_menu': main_menu_list,
                      'rules': rules_list,
                      'system': system,
                      'worlds': worlds_in_system}

    return render(request, 'baseapp/main_menu/worlds.html', context=system_context)
