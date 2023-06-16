package com.revolvingmadness.pythonmc.pythonmclibrary.server.difficulty;

import net.minecraft.world.Difficulty;

public class PyDifficulty {
	final Difficulty difficulty;
	public final String name;
	public final int id;
	public final String info;

	public PyDifficulty(Difficulty difficulty) {
		this.difficulty = difficulty;
		this.name = difficulty.getName();
		this.id = difficulty.getId();
		this.info = difficulty.getInfo().getString();
	}

	@Override
	public String toString() {
		return this.name;
	}
}
