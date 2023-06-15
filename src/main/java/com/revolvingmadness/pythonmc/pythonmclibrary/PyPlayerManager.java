package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.server.PlayerManager;
import net.minecraft.text.Text;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class PyPlayerManager {
	PlayerManager playerManager;

	public PyPlayerManager(PlayerManager playerManager) {
		this.playerManager = playerManager;
	}

	public boolean areCheatsAllowed() {
		return this.playerManager.areCheatsAllowed();
	}

	public void broadcast(Object message) {
		this.playerManager.broadcast(Text.of(String.valueOf(message)), false);
	}

	public void broadcast(PyText text) {
		this.playerManager.broadcast(text.text, false);
	}

	public void disconnectAllPlayers() {
		this.playerManager.disconnectAllPlayers();
	}

	public int getCurrentPlayerCount() {
		return this.playerManager.getCurrentPlayerCount();
	}

	public int getMaxPlayerCount() {
		return this.playerManager.getMaxPlayerCount();
	}

	public List<String> getOpNames() {
		return Arrays.stream(this.playerManager.getOpNames()).toList();
	}

	public PyPlayerEntity getPlayer(String name) {
		return new PyPlayerEntity(this.playerManager.getPlayer(name));
	}

	public List<PyPlayerEntity> getPlayerList() {
		List<PyPlayerEntity> result = new ArrayList<>();
		this.playerManager.getPlayerList().forEach(player -> result.add(new PyPlayerEntity(player)));
		return result;
	}

	public List<String> getPlayerNames() {
		return Arrays.stream(this.playerManager.getPlayerNames()).toList();
	}

	public int getViewDistance() {
		return this.playerManager.getViewDistance();
	}

	public List<String> getWhitelistedNames() {
		return Arrays.stream(this.playerManager.getWhitelistedNames()).toList();
	}

	public boolean isWhitelistEnabled() {
		return this.playerManager.isWhitelistEnabled();
	}

	public void reloadWhitelist() {
		this.playerManager.reloadWhitelist();
	}

	public void setCheatsAllowed(boolean cheatsAllowed) {
		this.playerManager.setCheatsAllowed(cheatsAllowed);
	}

	public void setSimulationDistance(Number simulationDistance) {
		this.playerManager.setSimulationDistance(simulationDistance.intValue());
	}

	public void setViewDistance(Number viewDistance) {
		this.playerManager.setViewDistance(viewDistance.intValue());
	}

	public void setWhitelistEnabled(boolean whitelistEnabled) {
		this.playerManager.setWhitelistEnabled(whitelistEnabled);
	}
}
