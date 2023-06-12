package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.server.MinecraftServer;
import net.minecraft.world.GameMode;

public class PyServer {
    final MinecraftServer server;

    public PyServer(MinecraftServer server) {
        this.server = server;
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

    public Integer getServerPort() {
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

    public Integer getMaxPlayerCount() {
        return this.server.getMaxPlayerCount();
    }

    public Integer getMaxWorldBorderRadius() {
        return this.server.getMaxWorldBorderRadius();
    }

    public Integer getSpawnProtectionRadius() {
        return this.server.getSpawnProtectionRadius();
    }

    public Integer getSpawnRadius(PyWorlds world) {
        return this.server.getSpawnRadius(this.server.getWorld(world.toWorldRegistryKey()));
    }

    public String getVersion() {
        return this.server.getVersion();
    }

    public Boolean isFlightEnabled() {
        return this.server.isFlightEnabled();
    }

    public Boolean isHardcore() {
        return this.server.isHardcore();
    }

    public Boolean isMonsterSpawningEnabled() {
        return this.server.isMonsterSpawningEnabled();
    }

    public Boolean isNetherAllowed() {
        return this.server.isNetherAllowed();
    }

    public Boolean isPVPEnabled() {
        return this.server.isPvpEnabled();
    }

    public Boolean isSingleplayer() {
        return this.server.isSingleplayer();
    }

    public void openToLAN(PyGameModes gameMode, boolean cheatsAllowed, Number port) {
        this.server.openToLan(gameMode.toGameMode(), cheatsAllowed, port.intValue());
    }
}
