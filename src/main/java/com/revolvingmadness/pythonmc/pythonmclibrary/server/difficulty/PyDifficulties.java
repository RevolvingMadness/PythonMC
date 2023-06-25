package com.revolvingmadness.pythonmc.pythonmclibrary.server.difficulty;

import net.minecraft.world.Difficulty;

public enum PyDifficulties {
	EASY, HARD, NORMAL, PEACEFUL;
	
	public PyDifficulty toDifficulty() {
		return switch (this) {
			case EASY -> new PyDifficulty(Difficulty.EASY);
			case HARD -> new PyDifficulty(Difficulty.HARD);
			case NORMAL -> new PyDifficulty(Difficulty.NORMAL);
			case PEACEFUL -> new PyDifficulty(Difficulty.PEACEFUL);
		};
	}
}
