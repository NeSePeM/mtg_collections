"""
Модели для приложения mtg_collections.

Приложение для создания коллекций и колод карт.
"""


from django.contrib.auth.models import AbstractUser
from django.db import models

import enums


class User(AbstractUser):
    """Модель пользователя."""


class Card(models.Model):
    """Модель карты."""

    #  Делать ли все эти поля ForeignKey?
    scryfall_id = models.UUIDField('Идентификатор карты')
    name = models.CharField('Имя')  # Название. На английском можно считать primary key. Хотя у меня в основном русские карты.
    super_type = models.IntegerChoices(enums.SuperTypes, verbose_name='Супертип')  # Супертип карты: базовый, легендарный, снежный.
    typee = models.IntegerChoices(enums.Types, verbose_name='Супертип')  # Тип карты: creature, land, enchantment, instant, sorcery, planeswalker, artifact, etc.
    sub_type = models.CharField('Подтип')
    text = models.TextField('Текст карты')
    mana_cost = models.CharField('Мана-стоимость')  # Написано в формате {1}{W}{U}{B}{R}{G} - формат из Правил.
    sett = models.CharField('Выпуск')  # Название сета. Трёхбуквенный код.
    rarity = models.IntegerChoices(enums.Rarity, verbose_name='Редкость')  # Редкость карты: common, uncommon, rare, mythic.
    foiled = models.BooleanField('Фольгированная')
    language = models.IntegerChoices(enums.Languages, verbose_name='Язык')  # Язык карты: ru, en, etc.
    image = models.ImageField('Изображение')
    layout = models.IntegerChoices(enums.Layouts, verbose_name='Форматирование карты')  # Указание на нестандартность карты.

    #  Могут быть, а могут не быть:
    power = models.IntegerField('Сила', blank=True)
    toughness = models.IntegerField('Выносливость', blank=True)
    initial_loyalty = models.IntegerField('Стартовая верность', blank=True)

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'

    def __str__(self) -> str:
        return str(self.name)

class CardQuantified(models.Model):
    """
    Модель количества карт в коллекции или колоде.

    Лучше отделить собственно карту и объект в колоде.
    Правда, не уверен, что нужно ли делать это через ManyToManyField
    нарпрямую на карту с полем through и обнуляемыми внешними ключами
    (так как потребуется ссылка как на Deck, так и на Collection) или как здесь.
    Да и в чём разница?..
    """

    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    count = models.IntegerField()

    class Meta:
        verbose_name = 'Количество карт'
        verbose_name_plural = 'Количество карт'


class Collection(models.Model):
    """Модель коллекции."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')
    cards = models.ManyToManyField(CardQuantified)

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

    def __str__(self) -> str:
        return f'Коллекция карт {self.user}'


class Deck(models.Model):
    """Модель колоды."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField()
    description = models.TextField()
    cards = models.ManyToManyField(CardQuantified)

    class Meta:
        verbose_name = 'Колода'
        verbose_name_plural = 'Колоды'

    def __str__(self) -> str:
        return str(self.title)
