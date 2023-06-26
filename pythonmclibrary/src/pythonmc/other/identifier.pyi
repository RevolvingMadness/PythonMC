class Identifier:
    """
    Represents an identifier with a namespace and a path.

    Attributes:
        namespace (str): The namespace of the identifier.
        path (str): The path of the identifier.
    """
    namespace: str
    path: str

    def __init__(self, namespace: str, path: str) -> None:
        ...
