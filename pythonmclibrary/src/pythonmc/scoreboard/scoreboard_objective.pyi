from src.pythonmc.scoreboard.render_types import RenderTypes
from src.pythonmc.scoreboard.scoreboard_criterions import ScoreboardCriterions
from src.pythonmc.server.text.text import Text


class ScoreboardObjective:
	def getCriterion(self) -> ScoreboardCriterions:
		"""
		Retrieves the criterion type of the scoreboard objective.

		Returns:
			ScoreboardCriterions: The criterion type of the objective.
		"""

	def getDisplayName(self) -> Text:
		"""
		Retrieves the display name of the scoreboard objective.

		Returns:
			Text: The display name of the objective.
		"""

	def getName(self) -> str:
		"""
		Retrieves the name of the scoreboard objective.

		Returns:
			str: The name of the objective.
		"""

	def getRenderType(self) -> RenderTypes:
		"""
		Retrieves the render type of the scoreboard objective.

		Returns:
			RenderTypes: The render type of the objective.
		"""

	def setDisplayName(self, displayName: Text) -> None:
		"""
		Sets the display name of the scoreboard objective.

		Args:
			displayName (Text): The display name to set.

		Returns:
			None
		"""

	def setRenderType(self, renderType: RenderTypes) -> None:
		"""
		Sets the render type of the scoreboard objective.

		Args:
			renderType (RenderTypes): The render type to set.

		Returns:
			None
		"""
