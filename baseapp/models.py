from django.db import models


class System(models.Model):
    """
    Модель, описывающая таблицу с системами, существующими внутри ролевой игры
    """
    system_name = models.CharField(max_length=50)
    system_slug = models.SlugField(unique=True, verbose_name='URL', null=True)
    system_description = models.TextField(null=True)
    system_danger = models.ForeignKey('DangerZone', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.system_name

    class Meta:
        verbose_name = 'Система'
        verbose_name_plural = 'Системы'
        ordering = ('system_name',)  # Сортировка по названию системы


class World(models.Model):
    """
    Модель, описывающая таблицу с мирами, существующими внутри ролевой игры
    Каждый мир принадлежит к какой-либо системе и у модели на ее внешний ключ
    """
    world_name = models.CharField(max_length=50)
    world_description = models.TextField(null=True)
    world_image = models.ImageField(null=True, upload_to='world_images/')
    system = models.ForeignKey('System', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.world_name

    class Meta:
        verbose_name = 'Мир'
        verbose_name_plural = 'Миры'
        ordering = ('world_name',)  # Сортировка по названию мира


class DangerZone(models.Model):
    """
    Модель, описывающая таблицу с уровнями опасности, существующими внутри ролевой игры
    Опасность относится исключительно к системам, а если строго говоря, к космическому пространству между мирами
    Опасность отдельных миров описывается в отдельном проекте discord-бота
    """
    danger_name = models.CharField(max_length=50)
    danger_description = models.TextField(null=True)

    def __str__(self):
        return self.danger_name


class PlayerRegister(models.Model):
    player_name = models.CharField(max_length=30)
    character_name = models.CharField(max_length=30)
    character_power = models.IntegerField()
    character_background = models.TextField(max_length=2000)
    character_image = models.ImageField(null=True, upload_to='player_images/')
