from typing import overload

from src.pythonmc.player.player_entity import PlayerEntity
from src.pythonmc.server.text.text import Text


class PlayerManager:
    """
    Manages players in the game.
    """

    def areCheatsAllowed(self) -> bool:
        """
        Checks if cheats are allowed in the game.

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
        Disconnects all players from the game.
        """
    def getCurrentPlayerCount(self) -> int:
        """
        Retrieves the current count of players in the game.

        Returns:
            int: The current count of players.
        """
    def getMaxPlayerCount(self) -> int:
        """
        Retrieves the maximum allowed count of players in the game.

        Returns:
            int: The maximum allowed count of players.
        """
    def getOpNames(self) -> list[str]:
        """
        Retrieves the names of all operators (ops) in the game.

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
        Retrieves a list of all player entities in the game.

        Returns:
            list[PlayerEntity]: A list of player entities.
        """
    def getPlayerNames(self) -> list[str]:
        """
        Retrieves the names of all players in the game.

        Returns:
            list[str]: The names of all players.
        """
    def getViewDistance(self) -> int:
        """
        Retrieves the view distance setting of the game.

        Returns:
            int: The view distance.
        """
    def getWhitelistedNames(self) -> list[str]:
        """
        Retrieves the names of all whitelisted players in the game.

        Returns:
            list[str]: The names of all whitelisted players.
        """
    def isWhitelistEnabled(self) -> bool:
        """
        Checks if the whitelist is enabled in the game.

        Returns:
            bool: True if the whitelist is enabled, False otherwise.
        """
    def reloadWhitelist(self) -> None:
        """
        Reloads the whitelist configuration.
        """
    def setCheatsAllowed(self, cheatsAllowed: bool) -> None:
        """
        Sets whether cheats are allowed in the game.

        Args:
            cheatsAllowed (bool): True to allow cheats, False to disallow cheats.
        """
    def setSimulationDistance(self, simulationDistance: int) -> None:
        """
        Sets the simulation distance of the game.

        Args:
            simulationDistance (int): The simulation distance value.
        """
    def setViewDistance(self, viewDistance: int) -> None:
        """
        Sets the view distance of the game.

        Args:
            viewDistance (int): The view distance value.
        """
    def setWhitelistEnabled(self, whitelistEnabled: bool) -> None:
        """
        Sets whether the whitelist is enabled in the game.

        Args:
            whitelistEnabled (bool): True to enable the whitelist, False to disable the whitelist.
        """
