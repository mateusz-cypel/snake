from models import Fruit


class ScoreHandler:
    def __init__(self):
        self._score: int = 0
        self._hi_score: int = 0

    @property
    def score(self) -> int:
        return self._score

    @property
    def hi_score(self) -> int:
        return self._hi_score

    def handle(self, fruit: Fruit) -> None:
        self._score += fruit.score
        self._hi_score = max(self._score, self._hi_score)

    def reset(self) -> None:
        self._score = 0
