package com.revolvingmadness.pythonmc.pythonmclibrary.scoreboard;

import net.minecraft.scoreboard.ScoreboardCriterion;

public enum PyRenderTypes {
	INTEGER, HEARTS;
	
	public static PyRenderTypes fromRenderType(ScoreboardCriterion.RenderType renderType) {
		return switch (renderType) {
			case INTEGER -> INTEGER;
			case HEARTS -> HEARTS;
		};
	}
	
	public ScoreboardCriterion.RenderType toRenderType() {
		return switch (this) {
			case INTEGER -> ScoreboardCriterion.RenderType.INTEGER;
			case HEARTS -> ScoreboardCriterion.RenderType.HEARTS;
		};
	}
}
