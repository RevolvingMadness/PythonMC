package com.revolvingmadness.pythonmc.pythonmclibrary.entity;

import net.minecraft.entity.Entity;

public enum PyRemovalReasons {
    KILLED, DISCARDED, UNLOADED_TO_CHUNK, UNLOADED_WITH_PLAYER, CHANGED_DIMENSION;

    public Entity.RemovalReason toRemovalReason() {
        return switch (this) {
            case KILLED -> Entity.RemovalReason.KILLED;
            case DISCARDED -> Entity.RemovalReason.DISCARDED;
            case UNLOADED_TO_CHUNK -> Entity.RemovalReason.UNLOADED_TO_CHUNK;
            case UNLOADED_WITH_PLAYER -> Entity.RemovalReason.UNLOADED_WITH_PLAYER;
            case CHANGED_DIMENSION -> Entity.RemovalReason.CHANGED_DIMENSION;
        };
    }
}
