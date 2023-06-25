from .enchantment_rarity import EnchantmentRarity


class Enchantment:
    """
    The Enchantment class represents an enchantment applied to an item in Minecraft.

    Attributes:
            level (int): The level or magnitude of the enchantment.
            rarity (EnchantmentRarity): The rarity level of the enchantment.
    """

    level: int
    rarity: EnchantmentRarity
