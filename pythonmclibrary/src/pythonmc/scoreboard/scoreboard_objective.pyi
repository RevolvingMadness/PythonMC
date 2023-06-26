from .render_types import RenderTypes
from .scoreboard_criterions import ScoreboardCriterions
from ..server_.text.text import Text


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
        """

    def setRenderType(self, renderType: RenderTypes) -> None:
        """
        Sets the render type of the scoreboard objective.

        Args:
                renderType (RenderTypes): The render type to set.
        """
