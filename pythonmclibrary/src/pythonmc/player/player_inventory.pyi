from numbers import Number
from typing import overload

from src.pythonmc.item.item_stack import ItemStack


class PlayerInventory:
    main: list[ItemStack]
    armor: list[ItemStack]
    offHand: list[ItemStack]
    selectedSlot: int

    def clear(self) -> None:
        """
        Clears the player's inventory.

        Returns:
            None
        """
    def contains(self, stack: ItemStack) -> bool:
        """
        Checks if the inventory contains the specified item stack.

        Args:
            stack (ItemStack): The item stack to check.

        Returns:
            bool: True if the inventory contains the item stack, False otherwise.
        """
    def dropAll(self) -> None:
        """
        Drops all items from the inventory.

        Returns:
            None
        """
    def dropSelectedItem(self, entireStack: bool) -> None:
        """
        Drops the selected item from the inventory.

        Args:
            entireStack (bool): Whether to drop the entire stack or just one item.

        Returns:
            None
        """
    def getArmorStack(self, slot: Number) -> ItemStack:
        """
        Retrieves the item stack in the specified armor slot.

        Args:
            slot (Number): The armor slot.

        Returns:
            ItemStack: The item stack in the specified armor slot.
        """
    def getEmptySlot(self) -> int:
        """
        Retrieves the index of an empty slot in the inventory.

        Returns:
            int: The index of an empty slot, or -1 if no empty slot is found.
        """
    def getMainHandStack(self) -> ItemStack:
        """
        Retrieves the item stack in the player's main hand.

        Returns:
            ItemStack: The item stack in the player's main hand.
        """
    def getSlotWithStack(self, stack: ItemStack) -> int:
        """
        Retrieves the index of the slot that contains the specified item stack.

        Args:
            stack (ItemStack): The item stack to search for.

        Returns:
            int: The index of the slot that contains the item stack, or -1 if not found.
        """
    def getStack(self, slot: Number) -> ItemStack:
        """
        Retrieves the item stack in the specified slot.

        Args:
            slot (Number): The slot index.

        Returns:
            ItemStack: The item stack in the specified slot.
        """
    def indexOf(self, stack: ItemStack) -> int:
        """
        Retrieves the index of the first occurrence of the specified item stack.

        Args:
            stack (ItemStack): The item stack to search for.

        Returns:
            int: The index of the first occurrence of the item stack, or -1 if not found.
        """
    @overload
    def insertStack(self, slot: Number, stack: ItemStack) -> None:
        """
        Inserts the specified item stack into the specified slot.

        Args:
            slot (Number): The slot index.
            stack (ItemStack): The item stack to insert.

        Returns:
            None
        """
    @overload
    def insertStack(self, stack: ItemStack) -> None:
        """
        Inserts the specified item stack into the first available slot.

        Args:
            stack (ItemStack): The item stack to insert.

        Returns:
            None
        """
    def isEmpty(self) -> bool:
        """
        Checks if the inventory is empty.

        Returns:
            bool: True if the inventory is empty, False otherwise.
        """
    def removeOne(self, stack: ItemStack) -> None:
        """
        Removes one item from the specified item stack.

        Args:
            stack (ItemStack): The item stack to remove from.

        Returns:
            None
        """
    @overload
    def removeStack(self, slot: Number, amount: Number) -> None:
        """
        Removes a specified number of items from the specified slot.

        Args:
            slot (Number): The slot index.
            amount (Number): The number of items to remove.

        Returns:
            None
        """
    @overload
    def removeStack(self, slot: Number) -> None:
        """
        Removes the item stack from the specified slot.

        Args:
            slot (Number): The slot index.

        Returns:
            None
        """
    def setStack(self, slot: Number, stack: ItemStack) -> None:
        """
        Sets the item stack in the specified slot.

        Args:
            slot (Number): The slot index.
            stack (ItemStack): The item stack to set.

        Returns:
            None
        """
