from typing import overload


class World:

    @overload
    def getBlock(self, x, y, z):
        ...

    @overload
    def getBlock(self, blockPos):
        ...

    @overload
    def getBlock(self, vec3d):
        ...

    def getAllPlayers(self):
        ...

    def getAllEntities(self):
        ...

    def getNearestPlayer(self, position):
        ...

    def getRandomPlayer(self):
        ...

    def getDifficulty(self):
        ...

    def getSeed(self):
        ...

    @overload
    def setBlock(self, x, y, z, block):
        ...

    @overload
    def setBlock(self, x, y, z, block):
        ...

    @overload
    def setBlock(self, blockPos, block):
        ...

    @overload
    def setBlock(self, blockPos, block):
        ...

    @overload
    def setSpawnPos(self, x, y, z):
        ...

    @overload
    def setSpawnPos(self, x, y, z, angle):
        ...

    @overload
    def setSpawnPos(self, blockPos):
        ...

    @overload
    def setSpawnPos(self, blockPos, angle):
        ...

    def setTime(self, time):
        ...

    @overload
    def setWeather(self, weather):
        ...

    @overload
    def setWeather(self, weather, duration):
        ...

    @overload
    def spawnEntity(self, entity, x, y, z, nbt):
        ...

    @overload
    def spawnEntity(self, entity, blockPos, nbt):
        ...
