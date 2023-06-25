from pythonmc.entity.entity import Entity
from pythonmc.player.player_entity import PlayerEntity
from pythonmc.server.text.text import Text
from pythonmc.world.position.vec2f import Vec2f
from pythonmc.world.position.vec3d import Vec3d
from pythonmc.world.world import World
from typing import overload


class Executor:
    """
    Attributes:
            name (str): The name of the executor.
            displayName (str): The display name of the executor.
            position (Vec3d): The position of the executor.
            player (PlayerEntity): The player entity associated with the executor.
            world (World): The world in which the executor exists.
            entity (Entity): The entity associated with the executor.
            isExecutedByPlayer (bool): Indicates if the executor is executed by a player.
            rotation (Vec2f): The rotation of the executor.
    """

    name: str
    displayName: str
    position: Vec3d
    player: PlayerEntity
    world: World
    entity: Entity
    isExecutedByPlayer: bool
    rotation: Vec2f

    @overload
    def sendMessage(self, message) -> None:
        """
        Sends a message to the executor.

        Args:
                message: The message to send.
        """

    @overload
    def sendError(self, error) -> None:
        """
        Sends an error message to the executor.

        Args:
                error: The error message to send.
        """

    @overload
    def sendMessage(self, text: Text) -> None:
        """
        Sends a text message to the executor.

        Args:
                text (Text): The text message to send.
        """

    @overload
    def sendError(self, text: Text) -> None:
        """
        Sends an error text message to the executor.

        Args:
                text (Text): The error text message to send.
        """
