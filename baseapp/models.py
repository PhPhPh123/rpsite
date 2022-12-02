from django.db import models


class Systems(models.Model):
    """
    Модель, описывающая таблицу с системами, существующими внутри ролевой игры
    """
    system_name = models.CharField(max_length=50)
    system_description = models.TextField()
    system_danger = models.ForeignKey('DangerZone', on_delete=models.CASCADE)


class Worlds(models.Model):
    """
    Модель, описывающая таблицу с мирами, существующими внутри ролевой игры
    Каждый мир принадлежит к какой-либо системе и у модели на ее внешний ключ
    """
    world_name = models.CharField(max_length=50)
    world_description = models.TextField()
    system = models.ForeignKey('Systems', on_delete=models.CASCADE)


class DangerZone(models.Model):
    """
    Модель, описывающая таблицу с уровнями опасности, существующими внутри ролевой игры
    Опасность относится исключительно к системам, а если строго говоря, к космическому пространству между мирами
    Опасность отдельных миров описывается в отдельном проекте discord-бота
    """
    danger_name = models.CharField(max_length=50)
    danger_description = models.TextField()
