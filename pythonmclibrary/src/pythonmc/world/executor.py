from typing import overload


class Executor:
    name = None
    displayName = None
    position = None
    player = None
    world = None
    entity = None
    isExecutedByPlayer = None
    rotation = None

    @overload
    def sendMessage(self, message):
        ...

    @overload
    def sendError(self, error):
        ...

    @overload
    def sendMessage(self, text):
        ...

    @overload
    def sendError(self, text):
        ...
