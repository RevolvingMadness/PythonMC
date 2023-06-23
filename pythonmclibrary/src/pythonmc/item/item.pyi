from src.pythonmc.item.items import Items


class Item:
    """
    Represents an item in the game.

    Attributes:
        name (str): The name of the item.
    """

    name: str

    def __init__(self, item: Items) -> None: ...
