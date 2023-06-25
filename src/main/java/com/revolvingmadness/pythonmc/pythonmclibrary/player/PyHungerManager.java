package com.revolvingmadness.pythonmc.pythonmclibrary.player;

import net.minecraft.entity.player.HungerManager;

public class PyHungerManager {
    public final float exhaustion;
    public final int foodLevel;
    public final float saturationLevel;
    final HungerManager manager;

    public PyHungerManager(HungerManager manager) {
        this.manager = manager;
        this.exhaustion = manager.getExhaustion();
        this.foodLevel = manager.getFoodLevel();
        this.saturationLevel = manager.getSaturationLevel();
    }

    @Override
    public String toString() {
        return String.valueOf(this.foodLevel);
    }
}
