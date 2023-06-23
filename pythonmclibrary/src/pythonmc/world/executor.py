class Executor:
    name = None
    displayName = None
    position = None
    player = None
    world = None
    entity = None
    isExecutedByPlayer = None
    rotation = None

    def sendMessage(self, message):
        ...

    def sendError(self, error):
        ...

    def sendMessage(self, text):
        ...

    def sendError(self, text):
        ...
