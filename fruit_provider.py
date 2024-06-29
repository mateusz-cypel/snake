import random

from models import Fruit, Apple, Orange, Strawberry

APPLE_SCORE = 5
APPLE_ENERGY = 5

ORANGE_SCORE = 5
ORANGE_ENERGY = 5

STRAWBERRY_SCORE = 5
STRAWBERRY_ENERGY = 5

APPLE_DROP_RATE = 70
ORANGE_DROP_RATE = 20
STRAWBERRY_DROP_RATE = 10
DROP_RATES = [
    APPLE_DROP_RATE, ORANGE_DROP_RATE, STRAWBERRY_DROP_RATE
]


class FruitProvider:
    def __init__(self):
        self.drop_rates_sum = sum(DROP_RATES)

    def get(self):
        rand_int = random.randint(0, self.drop_rates_sum - 1)
        if rand_int < APPLE_DROP_RATE:
            return Apple(
                score=APPLE_SCORE,
                energy=APPLE_ENERGY,
            )
        if rand_int < APPLE_DROP_RATE + ORANGE_DROP_RATE:
            return Orange(
                score=ORANGE_SCORE,
                energy=ORANGE_ENERGY,
            )
        return Strawberry(
            score=STRAWBERRY_SCORE,
            energy=STRAWBERRY_ENERGY,
        )
