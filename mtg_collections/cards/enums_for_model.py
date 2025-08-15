from django.db import models


class SuperTypes(models.IntegerChoices):
    BASIC = 1, 'Базовый'
    LEGENDARY = 2, 'Легендарный'
    SNOWY = 3, 'Снежный'


class Types(models.IntegerChoices):
    CREATURE = 1, 'Существо'
    LAND = 2, 'Земля'
    ENCHANTMENT = 3, 'Заклинание'
    INSTANT = 4, 'Мгновение'
    SORCERY = 5, 'Заклятие'
    PLANESWALKER = 6, 'Планешаг'
    ARTIFACT = 7, 'Артефакт'


class Languages(models.IntegerChoices):
    RU = 1, 'Русский'
    EN = 2, 'Английский'


class Rarity(models.IntegerChoices):
    COMMON = 1, 'Обычный'
    UNCOMMON = 2, 'Необычный'
    RARE = 3, 'Редкий'
    MYTHIC = 4, 'Мифический'


class Layouts(models.IntegerChoices):
    STANDARD = 1, 'Стандартный'
    DOUBLE_SIDED = 2, 'Двусторонний'
    DOUBLE_FACED = 3, 'Двойной'
