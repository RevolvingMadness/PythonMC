package com.revolvingmadness.pythonmc.pythonmclibrary.scoreboard;

import net.minecraft.scoreboard.ScoreboardCriterion;

public enum PyScoreboardCriterions {
	DUMMY, TRIGGER, DEATH_COUNT, PLAYER_KILL_COUNT, TOTAL_KILL_COUNT, HEALTH, FOOD, AIR, ARMOR, XP, LEVEL, TEAM_KILL_BLACK, TEAM_KILL_DARK_BLUE, TEAM_KILL_DARK_GREEN, TEAM_KILL_DARK_AQUA, TEAM_KILL_DARK_RED, TEAM_KILL_DARK_PURPLE, TEAM_KILL_GOLD, TEAM_KILL_GRAY, TEAM_KILL_DARK_GRAY, TEAM_KILL_BLUE, TEAM_KILL_GREEN, TEAM_KILL_AQUA, TEAM_KILL_RED, TEAM_KILL_LIGHT_PURPLE, TEAM_KILL_YELLOW, TEAM_KILL_WHITE, KILLED_BY_TEAM_BLACK, KILLED_BY_TEAM_DARK_BLUE, KILLED_BY_TEAM_DARK_GREEN, KILLED_BY_TEAM_DARK_AQUA, KILLED_BY_TEAM_DARK_RED, KILLED_BY_TEAM_DARK_PURPLE, KILLED_BY_TEAM_GOLD, KILLED_BY_TEAM_GRAY, KILLED_BY_TEAM_DARK_GRAY, KILLED_BY_TEAM_BLUE, KILLED_BY_TEAM_GREEN, KILLED_BY_TEAM_AQUA, KILLED_BY_TEAM_RED, KILLED_BY_TEAM_LIGHT_PURPLE, KILLED_BY_TEAM_YELLOW, KILLED_BY_TEAM_WHITE;
	
	public static PyScoreboardCriterions fromScoreboardCriterion(ScoreboardCriterion criterion) {
		if (criterion == ScoreboardCriterion.DUMMY) {
			return DUMMY;
		} else if (criterion == ScoreboardCriterion.TRIGGER) {
			return TRIGGER;
		} else if (criterion == ScoreboardCriterion.DEATH_COUNT) {
			return DEATH_COUNT;
		} else if (criterion == ScoreboardCriterion.PLAYER_KILL_COUNT) {
			return PLAYER_KILL_COUNT;
		} else if (criterion == ScoreboardCriterion.TOTAL_KILL_COUNT) {
			return TOTAL_KILL_COUNT;
		} else if (criterion == ScoreboardCriterion.HEALTH) {
			return HEALTH;
		} else if (criterion == ScoreboardCriterion.FOOD) {
			return FOOD;
		} else if (criterion == ScoreboardCriterion.AIR) {
			return AIR;
		} else if (criterion == ScoreboardCriterion.ARMOR) {
			return ARMOR;
		} else if (criterion == ScoreboardCriterion.XP) {
			return XP;
		} else if (criterion == ScoreboardCriterion.LEVEL) {
			return LEVEL;
		} else if (criterion == ScoreboardCriterion.TEAM_KILLS[0]) {
			return TEAM_KILL_BLACK;
		} else if (criterion == ScoreboardCriterion.TEAM_KILLS[1]) {
			return TEAM_KILL_DARK_BLUE;
		} else if (criterion == ScoreboardCriterion.TEAM_KILLS[2]) {
			return TEAM_KILL_DARK_GREEN;
		} else if (criterion == ScoreboardCriterion.TEAM_KILLS[3]) {
			return TEAM_KILL_DARK_AQUA;
		} else if (criterion == ScoreboardCriterion.TEAM_KILLS[4]) {
			return TEAM_KILL_DARK_RED;
		} else if (criterion == ScoreboardCriterion.TEAM_KILLS[5]) {
			return TEAM_KILL_DARK_PURPLE;
		} else if (criterion == ScoreboardCriterion.TEAM_KILLS[6]) {
			return TEAM_KILL_GOLD;
		} else if (criterion == ScoreboardCriterion.TEAM_KILLS[7]) {
			return TEAM_KILL_GRAY;
		} else if (criterion == ScoreboardCriterion.TEAM_KILLS[8]) {
			return TEAM_KILL_DARK_GRAY;
		} else if (criterion == ScoreboardCriterion.TEAM_KILLS[9]) {
			return TEAM_KILL_BLUE;
		} else if (criterion == ScoreboardCriterion.TEAM_KILLS[10]) {
			return TEAM_KILL_GREEN;
		} else if (criterion == ScoreboardCriterion.TEAM_KILLS[11]) {
			return TEAM_KILL_AQUA;
		} else if (criterion == ScoreboardCriterion.TEAM_KILLS[12]) {
			return TEAM_KILL_RED;
		} else if (criterion == ScoreboardCriterion.TEAM_KILLS[13]) {
			return TEAM_KILL_LIGHT_PURPLE;
		} else if (criterion == ScoreboardCriterion.TEAM_KILLS[14]) {
			return TEAM_KILL_YELLOW;
		} else if (criterion == ScoreboardCriterion.TEAM_KILLS[15]) {
			return TEAM_KILL_WHITE;
		} else if (criterion == ScoreboardCriterion.KILLED_BY_TEAMS[0]) {
			return KILLED_BY_TEAM_BLACK;
		} else if (criterion == ScoreboardCriterion.KILLED_BY_TEAMS[1]) {
			return KILLED_BY_TEAM_DARK_BLUE;
		} else if (criterion == ScoreboardCriterion.KILLED_BY_TEAMS[2]) {
			return KILLED_BY_TEAM_DARK_GREEN;
		} else if (criterion == ScoreboardCriterion.KILLED_BY_TEAMS[3]) {
			return KILLED_BY_TEAM_DARK_AQUA;
		} else if (criterion == ScoreboardCriterion.KILLED_BY_TEAMS[4]) {
			return KILLED_BY_TEAM_DARK_RED;
		} else if (criterion == ScoreboardCriterion.KILLED_BY_TEAMS[5]) {
			return KILLED_BY_TEAM_DARK_PURPLE;
		} else if (criterion == ScoreboardCriterion.KILLED_BY_TEAMS[6]) {
			return KILLED_BY_TEAM_GOLD;
		} else if (criterion == ScoreboardCriterion.KILLED_BY_TEAMS[7]) {
			return KILLED_BY_TEAM_GRAY;
		} else if (criterion == ScoreboardCriterion.KILLED_BY_TEAMS[8]) {
			return KILLED_BY_TEAM_DARK_GRAY;
		} else if (criterion == ScoreboardCriterion.KILLED_BY_TEAMS[9]) {
			return KILLED_BY_TEAM_BLUE;
		} else if (criterion == ScoreboardCriterion.KILLED_BY_TEAMS[10]) {
			return KILLED_BY_TEAM_GREEN;
		} else if (criterion == ScoreboardCriterion.KILLED_BY_TEAMS[11]) {
			return KILLED_BY_TEAM_AQUA;
		} else if (criterion == ScoreboardCriterion.KILLED_BY_TEAMS[12]) {
			return KILLED_BY_TEAM_RED;
		} else if (criterion == ScoreboardCriterion.KILLED_BY_TEAMS[13]) {
			return KILLED_BY_TEAM_LIGHT_PURPLE;
		} else if (criterion == ScoreboardCriterion.KILLED_BY_TEAMS[14]) {
			return KILLED_BY_TEAM_YELLOW;
		} else if (criterion == ScoreboardCriterion.KILLED_BY_TEAMS[15]) {
			return KILLED_BY_TEAM_WHITE;
		}
		return null;
	}
	
	public ScoreboardCriterion toScoreboardCriterion() {
		return switch (this) {
			case DUMMY -> ScoreboardCriterion.DUMMY;
			case TRIGGER -> ScoreboardCriterion.TRIGGER;
			case DEATH_COUNT -> ScoreboardCriterion.DEATH_COUNT;
			case PLAYER_KILL_COUNT -> ScoreboardCriterion.PLAYER_KILL_COUNT;
			case TOTAL_KILL_COUNT -> ScoreboardCriterion.TOTAL_KILL_COUNT;
			case HEALTH -> ScoreboardCriterion.HEALTH;
			case FOOD -> ScoreboardCriterion.FOOD;
			case AIR -> ScoreboardCriterion.AIR;
			case ARMOR -> ScoreboardCriterion.ARMOR;
			case XP -> ScoreboardCriterion.XP;
			case LEVEL -> ScoreboardCriterion.LEVEL;
			case TEAM_KILL_BLACK -> ScoreboardCriterion.TEAM_KILLS[0];
			case TEAM_KILL_DARK_BLUE -> ScoreboardCriterion.TEAM_KILLS[1];
			case TEAM_KILL_DARK_GREEN -> ScoreboardCriterion.TEAM_KILLS[2];
			case TEAM_KILL_DARK_AQUA -> ScoreboardCriterion.TEAM_KILLS[3];
			case TEAM_KILL_DARK_RED -> ScoreboardCriterion.TEAM_KILLS[4];
			case TEAM_KILL_DARK_PURPLE -> ScoreboardCriterion.TEAM_KILLS[5];
			case TEAM_KILL_GOLD -> ScoreboardCriterion.TEAM_KILLS[6];
			case TEAM_KILL_GRAY -> ScoreboardCriterion.TEAM_KILLS[7];
			case TEAM_KILL_DARK_GRAY -> ScoreboardCriterion.TEAM_KILLS[8];
			case TEAM_KILL_BLUE -> ScoreboardCriterion.TEAM_KILLS[9];
			case TEAM_KILL_GREEN -> ScoreboardCriterion.TEAM_KILLS[10];
			case TEAM_KILL_AQUA -> ScoreboardCriterion.TEAM_KILLS[11];
			case TEAM_KILL_RED -> ScoreboardCriterion.TEAM_KILLS[12];
			case TEAM_KILL_LIGHT_PURPLE -> ScoreboardCriterion.TEAM_KILLS[13];
			case TEAM_KILL_YELLOW -> ScoreboardCriterion.TEAM_KILLS[14];
			case TEAM_KILL_WHITE -> ScoreboardCriterion.TEAM_KILLS[15];
			case KILLED_BY_TEAM_BLACK -> ScoreboardCriterion.KILLED_BY_TEAMS[0];
			case KILLED_BY_TEAM_DARK_BLUE -> ScoreboardCriterion.KILLED_BY_TEAMS[1];
			case KILLED_BY_TEAM_DARK_GREEN -> ScoreboardCriterion.KILLED_BY_TEAMS[2];
			case KILLED_BY_TEAM_DARK_AQUA -> ScoreboardCriterion.KILLED_BY_TEAMS[3];
			case KILLED_BY_TEAM_DARK_RED -> ScoreboardCriterion.KILLED_BY_TEAMS[4];
			case KILLED_BY_TEAM_DARK_PURPLE -> ScoreboardCriterion.KILLED_BY_TEAMS[5];
			case KILLED_BY_TEAM_GOLD -> ScoreboardCriterion.KILLED_BY_TEAMS[6];
			case KILLED_BY_TEAM_GRAY -> ScoreboardCriterion.KILLED_BY_TEAMS[7];
			case KILLED_BY_TEAM_DARK_GRAY -> ScoreboardCriterion.KILLED_BY_TEAMS[8];
			case KILLED_BY_TEAM_BLUE -> ScoreboardCriterion.KILLED_BY_TEAMS[9];
			case KILLED_BY_TEAM_GREEN -> ScoreboardCriterion.KILLED_BY_TEAMS[10];
			case KILLED_BY_TEAM_AQUA -> ScoreboardCriterion.KILLED_BY_TEAMS[11];
			case KILLED_BY_TEAM_RED -> ScoreboardCriterion.KILLED_BY_TEAMS[12];
			case KILLED_BY_TEAM_LIGHT_PURPLE -> ScoreboardCriterion.KILLED_BY_TEAMS[13];
			case KILLED_BY_TEAM_YELLOW -> ScoreboardCriterion.KILLED_BY_TEAMS[14];
			case KILLED_BY_TEAM_WHITE -> ScoreboardCriterion.KILLED_BY_TEAMS[15];
		};
	}
}
