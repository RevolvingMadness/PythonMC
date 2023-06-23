from src.pythonmc.block.blocks import Blocks
from src.pythonmc.item.item import Item


class Block:
    item: Item
    name: str
    blastResistance: float
    velocityMultiplier: float
    jumpVelocityMultiplier: float
    slipperiness: float

    def __init__(self, block: Blocks) -> None:
        """
        Initializes a new Block object.

        Args:
            block (Blocks): The block object representing the block.

        Returns:
            None
        """
