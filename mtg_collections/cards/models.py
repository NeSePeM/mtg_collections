from django.contrib.auth.models import AbstractUser
from django.db import models
from cards.enums_for_model import (
    SuperTypes, Types, Languages, Rarity, Layouts
)


class User(AbstractUser):
    """Модель пользователя."""


class CardFace(models.Model):
    """Сторона карты."""

    name = models.CharField('Имя', max_length=255)
    # ... остальные поля ... нужно относледоваться будет вместе с Card

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'

    def __str__(self) -> str:
        return self.name


class Card(models.Model):
    """Модель карты."""

    scryfall_id = models.UUIDField('Идентификатор карты', primary_key=True)
    oracle_id = models.UUIDField('Идентификатор идентичности карты')
    name = models.CharField('Имя', max_length=255)
    super_type = models.IntegerField(
        'Супертип карты',
        choices=SuperTypes.choices,
        default=SuperTypes.BASIC
    )
    typee = models.IntegerField(
        'Тип карты',
        choices=Types.choices,
        default=Types.CREATURE
    )
    sub_type = models.CharField('Подтип', max_length=255)
    text = models.TextField('Текст карты')
    mana_cost = models.CharField('Мана-стоимость', max_length=255)
    sett = models.CharField('Выпуск', max_length=255)
    rarity = models.IntegerField(
        'Редкость',
        choices=Rarity.choices,
        default=Rarity.COMMON
    )
    foiled = models.BooleanField('Фольгированная', default=False)
    language = models.IntegerField(
        'Язык карты',
        choices=Languages.choices,
        default=Languages.RU
    )
    image = models.ImageField('Изображение')
    layout = models.IntegerField(
        'Макет карты',
        choices=Layouts.choices,
        default=Layouts.STANDARD
    )
    card_faces = models.ManyToManyField(CardFace)

    power = models.IntegerField('Сила', blank=True, null=True)
    toughness = models.IntegerField('Выносливость', blank=True, null=True)
    initial_loyalty = models.IntegerField('Стартовая верность', blank=True, null=True)

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'

    def __str__(self) -> str:
        return self.name


class CardQuantified(models.Model):
    """
    Модель количества карт в коллекции или колоде.
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
        return f'Коллекция {self.user.username}'


class Deck(models.Model):
    """Модель колоды."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    cards = models.ManyToManyField(CardQuantified)

    class Meta:
        verbose_name = 'Колода'
        verbose_name_plural = 'Колоды'

    def __str__(self) -> str:
        return self.title
