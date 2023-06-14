package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.server.MinecraftServer;
import net.minecraft.world.GameMode;

public class PyServer {
	final MinecraftServer server;

	public PyServer(MinecraftServer server) {
		this.server = server;
	}

	public PyPlayerManager getPlayerManager() {
		return new PyPlayerManager(this.server.getPlayerManager());
	}

	public void setDifficulty(PyDifficulties difficulty) {
		this.server.setDifficulty(difficulty.toDifficulty().difficulty, true);
	}

	public void setDefaultGameMode(PyGameModes mode) {
		this.server.setDefaultGameMode(mode.toGameMode());
	}

	public void setDifficultyLocked(boolean locked) {
		this.server.setDifficultyLocked(locked);
	}

	public String getServerIP() {
		return this.server.getServerIp();
	}

	public String getServerMOTD() {
		return this.server.getServerMotd();
	}

	public int getServerPort() {
		return this.server.getServerPort();
	}

	public PyGameMode getDefaultGameMode() {
		return new PyGameMode(this.server.getDefaultGameMode());
	}

	public PyGameMode getForcedGameMode() {
		GameMode forcedGameMode = this.server.getForcedGameMode();
		if (forcedGameMode == null) {
			return null;
		}
		return new PyGameMode(forcedGameMode);
	}

	public int getMaxPlayerCount() {
		return this.server.getMaxPlayerCount();
	}

	public int getMaxWorldBorderRadius() {
		return this.server.getMaxWorldBorderRadius();
	}

	public int getSpawnProtectionRadius() {
		return this.server.getSpawnProtectionRadius();
	}

	public int getSpawnRadius(PyWorlds world) {
		return this.server.getSpawnRadius(this.server.getWorld(world.toWorldRegistryKey()));
	}

	public String getVersion() {
		return this.server.getVersion();
	}

	public boolean isFlightEnabled() {
		return this.server.isFlightEnabled();
	}

	public boolean isHardcore() {
		return this.server.isHardcore();
	}

	public boolean isMonsterSpawningEnabled() {
		return this.server.isMonsterSpawningEnabled();
	}

	public boolean isNetherAllowed() {
		return this.server.isNetherAllowed();
	}

	public boolean isPVPEnabled() {
		return this.server.isPvpEnabled();
	}

	public boolean isSingleplayer() {
		return this.server.isSingleplayer();
	}

	public void openToLAN(PyGameModes gameMode, boolean cheatsAllowed, Number port) {
		this.server.openToLan(gameMode.toGameMode(), cheatsAllowed, port.intValue());
	}
}
