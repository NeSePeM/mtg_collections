"""
Модели для приложения mtg_collections.

Приложение для создания коллекций и колод карт.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя."""


class Card(models.Model):
    """Модель карты."""

    #  Делать ли все эти поля ForeignKey?
    scryfall_id = models.UUIDField()
    title = models.CharField()  # Название. На английском можно считать primary key. Хотя у меня в основном русские карты.
    super_type = models.TextChoices()  # Супертип карты: базовый, легендарный, снежный.
    typee = models.TextChoices()  # Тип карты: creature, land, enchantment, instant, sorcery, planeswalker, artifact, etc.
    sub_type = models.CharField()
    text = models.TextField()
    mana_cost = models.CharField()  # Написано в формате {1}{W}{U}{B}{R}{G} - формат из Правил.
    sett = models.CharField()  # Название сета. Трёхбуквенный код.
    rarity = models.TextChoices()  # Редкость карты: common, uncommon, rare, mythic.
    foiled = models.BooleanField()
    language = models.TextChoices()  # Язык карты: ru, en, etc.
    image = models.ImageField()
    layout = models.TextChoices()  # Указание на нестандартность карты.

    #  Могут быть, а могут не быть:
    power = models.CharField()
    toughness = models.CharField()
    initial_loyalty = models.IntegerField()

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'

    def __str__(self):
        ...
    
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

    cards = models.ManyToManyField(CardQuantified)

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

    def __str__(self):
        ...


class Deck(models.Model):
    """Модель колоды."""

    name = models.CharField()
    description = models.TextField()
    cards = models.ManyToManyField(CardQuantified)

    class Meta:
        verbose_name = 'Колода'
        verbose_name_plural = 'Колоды'
    
    def __str__(self):
        ...