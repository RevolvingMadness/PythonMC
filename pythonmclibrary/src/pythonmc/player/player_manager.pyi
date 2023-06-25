from pythonmc.player.player_entity import PlayerEntity
from pythonmc.server.text.text import Text
from typing import overload


class PlayerManager:
    """
    Manages players.
    """

    def areCheatsAllowed(self) -> bool:
        """
        Checks if cheats are allowed.

        Returns:
                bool: True if cheats are allowed, False otherwise.
        """

    @overload
    def broadcast(self, message: str) -> None:
        """
        Broadcasts a message to all players.

        Args:
                message (str): The message to broadcast.
        """

    @overload
    def broadcast(self, text: Text) -> None:
        """
        Broadcasts a text component to all players.

        Args:
                text (Text): The text component to broadcast.
        """

    def disconnectAllPlayers(self) -> None:
        """
        Disconnects all players.
        """

    def getCurrentPlayerCount(self) -> int:
        """
        Retrieves the current count of players.

        Returns:
                int: The current count of players.
        """

    def getMaxPlayerCount(self) -> int:
        """
        Retrieves the maximum allowed count of players.

        Returns:
                int: The maximum allowed count of players.
        """

    def getOpNames(self) -> list[str]:
        """
        Retrieves the names of all operators.

        Returns:
                list[str]: The names of all operators.
        """

    def getPlayer(self, name: str) -> PlayerEntity:
        """
        Retrieves the player entity with the specified name.

        Args:
                name (str): The name of the player.

        Returns:
                PlayerEntity: The player entity.
        """

    def getPlayerList(self) -> list[PlayerEntity]:
        """
        Retrieves a list of all player entities.

        Returns:
                list[PlayerEntity]: A list of player entities.
        """

    def getPlayerNames(self) -> list[str]:
        """
        Retrieves the names of all players.

        Returns:
                list[str]: The names of all players.
        """

    def getViewDistance(self) -> int:
        """
        Retrieves the view distance setting.

        Returns:
                int: The view distance.
        """

    def getWhitelistedNames(self) -> list[str]:
        """
        Retrieves the names of all whitelisted players.

        Returns:
                list[str]: The names of all whitelisted players.
        """

    def isWhitelistEnabled(self) -> bool:
        """
        Checks if the whitelist is enabled.

        Returns:
                bool: True if the whitelist is enabled, False otherwise.
        """

    def reloadWhitelist(self) -> None:
        """
        Reloads the whitelist configuration.
        """

    def setCheatsAllowed(self, cheatsAllowed: bool) -> None:
        """
        Sets whether cheats are allowed.

        Args:
                cheatsAllowed (bool): True to allow cheats, False to disallow cheats.
        """

    def setSimulationDistance(self, simulationDistance: int) -> None:
        """
        Sets the simulation distance.

        Args:
                simulationDistance (int): The simulation distance value.
        """

    def setViewDistance(self, viewDistance: int) -> None:
        """
        Sets the view distance.

        Args:
                viewDistance (int): The view distance value.
        """

    def setWhitelistEnabled(self, whitelistEnabled: bool) -> None:
        """
        Sets whether the whitelist is enabled.

        Args:
                whitelistEnabled (bool): True to enable the whitelist, False to disable the whitelist.
        """
