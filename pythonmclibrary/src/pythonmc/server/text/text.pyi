from pythonmc.server.text.formatting import Formatting


class Text:
    message: str

    def __init__(self, message: str) -> None: ...

    def withFormatting(self, formatting: Formatting): ...
