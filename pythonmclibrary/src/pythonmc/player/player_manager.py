from typing import overload


class PlayerManager:
	def areCheatsAllowed(self):
		pass

	@overload
	def broadcast(self, message):
		pass

	@overload
	def broadcast(self, text):
		pass

	def disconnectAllPlayers(self):
		pass

	def getCurrentPlayerCount(self):
		pass

	def getMaxPlayerCount(self):
		pass

	def getOpNames(self):
		pass

	def getPlayer(self, name):
		pass

	def getPlayerList(self):
		pass

	def getPlayerNames(self):
		pass

	def getViewDistance(self):
		pass

	def getWhitelistedNames(self):
		pass

	def isWhitelistEnabled(self):
		pass

	def reloadWhitelist(self):
		pass

	def setCheatsAllowed(self, cheatsAllowed):
		pass

	def setSimulationDistance(self, simulationDistance):
		pass

	def setViewDistance(self, viewDistance):
		pass

	def setWhitelistEnabled(self, whitelistEnabled):
		pass
