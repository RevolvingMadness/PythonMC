from numbers import Number
from typing import overload

from src.pythonmc.scoreboard.scoreboard import Scoreboard


class ScoreboardPlayerScore:
	def clearScore(self) -> None:
		"""
        Clears the score of the player.
        """

	def getPlayerName(self) -> str:
		"""
        Retrieves the name of the player associated with the score.

        Returns:
                str: The name of the player.
        """

	def getScore(self) -> int:
		"""
        Retrieves the score value.

        Returns:
                int: The score value.
        """

	def getScoreboard(self) -> Scoreboard:
		"""
        Retrieves the scoreboard associated with the score.

        Returns:
                Scoreboard: The associated scoreboard object.
        """

	@overload
	def incrementScore(self) -> None:
		"""
        Increments the score value by 1.
        """

	@overload
	def incrementScore(self, amount: Number) -> None:
		"""
        Increments the score value by the specified amount.

        Args:
                amount (Number): The amount to increment the score by.
        """

	def setScore(self, score: Number) -> None:
		"""
        Sets the score value.

        Args:
                score (Number): The score value to set.
        """
