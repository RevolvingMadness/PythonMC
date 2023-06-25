package com.revolvingmadness.pythonmc.pythonmclibrary.scoreboard;

import com.revolvingmadness.pythonmc.pythonmclibrary.entity.PyEntity;
import com.revolvingmadness.pythonmc.pythonmclibrary.server.text.PyText;
import net.minecraft.scoreboard.Scoreboard;

import java.util.ArrayList;
import java.util.List;

public class PyScoreboard {
	Scoreboard scoreboard;
	
	public PyScoreboard(Scoreboard scoreboard) {
		this.scoreboard = scoreboard;
	}
	
	public List<PyTeam> getTeams() {
		List<PyTeam> result = new ArrayList<>();
		this.scoreboard.getTeams().forEach(team -> result.add(new PyTeam(team)));
		return result;
	}
	
	public void resetPlayerScore(String playerName, PyScoreboardObjective objective) {
		this.scoreboard.resetPlayerScore(playerName, objective.objective);
	}
	
	public List<PyScoreboardPlayerScore> getAllPlayerScores(PyScoreboardObjective objective) {
		List<PyScoreboardPlayerScore> result = new ArrayList<>();
		this.scoreboard.getAllPlayerScores(objective.objective).forEach(scoreboardPlayerScore -> result.add(new PyScoreboardPlayerScore(scoreboardPlayerScore)));
		return result;
	}
	
	public void removeTeam(PyTeam team) {
		this.scoreboard.removeTeam(team.team);
	}
	
	public boolean containsObjective(String name) {
		return this.scoreboard.containsObjective(name);
	}
	
	public void addObjective(String name, PyScoreboardCriterions criterion, PyText displayName, PyRenderTypes renderType) {
		this.scoreboard.addObjective(name, criterion.toScoreboardCriterion(), displayName.text, renderType.toRenderType());
	}
	
	public void removePlayerFromTeam(String playerName, PyTeam team) {
		this.scoreboard.removePlayerFromTeam(playerName, team.team);
	}
	
	public List<PyScoreboardObjective> getObjectives() {
		List<PyScoreboardObjective> result = new ArrayList<>();
		this.scoreboard.getObjectives().forEach(objective -> result.add(new PyScoreboardObjective(objective)));
		return result;
	}
	
	public void addPlayerToTeam(String playerName, PyTeam team) {
		this.scoreboard.addPlayerToTeam(playerName, team.team);
	}
	
	public void clearPlayerTeam(String playerName) {
		this.scoreboard.clearPlayerTeam(playerName);
	}
	
	public List<String> getObjectiveNames() {
		return this.scoreboard.getObjectiveNames().stream().toList();
	}
	
	public PyTeam getTeam(String name) {
		return new PyTeam(this.scoreboard.getTeam(name));
	}
	
	public void resetEntityScore(PyEntity entity) {
		this.scoreboard.resetEntityScore(entity.entity);
	}
	
	public PyScoreboardObjective getObjective(String name) {
		return new PyScoreboardObjective(this.scoreboard.getObjective(name));
	}
	
	public void addTeam(String name) {
		this.scoreboard.addTeam(name);
	}
	
	public List<String> getTeamNames() {
		return this.scoreboard.getTeamNames().stream().toList();
	}
	
	public void removeObjective(PyScoreboardObjective objective) {
		this.scoreboard.removeObjective(objective.objective);
	}
	
	public PyScoreboardPlayerScore getPlayerScore(String name, PyScoreboardObjective objective) {
		return new PyScoreboardPlayerScore(this.scoreboard.getPlayerScore(name, objective.objective));
	}
	
	public PyTeam getPlayerTeam(String name) {
		return new PyTeam(this.scoreboard.getPlayerTeam(name));
	}
}
