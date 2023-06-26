from numbers import Number
from typing import overload

from .time_ import Time
from .weather import Weather
from ..block.block_pos import BlockPos
from ..block.block_state import BlockState
from ..block.blocks import Blocks
from ..entity.entities import Entities
from ..player.player_entity import PlayerEntity
from ..server_.difficulty.difficulty import Difficulty
from ..world.position import Vec3d


class World:
    """
    Represents a world.
    """

    @overload
    def getBlock(self, x: Number, y: Number, z: Number) -> BlockState:
        """
        Retrieves the block state at the given coordinates.

        Args:
                x (Number): The x-coordinate of the block.
                y (Number): The y-coordinate of the block.
                z (Number): The z-coordinate of the block.

        Returns:
                BlockState: The block state at the given coordinates.
        """

    @overload
    def getBlock(self, blockPos: BlockPos) -> BlockState:
        """
        Retrieves the block state at the given block position.

        Args:
                blockPos (BlockPos): The block position.

        Returns:
                BlockState: The block state at the given block position.
        """

    @overload
    def getBlock(self, vec3d: Vec3d) -> BlockState:
        """
        Retrieves the block state at the given vector.

        Args:
                vec3d (Vec3d): The block position.

        Returns:
                BlockState: The block state at the given block position.
        """

    def getAllPlayers(self) -> list[PlayerEntity]:
        """
        Retrieves a list of all player entities in the game.

        Returns:
            A list of PlayerEntity objects representing all players in the game.
        """

    def getAllEntities(self) -> list[PlayerEntity]:
        """
        Retrieves a list of all entities in the game, including players and non-players.

        Returns:
            A list of PlayerEntity objects representing all entities in the game.
        """

    def getNearestPlayer(self, position: Vec3d) -> PlayerEntity:
        """
        Finds the nearest player entity to the specified position.

        Args:
            position (Vec3d): The position from which to search for the nearest player.

        Returns:
            The PlayerEntity object representing the nearest player to the specified position.
        """

    def getRandomPlayer(self) -> PlayerEntity:
        """
        Selects a random player entity from the game.

        Returns:
            A randomly chosen PlayerEntity object from the available players in the game.
        """

    def getDifficulty(self) -> Difficulty:
        """
        Retrieves the difficulty level of the world.

        Returns:
                Difficulty: The difficulty level of the world.
        """

    def getSeed(self) -> int:
        """
        Retrieves the seed value of the world.

        Returns:
                int: The seed value of the world.
        """

    @overload
    def setBlock(self, x: Number, y: Number, z: Number, block: Blocks) -> None:
        """
        Sets the block at the given coordinates.

        Args:
                x (Number): The x-coordinate of the block.
                y (Number): The y-coordinate of the block.
                z (Number): The z-coordinate of the block.
                block (Blocks): The block to be set.
        """

    @overload
    def setBlock(self, x: Number, y: Number, z: Number, block: BlockState) -> None:
        """
        Sets the block with the specified state at the given coordinates.

        Args:
                x (Number): The x-coordinate of the block.
                y (Number): The y-coordinate of the block.
                z (Number): The z-coordinate of the block.
                block (BlockState): The block state to be set.
        """

    @overload
    def setBlock(self, blockPos: BlockPos, block: Blocks) -> None:
        """
        Sets the block at the given block position.

        Args:
                blockPos (BlockPos): The block position.
                block (Blocks): The block to be set.
        """

    @overload
    def setBlock(self, blockPos: BlockPos, block: BlockState) -> None:
        """
        Sets the block with the specified state at the given block position.

        Args:
                blockPos (BlockPos): The block position.
                block (BlockState): The block state to be set.
        """

    @overload
    def setSpawnPos(self, x: Number, y: Number, z: Number) -> None:
        """
        Sets the spawn position of the world.

        Args:
                x (Number): The x-coordinate of the spawn position.
                y (Number): The y-coordinate of the spawn position.
                z (Number): The z-coordinate of the spawn position.
        """

    @overload
    def setSpawnPos(self, x: Number, y: Number, z: Number, angle: Number) -> None:
        """
        Sets the spawn position and angle of the world.

        Args:
                x (Number): The x-coordinate of the spawn position.
                y (Number): The y-coordinate of the spawn position.
                z (Number): The z-coordinate of the spawn position.
                angle (Number): The angle of the spawn position.
        """

    @overload
    def setSpawnPos(self, blockPos: BlockPos) -> None:
        """
        Sets the spawn position of the world using block position.

        Args:
                blockPos (BlockPos): The block position of the spawn position.
        """

    @overload
    def setSpawnPos(self, blockPos: BlockPos, angle: Number) -> None:
        """
        Sets the spawn position and angle of the world using block position.

        Args:
                blockPos (BlockPos): The block position of the spawn position.
                angle (Number): The angle of the spawn position.
        """

    def setTime(self, time: Time) -> None:
        """
        Sets the current time of the world.

        Args:
                time (Time): The time value to be set.
        """

    @overload
    def setWeather(self, weather: Weather) -> None:
        """
        Sets the weather condition of the world.

        Args:
                weather (Weather): The weather condition to be set.
        """

    @overload
    def setWeather(self, weather: Weather, duration: Number) -> None:
        """
        Sets the weather condition and duration of the world.

        Args:
                weather (Weather): The weather condition to be set.
                duration (Number): The duration of the weather condition.
        """

    @overload
    def spawnEntity(
            self, entity: Entities, x: Number, y: Number, z: Number, nbt: dict[str, object]
    ) -> None:
        """
        Spawns an entity at the specified coordinates.

        Args:
                entity (Entities): The type of entity to be spawned.
                x (Number): The x-coordinate of the entity's spawn location.
                y (Number): The y-coordinate of the entity's spawn location.
                z (Number): The z-coordinate of the entity's spawn location.
                nbt (dict[str, object]): Additional data for the entity (if applicable).
        """

    @overload
    def spawnEntity(
            self, entity: Entities, blockPos: BlockPos, nbt: dict[str, object]
    ) -> None:
        """
        Spawns an entity at the specified block position.

        Args:
                entity (Entities): The type of entity to be spawned.
                blockPos (BlockPos): The block position of the entity's spawn location.
                nbt (dict[str, object]): Additional data for the entity (if applicable).
        """
