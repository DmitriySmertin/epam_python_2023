"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.

from enum import Enum


class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"


class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"


Should become:

class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""

class SimplifiedEnum(type):

    def __new__(mcs, name, bases, dct):
        cls_instance = super().__new__(mcs, name, bases, dct)
        for key in cls_instance._keys:
            setattr(cls_instance, key, key)
        return cls_instance

    def __prepare__(cls, bases, **kwargs):
        keys = kwargs.get("_keys", ())
        return {k: k for k in keys}

class ColorsEnum(metaclass=SimplifiedEnum):
    _keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    _keys = ("XL", "L", "M", "S", "XS")

assert ColorsEnum.RED == "RED"