class World:
    def getBlock(self, x, y, z):
        ...

    def getBlock(self, blockPos):
        ...

    def getDifficulty(self):
        ...

    def getSeed(self):
        ...

    def setBlock(self, x, y, z, block):
        ...

    def setBlock(self, x, y, z, block):
        ...

    def setBlock(self, blockPos, block):
        ...

    def setBlock(self, blockPos, block):
        ...

    def setSpawnPos(self, x, y, z):
        ...

    def setSpawnPos(self, x, y, z, angle):
        ...

    def setSpawnPos(self, blockPos):
        ...

    def setSpawnPos(self, blockPos, angle):
        ...

    def setTime(self, time):
        ...

    def setWeather(self, weather):
        ...

    def setWeather(self, weather, duration):
        ...

    def spawnEntity(self, entity, x, y, z, nbt):
        ...

    def spawnEntity(self, entity, blockPos, nbt):
        ...