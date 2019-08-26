from enum import Enum, auto

class IceCream(Enum):
    VANILLA = 1
    CHOCOLATE = 2
    STRAWBERRY = 3
    MINT = 4

for icecream in IceCream:
    print(icecream)

class Suits(Enum):
    hearts = auto()
    spades = auto()
    clubs = auto()
    diamonds = auto()

for suit in Suits:
    print(suit)
    