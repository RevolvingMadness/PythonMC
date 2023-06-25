package com.revolvingmadness.pythonmc.pythonmclibrary.server.gamemode;

import net.minecraft.world.GameMode;

public enum PyGameModes {
    ADVENTURE, CREATIVE, SPECTATOR, SURVIVAL;

    public GameMode toGameMode() {
        return switch (this) {
            case ADVENTURE -> GameMode.ADVENTURE;
            case CREATIVE -> GameMode.CREATIVE;
            case SPECTATOR -> GameMode.SPECTATOR;
            case SURVIVAL -> GameMode.SURVIVAL;
        };
    }
}
