package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.registry.RegistryKey;
import net.minecraft.world.World;

public enum PyWorlds {
    OVERWORLD, NETHER, END;

    public RegistryKey<World> toWorldRegistryKey() {
        return switch (this) {
            case OVERWORLD -> World.OVERWORLD;
            case NETHER -> World.NETHER;
            case END -> World.END;
        };
    }
}
