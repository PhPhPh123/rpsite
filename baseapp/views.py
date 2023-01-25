from django.shortcuts import render, get_object_or_404, redirect

from .forms import PlayerRegisterForm
from .models import *

"""
Контекстные переменные для рендера в шаблонах hmtl
"""

title = 'Вархаммер40к-РП-Ролка'  # титульное название сайта

# Список пунктов главного меню боковой левой панели
main_menu_list = [{'menu_name': 'О ролке', 'url_name': 'about'},
                  {'menu_name': 'Правила', 'url_name': 'rules'},
                  {'menu_name': 'Карта', 'url_name': 'maps'},
                  {'menu_name': 'Введение', 'url_name': 'introduction'},
                  {'menu_name': 'Регистрация', 'url_name': 'register'}]

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
    all_systems = {'all_systems': System.objects.all()}
    return render(request, 'baseapp/main_menu/map_rp.html', context={**context, **all_systems})


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
    worlds_amount = len(worlds_in_system)

    worlds_tag = {'worlds': tuple(enumerate(worlds_in_system)), "worlds_amount": worlds_amount}
    system_tag = {'system': system}
    system_context = {**context, **worlds_tag, **system_tag}

    return render(request, 'baseapp/main_menu/systems.html', context=system_context)


def render_register(request):
    if request.method == 'POST':
        register_form = PlayerRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return redirect('register-success/')
    else:
        register_form = PlayerRegisterForm()

    form_tag = {'register_form': register_form}
    register_context = {**context, **form_tag}

    return render(request, 'baseapp/register.html', register_context)


def render_register_success(request):
    return render(request, 'baseapp/register_success.html', context)
