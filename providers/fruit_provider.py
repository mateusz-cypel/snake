import random

from models import Apple, Orange, Strawberry
from settings import settings

DROP_RATES = [
    settings.fruit.apple.drop_rate,
    settings.fruit.orange.drop_rate,
    settings.fruit.strawberry.drop_rate,
]


class FruitProvider:
    def __init__(self):
        self.drop_rates_sum = sum(DROP_RATES)

    def get(self):
        rand_int = random.randint(0, self.drop_rates_sum - 1)
        if rand_int < settings.fruit.apple.drop_rate:
            return Apple(
                score=settings.fruit.apple.score,
                energy=settings.fruit.apple.energy,
            )
        if rand_int < settings.fruit.apple.drop_rate + settings.fruit.orange.drop_rate:
            return Orange(
                score=settings.fruit.orange.score,
                energy=settings.fruit.orange.energy,
            )
        return Strawberry(
            score=settings.fruit.strawberry.score,
            energy=settings.fruit.strawberry.energy,
        )
