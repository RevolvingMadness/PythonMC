class Vec2f:
	"""
	Represents a two-dimensional vector.

	Attributes:
		x (float): The x-coordinate of the vector.
		y (float): The y-coordinate of the vector.
	"""

	x: float
	y: float

	def __init__(self, x: float, y: float) -> None:
		"""
		Initializes a Vec2f instance with the given coordinates.

		Args:
			x (float): The x-coordinate of the vector.
			y (float): The y-coordinate of the vector.
		"""
