package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.entity.player.HungerManager;

public class PyHungerManager {
	HungerManager manager;
	public float exhaustion;
	public int foodLevel;
	public float saturationLevel;
	
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
