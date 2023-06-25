class Vec3d:
    """
    Represents a three-dimensional vector.

    Attributes:
            x (float): The x-coordinate of the vector.
            y (float): The y-coordinate of the vector.
            z (float): The z-coordinate of the vector.
    """

    x: float
    y: float
    z: float

    def __init__(self, x: float, y: float, z: float) -> None:
        """
        Initializes a Vec3d instance with the given coordinates.

        Args:
                x (float): The x-coordinate of the vector.
                y (float): The y-coordinate of the vector.
                z (float): The z-coordinate of the vector.
        """
