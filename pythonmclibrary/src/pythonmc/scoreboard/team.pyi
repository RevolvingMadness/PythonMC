from src.pythonmc.scoreboard.rules.collision_rules import CollisionRules
from src.pythonmc.scoreboard.rules.visibility_rules import VisibilityRules
from src.pythonmc.server.text.formatting import Formatting
from src.pythonmc.server.text.text import Text


class Team:
    def setSuffix(self, suffix: Text) -> None:
        """
        Sets the suffix of the team.

        Args:
            suffix (Text): The suffix to set for the team.

        Returns:
            None
        """
    def setShowFriendlyInvisibles(self, showFriendlyInvisibles: bool) -> None:
        """
        Sets whether to show friendly invisibles for the team.

        Args:
            showFriendlyInvisibles (bool): A boolean value indicating whether to show friendly invisibles.

        Returns:
            None
        """
    def setPrefix(self, prefix: Text) -> None:
        """
        Sets the prefix of the team.

        Args:
            prefix (Text): The prefix to set for the team.

        Returns:
            None
        """
    def shouldShowFriendlyInvisibles(self) -> bool:
        """
        Checks if friendly invisibles are shown for the team.

        Returns:
            bool: True if friendly invisibles are shown, False otherwise.
        """
    def setNameTagVisibilityRule(self, nameTagVisibilityRule: VisibilityRules) -> None:
        """
        Sets the name tag visibility rule for the team.

        Args:
            nameTagVisibilityRule (VisibilityRules): The name tag visibility rule to set for the team.

        Returns:
            None
        """
    def setFriendlyFireAllowed(self, friendlyFireAllowed: bool) -> None:
        """
        Sets whether friendly fire is allowed for the team.

        Args:
            friendlyFireAllowed (bool): A boolean value indicating whether friendly fire is allowed.

        Returns:
            None
        """
    def setDisplayName(self, displayName: Text) -> None:
        """
        Sets the display name of the team.

        Args:
            displayName (Text): The display name to set for the team.

        Returns:
            None
        """
    def setDeathMessageVisibilityRule(
        self, deathMessageVisibilityRule: VisibilityRules
    ) -> None:
        """
        Sets the death message visibility rule for the team.

        Args:
            deathMessageVisibilityRule (VisibilityRules): The death message visibility rule to set for the team.

        Returns:
            None
        """
    def setColor(self, formatting: Formatting) -> None:
        """
        Sets the color of the team.

        Args:
            formatting (Formatting): The color formatting to set for the team.

        Returns:
            None
        """
    def setCollisionRule(self, collisionRule: CollisionRules) -> None:
        """
        Sets the collision rule for the team.

        Args:
            collisionRule (CollisionRules): The collision rule to set for the team.

        Returns:
            None
        """
    def isFriendlyFireAllowed(self) -> bool:
        """
        Checks if friendly fire is allowed for the team.

        Returns:
            bool: True if friendly fire is allowed, False otherwise.
        """
    def getSuffix(self) -> Text:
        """
        Returns the suffix of the team.

        Returns:
            Text: The suffix of the team.
        """
    def getPlayerList(self) -> list[str]:
        """
        Returns the list of players in the team.

        Returns:
            list[str]: The list of players in the team.
        """
    def getPrefix(self) -> Text:
        """
        Returns the prefix of the team.

        Returns:
            Text: The prefix of the team.
        """
    def getNameTagVisibilityRule(self) -> VisibilityRules:
        """
        Returns the name tag visibility rule of the team.

        Returns:
            VisibilityRules: The name tag visibility rule of the team.
        """
    def getName(self) -> str:
        """
        Returns the name of the team.

        Returns:
            str: The name of the team.
        """
    def getDisplayName(self) -> Text:
        """
        Returns the display name of the team.

        Returns:
            Text: The display name of the team.
        """
    def getDeathMessageVisibilityRule(self) -> VisibilityRules:
        """
        Returns the death message visibility rule of the team.

        Returns:
            VisibilityRules: The death message visibility rule of the team.
        """
    def getColor(self) -> Formatting:
        """
        Returns the color of the team.

        Returns:
            Formatting: The color of the team.
        """
    def getCollisionRule(self) -> CollisionRules:
        """
        Returns the collision rule of the team.

        Returns:
            CollisionRules: The collision rule of the team.
        """
