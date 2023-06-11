package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.world.Difficulty;

public class PyDifficulty {
	Difficulty difficulty;
	public String name;
	public int id;
	public String info;
	
	public PyDifficulty(Difficulty difficulty) {
		this.difficulty = difficulty;
		this.name = difficulty.getName();
		this.id = difficulty.getId();
		this.info = difficulty.getInfo().getString();
	}
	
	@Override
	public String toString() {
		return name;
	}
}
