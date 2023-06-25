from .block import Block
from .blocks import Blocks


class BlockState:
    """
    The BlockState class represents the state of a block in Minecraft.

    Attributes:
            block (Block): The block associated with this state.
    """

    block: Block

    def __init__(self, block: Blocks) -> None: ...

    @staticmethod
    def isOf(block: Block) -> bool: ...
