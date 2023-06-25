from .items import Items


class Item:
    """
    Represents an item.

    Attributes:
            name (str): The name of the item.
    """

    name: str

    def __init__(self, item: Items) -> None: ...
