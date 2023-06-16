package com.revolvingmadness.pythonmc.pythonmclibrary.scoreboard;

import net.minecraft.scoreboard.ScoreboardPlayerScore;

public class PyScoreboardPlayerScore {
	ScoreboardPlayerScore score;

	public PyScoreboardPlayerScore(ScoreboardPlayerScore score) {
		this.score = score;
	}

	public void clearScore() {
		this.score.clearScore();
	}

	public String getPlayerName() {
		return this.score.getPlayerName();
	}

	public int getScore() {
		return this.score.getScore();
	}

	public PyScoreboard getScoreboard() {
		return new PyScoreboard(this.score.getScoreboard());
	}

	public void incrementScore() {
		this.score.incrementScore();
	}

	public void incrementScore(Number amount) {
		this.score.incrementScore(amount.intValue());
	}

	public void setScore(Number score) {
		this.score.setScore(score.intValue());
	}
}
