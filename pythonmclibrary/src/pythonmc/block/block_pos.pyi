from numbers import Number

class BlockPos:
    """
    Represents a position in the world.

    Attributes:
            x (int): The x-coordinate of the position.
            y (int): The y-coordinate of the position.
            z (int): The z-coordinate of the position.
    """

    x: int
    y: int
    z: int

    def __init__(self, x: Number, y: Number, z: Number) -> None:
        """
        Initializes a new BlockPos object.

        Args:
                x (Number): The x-coordinate of the position.
                y (Number): The y-coordinate of the position.
                z (Number): The z-coordinate of the position.
        """
