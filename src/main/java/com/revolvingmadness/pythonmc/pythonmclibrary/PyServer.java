package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.server.MinecraftServer;

public class PyServer {
    MinecraftServer server;

    public PyServer(MinecraftServer server) {
        this.server = server;
    }

    public void setDifficulty(PyDifficulties difficulty) {
        this.server.setDifficulty(difficulty.toDifficulty().difficulty, true);
    }

    public void setPVPEnabled(boolean pvpEnabled) {
        this.server.setPvpEnabled(pvpEnabled);
    }

    public void setFlightEnabled(boolean flightEnabled) {
        this.server.setFlightEnabled(flightEnabled);
    }

    public void setDefaultGameMode(PyGameModes mode) {
        this.server.setDefaultGameMode(mode.toGameMode());
    }

    public void setDifficultyLocked(boolean locked) {
        this.server.setDifficultyLocked(locked);
    }
}
