from numbers import Number

from src.pythonmc.player.player_manager import PlayerManager
from src.pythonmc.scoreboard.scoreboard import Scoreboard
from src.pythonmc.server.difficulty.difficulties import Difficulties
from src.pythonmc.server.gamemode.game_mode import GameMode
from src.pythonmc.server.gamemode.game_modes import GameModes
from src.pythonmc.world.world import World
from src.pythonmc.world.worlds import Worlds


class Server:
	def getPlayerManager(self) -> PlayerManager:
		"""
		Retrieves the player manager for the server.

		Returns:
			PlayerManager: The player manager object.
		"""

	def getDefaultGameMode(self) -> GameMode:
		"""
		Retrieves the default game mode for new players.

		Returns:
			GameMode: The default game mode.
		"""

	def getForcedGameMode(self) -> GameMode:
		"""
		Retrieves the forced game mode for all players.

		Returns:
			GameMode: The forced game mode.
		"""

	def getScoreboard(self) -> Scoreboard:
		"""
		Retrieves the scoreboard for the server.

		Returns:
			Scoreboard: The scoreboard object.
		"""

	def getMaxWorldBorderRadius(self) -> int:
		"""
		Retrieves the maximum radius of the world border.

		Returns:
			int: The maximum world border radius.
		"""

	def getServerIP(self) -> str:
		"""
		Retrieves the IP address of the server.

		Returns:
			str: The server IP address.
		"""

	def getWorld(self, world: Worlds) -> World:
		"""
		Retrieves the world object for the specified world type.

		Args:
			world (Worlds): The type of the world to retrieve.

		Returns:
			World: The world object.
		"""

	def getServerMOTD(self) -> str:
		"""
		Retrieves the MOTD (Message of the Day) of the server.

		Returns:
			str: The server MOTD.
		"""

	def getServerPort(self) -> int:
		"""
		Retrieves the port number on which the server is running.

		Returns:
			int: The server port number.
		"""

	def getSpawnProtectionRadius(self) -> int:
		"""
		Retrieves the radius of spawn protection around the world spawn point.

		Returns:
			int: The spawn protection radius.
		"""

	def getSpawnRadius(self, world: Worlds) -> int:
		"""
		Retrieves the spawn radius for the specified world type.

		Args:
			world (Worlds): The type of the world to retrieve the spawn radius for.

		Returns:
			int: The spawn radius of the world.
		"""

	def getVersion(self) -> str:
		"""
		Retrieves the version of the server.

		Returns:
			str: The server version.
		"""

	def isFlightEnabled(self) -> bool:
		"""
		Checks if flight is enabled on the server.

		Returns:
			bool: True if flight is enabled, False otherwise.
		"""

	def isHardcore(self) -> bool:
		"""
		Checks if the server is in hardcore mode.

		Returns:
			bool: True if the server is in hardcore mode, False otherwise.
		"""

	def isMonsterSpawningEnabled(self) -> bool:
		"""
		Checks if monster spawning is enabled on the server.

		Returns:
			bool: True if monster spawning is enabled, False otherwise.
		"""

	def isNetherAllowed(self) -> bool:
		"""
		Checks if the Nether dimension is allowed on the server.

		Returns:
			bool: True if the Nether is allowed, False otherwise.
		"""

	def isPVPEnabled(self) -> bool:
		"""
		Checks if PVP (Player vs. Player) is enabled on the server.

		Returns:
			bool: True if PVP is enabled, False otherwise.
		"""

	def isSingleplayer(self) -> bool:
		"""
		Checks if the server is running in singleplayer mode.

		Returns:
			bool: True if the server is in singleplayer mode, False otherwise.
		"""

	def openToLAN(self, gameMode: GameModes, cheatsAllowed: bool, port: Number) -> None:
		"""
		Opens the server to LAN (Local Area Network) with the specified settings.

		Args:
			gameMode (GameModes): The game mode for LAN players.
			cheatsAllowed (bool): Whether cheats are allowed for LAN players.
			port (Number): The port number to use for LAN connections.

		Returns:
			None
		"""

	def setDefaultGameMode(self, defaultGameMode: GameModes) -> None:
		"""
		Sets the default game mode for new players.

		Args:
			defaultGameMode (GameModes): The default game mode to set.

		Returns:
			None
		"""

	def setDifficulty(self, difficulty: Difficulties) -> None:
		"""
		Sets the difficulty level of the server.

		Args:
			difficulty (Difficulties): The difficulty level to set.

		Returns:
			None
		"""

	def setDifficultyLocked(self, difficultyLocked: bool) -> None:
		"""
		Sets whether the difficulty level is locked on the server.

		Args:
			difficultyLocked (bool): True to lock the difficulty level, False otherwise.

		Returns:
			None
		"""
