from numbers import Number

from src.pythonmc.entity.arm import Arm
from src.pythonmc.entity.damage_sources import DamageSources
from src.pythonmc.entity.effects.status_effect_instance import StatusEffectInstance
from src.pythonmc.entity.effects.status_effects import StatusEffects
from src.pythonmc.entity.entity import Entity
from src.pythonmc.entity.hand import Hand
from src.pythonmc.item.item import Item
from src.pythonmc.item.item_stack import ItemStack
from src.pythonmc.world.position.vec3d import Vec3d


class LivingEntity(Entity):
	"""
    Represents a living entity.
    Inherits from Entity.
    """

	def addStatusEffect(
			self, effect: StatusEffects, duration: Number, amplifier: Number, visible: bool
	) -> None:
		"""
        Adds a status effect to the living entity.

        Args:
                effect (StatusEffects): The status effect to add.
                duration (Number): The duration of the effect.
                amplifier (Number): The amplifier level of the effect.
                visible (bool): Whether the effect is visible.
        """

	def canBreatheInWater(self) -> bool:
		"""
        Checks if the living entity can breathe underwater.

        Returns:
                bool: True if the entity can breathe in water, False otherwise.
        """

	def canHaveStatusEffect(self, effect: StatusEffects) -> bool:
		"""
        Checks if the living entity can have the specified status effect.

        Args:
                effect (StatusEffects): The status effect to check.

        Returns:
                bool: True if the entity can have the effect, False otherwise.
        """

	def canSee(self, entity: Entity) -> bool:
		"""
        Checks if the living entity can see the specified entity.

        Args:
                entity (Entity): The entity to check visibility.

        Returns:
                bool: True if the entity can see the other entity, False otherwise.
        """

	def canTakeDamage(self) -> bool:
		"""
        Checks if the living entity can take damage.

        Returns:
                bool: True if the entity can take damage, False otherwise.
        """

	def clearStatusEffects(self) -> None:
		"""
        Clears all status effects from the living entity.
        """

	def damageArmor(self, damageSource: DamageSources, amount: Number) -> None:
		"""
        Damages the entity's armor by the specified amount.

        Args:
                damageSource (DamageSources): The source of the damage.
                amount (Number): The amount of damage to apply.
        """

	def damageHelmet(self, damageSource: DamageSources, amount: Number) -> None:
		"""
        Damages the entity's helmet by the specified amount.

        Args:
                damageSource (DamageSources): The source of the damage.
                amount (Number): The amount of damage to apply.
        """

	def damageShield(self, amount: Number) -> None:
		"""
        Damages the entity's shield by the specified amount.

        Args:
                amount (Number): The amount of damage to apply.
        """

	def eatFood(self, stack: ItemStack) -> None:
		"""
        Makes the living entity eat the specified food item stack.

        Args:
                stack (ItemStack): The food item stack to eat.
        """

	def getAbsorptionAmount(self) -> float:
		"""
        Returns the absorption amount of the living entity.

        Returns:
                float: The absorption amount.
        """

	def getActiveHand(self) -> Hand:
		"""
        Returns the active hand of the living entity.

        Returns:
                Hand: The active hand.
        """

	def getActiveItem(self) -> ItemStack:
		"""
        Returns the item stack in the entity's active hand.

        Returns:
                ItemStack: The active item stack.
        """

	def getArmor(self) -> float:
		"""
        Returns the armor value of the living entity.

        Returns:
                float: The armor value.
        """

	def getAttacker(self) -> LivingEntity:
		"""
        Returns the entity that attacked this living entity.

        Returns:
                LivingEntity: The attacking entity.
        """

	def getAttacking(self) -> LivingEntity:
		"""
        Returns the entity that this living entity is currently attacking.

        Returns:
                LivingEntity: The attacking entity.
        """

	def getMainArm(self) -> Arm:
		"""
        Returns the main arm of the living entity.

        Returns:
                Arm: The main arm.
        """

	def getMainHandStack(self) -> ItemStack:
		"""
        Returns the item stack in the entity's main hand.

        Returns:
                ItemStack: The main hand item stack.
        """

	def getMaxHealth(self) -> float:
		"""
        Returns the maximum health of the living entity.

        Returns:
                float: The maximum health.
        """

	def getMovementSpeed(self) -> float:
		"""
        Returns the movement speed of the living entity.

        Returns:
                float: The movement speed.
        """

	def getScaleFactor(self) -> float:
		"""
        Returns the scale factor of the living entity.

        Returns:
                float: The scale factor.
        """

	def getStackInHand(self, hand: Hand) -> ItemStack:
		"""
        Returns the item stack in the specified hand.

        Args:
                hand (Hand): The hand to get the item stack from.

        Returns:
                ItemStack: The item stack in the hand.
        """

	def getStatusEffect(self, effect: StatusEffects) -> StatusEffectInstance:
		"""
        Returns the status effect instance of the specified effect.

        Args:
                effect (StatusEffects): The status effect to retrieve.

        Returns:
                StatusEffectInstance: The status effect instance.
        """

	def getStatusEffects(self) -> list[StatusEffectInstance]:
		"""
        Returns a list of all status effects applied to the living entity.

        Returns:
                list[StatusEffectInstance]: The list of status effect instances.
        """

	def getStuckArrowCount(self) -> float:
		"""
        Returns the number of arrows stuck in the living entity.

        Returns:
                float: The stuck arrow count.
        """

	def hasStatusEffect(self, effect: StatusEffects) -> bool:
		"""
        Checks if the living entity has the specified status effect.

        Args:
                effect (StatusEffects): The status effect to check.

        Returns:
                bool: True if the entity has the effect, False otherwise.
        """

	def heal(self, amount: Number) -> None:
		"""
        Heals the living entity by the specified amount.

        Args:
                amount (Number): The amount to heal.
        """

	def getHealth(self) -> float:
		"""
        Returns the current health of the living entity.

        Returns:
                float: The current health.
        """

	def isAffectedBySplashPotions(self) -> bool:
		"""
        Checks if the living entity is affected by splash potions.

        Returns:
                bool: True if the entity is affected, False otherwise.
        """

	def isBaby(self) -> bool:
		"""
        Checks if the living entity is a baby.

        Returns:
                bool: True if the entity is a baby, False otherwise.
        """

	def isBlocking(self) -> bool:
		"""
        Checks if the living entity is currently blocking.

        Returns:
                bool: True if the entity is blocking, False otherwise.
        """

	def isClimbing(self) -> bool:
		"""
        Checks if the living entity is currently climbing.

        Returns:
                bool: True if the entity is climbing, False otherwise.
        """

	def isDead(self) -> bool:
		"""
        Checks if the living entity is dead.

        Returns:
                bool: True if the entity is dead, False otherwise.
        """

	def isFallFlying(self) -> bool:
		"""
        Checks if the living entity is currently fall flying.

        Returns:
                bool: True if the entity is fall flying, False otherwise.
        """

	def isHolding(self, item: Item) -> bool:
		"""
        Checks if the living entity is holding the specified item.

        Args:
                item (Item): The item to check.

        Returns:
                bool: True if the entity is holding the item, False otherwise.
        """

	def isHoldingOntoLadder(self) -> bool:
		"""
        Checks if the living entity is holding onto a ladder.

        Returns:
                bool: True if the entity is holding onto a ladder, False otherwise.
        """

	def isHurtByWater(self) -> bool:
		"""
        Checks if water hurts the living entity.

        Returns:
                bool: True if water hurts the entity, False otherwise.
        """

	def isMobOrPlayer(self) -> bool:
		"""
        Checks if the living entity is either a mob or a player.

        Returns:
                bool: True if the entity is a mob or a player, False otherwise.
        """

	def isSleeping(self) -> bool:
		"""
        Checks if the living entity is sleeping.

        Returns:
                bool: True if the entity is sleeping, False otherwise.
        """

	def isUndead(self) -> bool:
		"""
        Checks if the living entity is undead.

        Returns:
                bool: True if the entity is undead, False otherwise.
        """

	def isUsingItem(self) -> bool:
		"""
        Checks if the living entity is currently using an item.

        Returns:
                bool: True if the entity is using an item, False otherwise.
        """

	def isUsingRiptide(self) -> bool:
		"""
        Checks if the living entity is currently using the riptide enchantment.

        Returns:
                bool: True if the entity is using riptide, False otherwise.
        """

	def removeStatusEffect(self, effect: StatusEffects) -> None:
		"""
        Removes the specified status effect from the living entity.

        Args:
                effect (StatusEffects): The status effect to remove.
        """

	def setAbsorptionAmount(self, amount: Number) -> None:
		"""
        Sets the absorption amount of the living entity.

        Args:
                amount (Number): The absorption amount to set.
        """

	def setAttacker(self, entity: LivingEntity) -> None:
		"""
        Sets the entity that attacked this living entity.

        Args:
                entity (LivingEntity): The attacking entity.
        """

	def setAttacking(self, entity: LivingEntity) -> None:
		"""
        Sets the entity that this living entity is currently attacking.

        Args:
                entity (LivingEntity): The attacking entity.
        """

	def setCurrentHand(self, hand: Hand) -> None:
		"""
        Sets the current hand of the living entity.

        Args:
                hand (Hand): The hand to set as current.
        """

	def setHealth(self, amount: Number) -> None:
		"""
        Sets the current health of the living entity.

        Args:
                amount (Number): The amount to set as health.
        """

	def setJumping(self, jumping: bool) -> None:
		"""
        Sets whether the living entity is jumping.

        Args:
                jumping (bool): True if the entity is jumping, False otherwise.
        """

	def setMovementSpeed(self, movementSpeed: Number) -> None:
		"""
        Sets the movement speed of the living entity.

        Args:
                movementSpeed (Number): The movement speed to set.
        """

	def setStackInHand(self, hand: Hand, stack: ItemStack) -> None:
		"""
        Sets the item stack in the specified hand.

        Args:
                hand (Hand): The hand to set the item stack in.
                stack (ItemStack): The item stack to set.
        """

	def setStingerCount(self, stingerCount: Number) -> None:
		"""
        Sets the stinger count of the living entity.

        Args:
                stingerCount (Number): The stinger count to set.
        """

	def setStuckArrowCount(self, stuckArrowCount: Number) -> None:
		"""
        Sets the number of arrows stuck in the living entity.

        Args:
                stuckArrowCount (Number): The stuck arrow count to set.
        """

	def shouldDisplaySoulSpeedEffects(self) -> bool:
		"""
        Checks if the living entity should display soul speed effects.

        Returns:
                bool: True if the entity should display soul speed effects, False otherwise.
        """

	def shouldDropXp(self) -> bool:
		"""
        Checks if the living entity should drop experience points upon death.

        Returns:
                bool: True if the entity should drop experience points, False otherwise.
        """

	def swingHand(self, hand: Hand) -> None:
		"""
        Swings the specified hand of the living entity.

        Args:
                hand (Hand): The hand to swing.
        """

	def takeKnockback(self, strength: Number, x: Number, z: Number) -> None:
		"""
        Applies knockback to the living entity.

        Args:
                strength (Number): The strength of the knockback.
                x (Number): The x-direction of the knockback.
                z (Number): The z-direction of the knockback.
        """

	def teleport(self, position: Vec3d) -> None:
		"""
        Teleports the living entity to the specified position.

        Args:
                position (Vec3d): The position to teleport to.
        """

	def tiltScreen(self, deltaX: Number, deltaY: Number) -> None:
		"""
        Tilts the screen of the living entity by the specified amount.

        Args:
                deltaX (Number): The amount to tilt the screen horizontally.
                deltaY (Number): The amount to tilt the screen vertically.
        """
