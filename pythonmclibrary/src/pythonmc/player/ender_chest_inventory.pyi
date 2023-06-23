from src.pythonmc.item.item_stack import ItemStack


class EnderChestInventory:
	"""
	The EnderChestInventory class represents the inventory of an Ender Chest in Minecraft.

	Attributes:
		stacks (list[ItemStack]): A list of ItemStack objects representing the items stored in the Ender Chest.
	"""

	stacks: list[ItemStack]
