from enum import IntEnum, auto


class SuperTypes(IntEnum):
    BASIC = auto()
    LEGENDARY = auto()
    SNOWY = auto()


class Types(IntEnum):
    CREATURE = auto()
    LAND = auto()
    ENCHANTMENT = auto()
    INSTANT = auto()
    SORCERY = auto()
    PLANESWALKER = auto()
    ARTIFACT = auto()


class Languages(IntEnum):
    RU = auto()
    EN = auto()


class Rarity(IntEnum):
    COMMON = auto()
    UNCOMMON = auto()
    RARE = auto()
    MYTHIC = auto()


class Layouts(IntEnum):
    STANDART = auto()
    DOUBLE_SIDED = auto()
    DOUBLE = auto()
