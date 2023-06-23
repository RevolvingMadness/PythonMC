from numbers import Number
from typing import overload

from src.pythonmc.item.enchantment.enchantment import Enchantment
from src.pythonmc.item.enchantment.enchantments import Enchantments
from src.pythonmc.item.hide_flags import HideFlags
from src.pythonmc.item.item_rarity import ItemRarity
from src.pythonmc.item.items import Items
from src.pythonmc.server.text.text import Text


class ItemStack:
    """
    Represents an item stack in Minecraft.
    """

    @overload
    def __init__(self, item: Items, count: Number, nbt: dict[str, object]) -> None:
        """
        Initializes an ItemStack with the specified item, count, and NBT data.

        Args:
            item (Items): The item type.
            count (Number): The number of items in the stack.
            nbt (dict[str, object]): The NBT data associated with the item.

        Returns:
            None
        """
    @overload
    def __init__(self, item: Items, nbt: dict[str, object]) -> None:
        """
        Initializes an ItemStack with the specified item and NBT data.

        Args:
            item (Items): The item type.
            nbt (dict[str, object]): The NBT data associated with the item.

        Returns:
            None
        """
    @overload
    def __init__(self, item: Items, count: Number) -> None:
        """
        Initializes an ItemStack with the specified item and count.

        Args:
            item (Items): The item type.
            count (Number): The number of items in the stack.

        Returns:
            None
        """
    @overload
    def __init__(self, item: Items) -> None:
        """
        Initializes an ItemStack with the specified item.

        Args:
            item (Items): The item type.

        Returns:
            None
        """
    def addEnchantment(self, enchantment: Enchantments, level: Number) -> None:
        """
        Adds an enchantment to the item stack.

        Args:
            enchantment (Enchantments): The enchantment to add.
            level (Number): The level of enchantment.

        Returns:
            None
        """
    def addHideFlag(self, hideFlag: HideFlags) -> None:
        """
        Adds a hide flag to the item stack.

        Args:
            hideFlag (HideFlags): The hide flag to add.

        Returns:
            None
        """
    def decrement(self, amount: Number) -> None:
        """
        Decrements the count of items in the stack by the specified amount.

        Args:
            amount (Number): The amount to decrement.

        Returns:
            None
        """
    def getCount(self) -> int:
        """
        Returns the number of items in the stack.

        Returns:
            int: The count of items.
        """
    def getDamage(self) -> int:
        """
        Returns the damage value of the item stack.

        Returns:
            int: The damage value.
        """
    def getEnchantments(self) -> list[Enchantment]:
        """
        Returns a list of enchantments applied to the item stack.

        Returns:
            list[Enchantment]: The list of enchantments.
        """
    def getMaxCount(self) -> int:
        """
        Returns the maximum count of items allowed in the stack.

        Returns:
            int: The maximum count.
        """
    def getMaxDamage(self) -> int:
        """
        Returns the maximum damage value of the item stack.

        Returns:
            int: The maximum damage value.
        """
    def getName(self) -> str:
        """
        Returns the name of the item.

        Returns:
            str: The item name.
        """
    def getNbt(self) -> dict[str, object]:
        """
        Returns the NBT data associated with the item stack.

        Returns:
            dict[str, object]: The NBT data.
        """
    def getRarity(self) -> ItemRarity:
        """
        Returns the rarity of the item.

        Returns:
            ItemRarity: The item rarity.
        """
    def getRepairCost(self) -> int:
        """
        Returns the repair cost of the item.

        Returns:
            int: The repair cost.
        """
    def hasCustomName(self) -> bool:
        """
        Checks if the item has a custom name.

        Returns:
            bool: True if the item has a custom name, False otherwise.
        """
    def hasEnchantments(self) -> bool:
        """
        Checks if the item has any enchantments.

        Returns:
            bool: True if the item has enchantments, False otherwise.
        """
    def hasGlint(self) -> bool:
        """
        Checks if the item has a glint effect.

        Returns:
            bool: True if the item has a glint effect, False otherwise.
        """
    def hasNbt(self) -> bool:
        """
        Checks if the item has NBT data.

        Returns:
            bool: True if the item has NBT data, False otherwise.
        """
    def increment(self, amount: Number) -> None:
        """
        Increments the count of items in the stack by the specified amount.

        Args:
            amount (Number): The amount to increment.

        Returns:
            None
        """
    def isDamageable(self) -> bool:
        """
        Checks if the item is damageable.

        Returns:
            bool: True if the item is damageable, False otherwise.
        """
    def isDamaged(self) -> bool:
        """
        Checks if the item is damaged.

        Returns:
            bool: True if the item is damaged, False otherwise.
        """
    def isEnchantable(self) -> bool:
        """
        Checks if the item is enchantable.

        Returns:
            bool: True if the item is enchantable, False otherwise.
        """
    def isFood(self) -> bool:
        """
        Checks if the item is a food item.

        Returns:
            bool: True if the item is a food item, False otherwise.
        """
    def isItemBarVisible(self) -> bool:
        """
        Checks if the item bar is visible.

        Returns:
            bool: True if the item bar is visible, False otherwise.
        """
    def isStackable(self) -> bool:
        """
        Checks if the item is stackable.

        Returns:
            bool: True if the item is stackable, False otherwise.
        """
    def removeCustomName(self) -> None:
        """
        Removes the custom name of the item.

        Returns:
            None
        """
    def setCount(self, count: Number) -> None:
        """
        Sets the count of items in the stack.

        Args:
            count (Number): The count of items.

        Returns:
            None
        """
    @overload
    def setCustomName(self, customName: str) -> None:
        """
        Sets the custom name of the item.

        Args:
            customName (str): The custom name.

        Returns:
            None
        """
    @overload
    def setCustomName(self, text: Text) -> None:
        """
        Sets the custom name of the item using a text object.

        Args:
            text (Text): The text object representing the custom name.

        Returns:
            None
        """
    def setDamage(self, damage: Number) -> None:
        """
        Sets the damage value of the item stack.

        Args:
            damage (Number): The damage value.

        Returns:
            None
        """
    def setRepairCost(self, repairCost: Number) -> None:
        """
        Sets the repair cost of the item.

        Args:
            repairCost (Number): The repair cost.

        Returns:
            None
        """
