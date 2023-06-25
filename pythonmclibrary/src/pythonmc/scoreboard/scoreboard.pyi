from src.pythonmc.entity.entity import Entity
from src.pythonmc.scoreboard.render_types import RenderTypes
from src.pythonmc.scoreboard.scoreboard_criterions import ScoreboardCriterions
from src.pythonmc.scoreboard.scoreboard_objective import ScoreboardObjective
from src.pythonmc.scoreboard.scoreboard_player_score import ScoreboardPlayerScore
from src.pythonmc.scoreboard.team import Team
from src.pythonmc.server.text.text import Text

class Scoreboard:
    def getTeams(self) -> list[Team]:
        """
        Retrieves a list of all teams on the scoreboard.

        Returns:
                list[Team]: A list of all teams on the scoreboard.
        """

    def resetPlayerScore(self, playerName: str, objective: ScoreboardObjective) -> None:
        """
        Resets the score of a player for the specified objective.

        Args:
                playerName (str): The name of the player.
                objective (ScoreboardObjective): The objective to reset the player's score for.
        """

    def getAllPlayerScores(
            self, objective: ScoreboardObjective
    ) -> list[ScoreboardPlayerScore]:
        """
        Retrieves a list of all player scores for the specified objective.

        Args:
                objective (ScoreboardObjective): The objective to retrieve player scores for.

        Returns:
                list[ScoreboardPlayerScore]: A list of all player scores for the objective.
        """

    def removeTeam(self, team: Team) -> None:
        """
        Removes the specified team from the scoreboard.

        Args:
                team (Team): The team to remove.
        """

    def containsObjective(self, name: str) -> bool:
        """
        Checks if an objective with the specified name exists in the scoreboard.

        Args:
                name (str): The name of the objective.

        Returns:
                bool: True if the objective exists, False otherwise.
        """

    def addObjective(
            self,
            name: str,
            criterion: ScoreboardCriterions,
            displayName: Text,
            renderType: RenderTypes,
    ) -> None:
        """
        Adds a new objective to the scoreboard.

        Args:
                name (str): The name of the objective.
                criterion (ScoreboardCriterions): The criterion type of the objective.
                displayName (Text): The display name of the objective.
                renderType (RenderTypes): The render type of the objective.
        """

    def removePlayerFromTeam(self, playerName: str, team: Team) -> None:
        """
        Removes a player from the specified team.

        Args:
                playerName (str): The name of the player.
                team (Team): The team to remove the player from.
        """

    def getObjectives(self) -> list[ScoreboardObjective]:
        """
        Retrieves a list of all objectives on the scoreboard.

        Returns:
                list[ScoreboardObjective]: A list of all objectives on the scoreboard.
        """

    def addPlayerToTeam(self, playerName: str, team: Team) -> None:
        """
        Adds a player to the specified team.

        Args:
                playerName (str): The name of the player.
                team (Team): The team to add the player to.
        """

    def clearPlayerTeam(self, playerName: str) -> None:
        """
        Clears the team association of a player.

        Args:
                playerName (str): The name of the player.
        """

    def getObjectiveNames(self) -> list[str]:
        """
        Retrieves a list of names from all the objectives on the scoreboard.

        Returns:
                list[str]: A list of names from all the objectives on the scoreboard.
        """

    def getTeam(self, name: str) -> Team:
        """
        Retrieves the team with the specified name.

        Args:
                name (str): The name of the team.

        Returns:
                Team: The team object.
        """

    def resetEntityScore(self, entity: Entity) -> None:
        """
        Resets the score of an entity on all objectives.

        Args:
                entity (Entity): The entity.
        """

    def getObjective(self, name: str) -> ScoreboardObjective:
        """
        Retrieves the objective with the specified name.

        Args:
                name (str): The name of the objective.

        Returns:
                ScoreboardObjective: The objective object.
        """

    def addTeam(self, name: str) -> None:
        """
        Adds a new team to the scoreboard.

        Args:
                name (str): The name of the team.
        """

    def getTeamNames(self) -> list[str]:
        """
        Retrieves a list of names from all the teams on the scoreboard.

        Returns:
                list[str]: A list of names from all the teams on the scoreboard.
        """

    def removeObjective(self, objective: ScoreboardObjective) -> None:
        """
        Removes the specified objective from the scoreboard.

        Args:
                objective (ScoreboardObjective): The objective to remove.
        """

    def getPlayerScore(
            self, name: str, objective: ScoreboardObjective
    ) -> ScoreboardPlayerScore:
        """
        Retrieves the score of a player for the specified objective.

        Args:
                name (str): The name of the player.
                objective (ScoreboardObjective): The objective to retrieve the player's score for.

        Returns:
                ScoreboardPlayerScore: The player's score for the objective.
        """

    def getPlayerTeam(self, name: str) -> Team:
        """
        Retrieves the team associated with the specified player.

        Args:
                name (str): The name of the player.

        Returns:
                Team: The associated team object.
        """
