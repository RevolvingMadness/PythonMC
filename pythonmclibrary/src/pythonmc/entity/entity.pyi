from numbers import Number

from src.pythonmc.block.block_pos import BlockPos
from src.pythonmc.entity.damage_sources import DamageSources
from src.pythonmc.entity.entities import Entities
from src.pythonmc.item.item_stack import ItemStack
from src.pythonmc.world.position.vec3d import Vec3d
from src.pythonmc.world.world import World


class Entity:
	def __init__(self, entity: Entities, world: World) -> None:
		"""
		Initializes a new entity with the specified entity type and world.

		Args:
			entity: The type of entity.
			world: The world the entity belongs to.
		"""

	def addVelocity(self, velocity: Vec3d) -> None:
		"""
		Adds velocity to the entity.

		Args:
			velocity: The velocity to add to the entity.
		"""

	def canFreeze(self) -> bool:
		"""
		Checks if the entity can freeze.

		Returns:
			True if the entity can freeze, False otherwise.
		"""

	def canUsePortals(self) -> bool:
		"""
		Checks if the entity can use portals.

		Returns:
			True if the entity can use portals, False otherwise.
		"""

	def collidesWith(self, entity: Entity) -> bool:
		"""
		Checks if the entity collides with another entity.

		Args:
			entity: The entity to check collision with.

		Returns:
			True if the entity collides with the specified entity, False otherwise.
		"""

	def damage(self, damageSource: DamageSources, amount: Number) -> None:
		"""
		Damages the entity by the specified amount using the given damage source.

		Args:
			damageSource: The source of the damage.
			amount: The amount of damage to inflict.
		"""

	def dismountVehicle(self) -> None:
		"""
		Dismounts the entity from its current vehicle.
		"""

	def distanceTo(self, entity: Entity) -> float:
		"""
		Calculates the distance to another entity.

		Args:
			entity: The entity to calculate the distance to.

		Returns:
			The distance to the specified entity.
		"""

	def extinguish(self) -> None:
		"""
		Extinguishes the entity.
		"""

	def extinguishWithSound(self) -> None:
		"""
		Extinguishes the entity with a sound effect.
		"""

	def getArmorItems(self) -> list[ItemStack]:
		"""
		Returns a list of armor items worn by the entity.

		Returns:
			A list of ItemStack objects representing the armor items.
		"""

	def getBlockPos(self) -> BlockPos:
		"""
		Returns the block position of the entity.

		Returns:
			The BlockPos object representing the block position.
		"""

	def getCommandTags(self) -> list[str]:
		"""
		Returns a list of command tags associated with the entity.

		Returns:
			A list of strings representing the command tags.
		"""

	def getCustomName(self) -> str:
		"""
		Returns the custom name of the entity.

		Returns:
			The custom name of the entity as a string.
		"""

	def getDisplayName(self) -> str:
		"""
		Returns the display name of the entity.

		Returns:
			The display name of the entity as a string.
		"""

	def getHandItems(self) -> list[ItemStack]:
		"""
		Returns a list of items held in the entity's hands.

		Returns:
			A list of ItemStack objects representing the held items.
		"""

	def getName(self) -> str:
		"""
		Returns the name of the entity.

		Returns:
			The name of the entity as a string.
		"""

	def getPosition(self) -> Vec3d:
		"""
		Returns the position of the entity.

		Returns:
			The position of the entity as a Vec3d object.
		"""

	def getVehicle(self) -> Entity:
		"""
		Returns the vehicle that the entity is riding.

		Returns:
			The vehicle entity that the entity is riding, or None if not riding any vehicle.
		"""

	def getVelocity(self) -> Vec3d:
		"""
		Returns the velocity of the entity.

		Returns:
			The velocity of the entity as a Vec3d object.
		"""

	def getX(self) -> float:
		"""
		Returns the X-coordinate of the entity's position.

		Returns:
			The X-coordinate of the entity's position as a float.
		"""

	def getY(self) -> float:
		"""
		Returns the Y-coordinate of the entity's position.

		Returns:
			The Y-coordinate of the entity's position as a float.
		"""

	def getZ(self) -> float:
		"""
		Returns the Z-coordinate of the entity's position.

		Returns:
			The Z-coordinate of the entity's position as a float.
		"""

	def hasCustomName(self) -> bool:
		"""
		Checks if the entity has a custom name.

		Returns:
			True if the entity has a custom name, False otherwise.
		"""

	def hasNoGravity(self) -> bool:
		"""
		Checks if the entity has no gravity.

		Returns:
			True if the entity has no gravity, False otherwise.
		"""

	def hasPassenger(self, entity: Entity) -> bool:
		"""
		Checks if the entity has the specified entity as a passenger.

		Args:
			entity: The entity to check for as a passenger.

		Returns:
			True if the entity has the specified entity as a passenger, False otherwise.
		"""

	def hasPassengers(self) -> bool:
		"""
		Checks if the entity has any passengers.

		Returns:
			True if the entity has passengers, False otherwise.
		"""

	def hasPermissionLevel(self, level: Number) -> bool:
		"""
		Checks if the entity has the specified permission level.

		Args:
			level: The permission level to check.

		Returns:
			True if the entity has the specified permission level, False otherwise.
		"""

	def hasPortalCooldown(self) -> bool:
		"""
		Checks if the entity has a portal cooldown.

		Returns:
			True if the entity has a portal cooldown, False otherwise.
		"""

	def hasVehicle(self) -> bool:
		"""
		Checks if the entity is riding a vehicle.

		Returns:
			True if the entity is riding a vehicle, False otherwise.
		"""

	def isAlive(self) -> bool:
		"""
		Checks if the entity is alive.

		Returns:
			True if the entity is alive, False otherwise.
		"""

	def isCollidable(self) -> bool:
		"""
		Checks if the entity is collidable.

		Returns:
			True if the entity is collidable, False otherwise.
		"""

	def isCrawling(self) -> bool:
		"""
		Checks if the entity is crawling.

		Returns:
			True if the entity is crawling, False otherwise.
		"""

	def isCustomNameVisible(self) -> bool:
		"""
		Checks if the entity's custom name is visible.

		Returns:
			True if the entity's custom name is visible, False otherwise.
		"""

	def isDead(self) -> bool:
		"""
		Checks if the entity is dead.

		Returns:
			True if the entity is dead, False otherwise.
		"""

	def isInLava(self) -> bool:
		"""
		Checks if the entity is in lava.

		Returns:
			True if the entity is in lava, False otherwise.
		"""

	def isInRain(self) -> bool:
		"""
		Checks if the entity is in rain.

		Returns:
			True if the entity is in rain, False otherwise.
		"""

	def isInsidePortal(self) -> bool:
		"""
		Checks if the entity is inside a portal.

		Returns:
			True if the entity is inside a portal, False otherwise.
		"""

	def isInsideWater(self) -> bool:
		"""
		Checks if the entity is inside water.

		Returns:
			True if the entity is inside water, False otherwise.
		"""

	def isOnGround(self) -> bool:
		"""
		Checks if the entity is on the ground.

		Returns:
			True if the entity is on the ground, False otherwise.
		"""

	def isSpectator(self) -> bool:
		"""
		Checks if the entity is a spectator.

		Returns:
			True if the entity is a spectator, False otherwise.
		"""

	def isSubmergedInWater(self) -> bool:
		"""
		Checks if the entity is submerged in water.

		Returns:
			True if the entity is submerged in water, False otherwise.
		"""

	def isVisible(self) -> bool:
		"""
		Checks if the entity is visible.

		Returns:
			True if the entity is visible, False otherwise.
		"""

	def lookAt(self, x: float, y: float, z: float) -> None:
		"""
		Sets the entity's rotation to face the specified position.

		Args:
			x: The X-coordinate of the target position.
			y: The Y-coordinate of the target position.
			z: The Z-coordinate of the target position.
		"""

	def removeAllPassengers(self) -> None:
		"""
		Removes all passengers from the entity.
		"""

	def removePassenger(self, entity: Entity) -> None:
		"""
		Removes the specified entity from the entity's passengers.

		Args:
			entity: The entity to remove as a passenger.
		"""

	def removePermissionLevel(self, level: Number) -> None:
		"""
		Removes the specified permission level from the entity.

		Args:
			level: The permission level to remove.
		"""

	def ride(self, entity: Entity) -> None:
		"""
		Rides the specified entity.

		Args:
			entity: The entity to ride.
		"""

	def setPosition(self, x: float, y: float, z: float) -> None:
		"""
		Sets the position of the entity.

		Args:
			x: The X-coordinate of the new position.
			y: The Y-coordinate of the new position.
			z: The Z-coordinate of the new position.
		"""

	def setCustomName(self, customName: str) -> None:
		"""
		Sets the custom name of the entity using a string.

		Args:
			customName: The custom name to set.
		"""

	def setCustomNameVisible(self, visible: bool) -> None:
		"""
		Sets whether the custom name of the entity is visible.

		Args:
			visible: True to make the custom name visible, False to hide it.
		"""

	def setGlowing(self, glowing: bool) -> None:
		"""
		Sets whether the entity is glowing.

		Args:
			glowing: True to make the entity glow, False otherwise.
		"""

	def setInvisible(self, invisible: bool) -> None:
		"""
		Sets whether the entity is invisible.

		Args:
			invisible: True to make the entity invisible, False otherwise.
		"""

	def setInvulnerable(self, invulnerable: bool) -> None:
		"""
		Sets whether the entity is invulnerable.

		Args:
			invulnerable: True to make the entity invulnerable, False otherwise.
		"""

	def setMotion(self, motion: Vec3d) -> None:
		"""
		Sets the motion of the entity.

		Args:
			motion: The new motion to set for the entity.
		"""

	def setNoGravity(self, noGravity: bool) -> None:
		"""
		Sets whether the entity has gravity.

		Args:
			noGravity: True to disable gravity for the entity, False otherwise.
		"""

	def setSilent(self, silent: bool) -> None:
		"""
		Sets whether the entity is silent.

		Args:
			silent: True to make the entity silent, False otherwise.
		"""

	def setSneaking(self, sneaking: bool) -> None:
		"""
		Sets whether the entity is sneaking.

		Args:
			sneaking: True to make the entity sneak, False otherwise.
		"""

	def setSprinting(self, sprinting: bool) -> None:
		"""
		Sets whether the entity is sprinting.

		Args:
			sprinting: True to make the entity sprint, False otherwise.
		"""

	def startRiding(self, entity: Entity) -> None:
		"""
		Starts riding the specified entity.

		Args:
			entity: The entity to start riding.
		"""

	def stopRiding(self) -> None:
		"""
		Stops riding any entity the entity is currently riding.
		"""

	def teleport(self, position: Vec3d) -> None:
		"""
		Teleports the entity to the specified position.

		Args:
			position: The position to teleport the entity to.
		"""
