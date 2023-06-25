from numbers import Number

from src.pythonmc.block.block_state import BlockState
from src.pythonmc.block.blocks import Blocks
from src.pythonmc.entity.arm import Arm
from src.pythonmc.entity.entity import Entity
from src.pythonmc.entity.living_entity import LivingEntity
from src.pythonmc.player.ender_chest_inventory import EnderChestInventory
from src.pythonmc.player.hunger_manager import HungerManager
from src.pythonmc.player.player_inventory import PlayerInventory


class PlayerEntity(LivingEntity):
	def addExhaustion(self, exhaustion: Number) -> None:
		"""
        Increases the exhaustion level of the player.

        Args:
                exhaustion (Number): The amount of exhaustion to add.
        """

	def addExperience(self, experience: Number) -> None:
		"""
        Adds experience points to the player.

        Args:
                experience (Number): The number of experience points to add.
        """

	def addExperienceLevels(self, levels: Number) -> None:
		"""
        Adds experience levels to the player.

        Args:
                levels (Number): The number of levels to add.
        """

	def addScore(self, score: Number) -> None:
		"""
        Adds a score value to the player.

        Args:
                score (Number): The score value to add.
        """

	def addShoulderEntity(self, entityNbt: dict[str, object]) -> None:
		"""
        Adds an entity to the player's shoulder.

        Args:
                entityNbt (dict[str, object]): The NBT data of the entity to add.
        """

	def attack(self, entity: Entity) -> None:
		"""
        Attacks the specified entity.

        Args:
                entity (Entity): The entity to attack.
        """

	def canConsume(self, ignoreHunger: bool) -> bool:
		"""
        Checks if the player can consume items.

        Args:
                ignoreHunger (bool): Whether to ignore hunger level when checking.

        Returns:
                bool: True if the player can consume items, False otherwise.
        """

	def canFoodHeal(self) -> bool:
		"""
        Checks if the player can heal using food.

        Returns:
                bool: True if the player can heal with food, False otherwise.
        """

	def canHarvest(self, block: Blocks | BlockState) -> bool:
		"""
        Checks if the player can harvest the specified block.

        Args:
                block (Union[Blocks, BlockState]): The block to check.

        Returns:
                bool: True if the player can harvest the block, False otherwise.
        """

	def checkFallFlying(self) -> bool:
		"""
        Checks if the player can use elytra to fall with reduced speed.

        Returns:
                bool: True if the player can fall flying, False otherwise.
        """

	def disableShield(self, sprinting: bool) -> None:
		"""
        Disables the player's shield.

        Args:
                sprinting (bool): Whether the player is sprinting.
        """

	def getAttackCooldownProgress(self, baseTime: Number) -> float:
		"""
        Calculates the progress of the attack cooldown.

        Args:
                baseTime (Number): The base time for the attack cooldown.

        Returns:
                float: The progress of the attack cooldown as a value between 0.0 and 1.0.
        """

	def getEnderChestInventory(self) -> EnderChestInventory:
		"""
        Retrieves the ender chest inventory of the player.

        Returns:
                EnderChestInventory: The ender chest inventory of the player.
        """

	def getHungerManager(self) -> HungerManager:
		"""
        Retrieves the hunger manager of the player.

        Returns:
                HungerManager: The hunger manager of the player.
        """

	def getInventory(self) -> PlayerInventory:
		"""
        Retrieves the inventory of the player.

        Returns:
                PlayerInventory: The inventory of the player.
        """

	def getShoulderEntityLeft(self) -> dict[str, object]:
		"""
        Retrieves the entity data on the player's left shoulder.

        Returns:
                dict[str, object]: The NBT data of the entity on the left shoulder.
        """

	def getShoulderEntityRight(self) -> dict[str, object]:
		"""
        Retrieves the entity data on the player's right shoulder.

        Returns:
                dict[str, object]: The NBT data of the entity on the right shoulder.
        """

	def isCreative(self) -> bool:
		"""
        Checks if the player is in creative mode.

        Returns:
                bool: True if the player is in creative mode, False otherwise.
        """

	def isMainPlayer(self) -> bool:
		"""
        Checks if the player is the main player.

        Returns:
                bool: True if the player is the main player, False otherwise.
        """

	def isUsingSglass(self) -> bool:
		"""
        Checks if the player is using a spyglass.

        Returns:
                bool: True if the player is using a spyglass, False otherwise.
        """

	def requestRespawn(self) -> None:
		"""
        Requests the player to respawn.
        """

	def sendMessage(self, message: str) -> None:
		"""
        Sends a message to the player.

        Args:
                message: The message to send.
        """

	def setMainArm(self, arm: Arm) -> None:
		"""
        Sets the player's main arm.

        Args:
                arm (Arm): The main arm to set.
        """
