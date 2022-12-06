"""rpsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from baseapp.views import render_index, render_about, render_rules, render_maps, render_introduction, render_system
from . import settings

# паттерны послекорневой директории сайта
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render_index, name='home'),
    path('about/', render_about, name='about'),  # конечная страница о ролке
    path('rules/', render_rules, name='rules'),  # подкаталог с правилами
    path('map/', render_maps, name='maps'),  # конечная страница с картой
    path('map/<slug:system_slug>/', render_system, name='system'),
    path('introduction/', render_introduction, name='introduction'),  # конечная страница с вводной информацией
    path('rules/', include('baseapp.urls_rules'))  # расширение подкаталога пункта меню "Правила"
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
