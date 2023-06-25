from typing import overload


class ScoreboardPlayerScore:
    def clearScore(self):
        ...

    def getPlayerName(self):
        ...

    def getScore(self):
        ...

    def getScoreboard(self):
        ...

    @overload
    def incrementScore(self):
        ...

    @overload
    def incrementScore(self, amount):
        ...

    def setScore(self, score):
        ...
