package com.revolvingmadness.pythonmc.pythonmclibrary.scoreboard;

import com.revolvingmadness.pythonmc.pythonmclibrary.scoreboard.rules.PyCollisionRules;
import com.revolvingmadness.pythonmc.pythonmclibrary.scoreboard.rules.PyVisibilityRules;
import com.revolvingmadness.pythonmc.pythonmclibrary.server.text.PyFormatting;
import com.revolvingmadness.pythonmc.pythonmclibrary.server.text.PyText;
import net.minecraft.scoreboard.Team;

import java.util.List;

public class PyTeam {
	Team team;

	public PyTeam(Team team) {
		this.team = team;
	}

	public void setSuffix(PyText suffix) {
		this.team.setSuffix(suffix.text);
	}

	public void setShowFriendlyInvisibles(boolean showFriendlyInvisibles) {
		this.team.setShowFriendlyInvisibles(showFriendlyInvisibles);
	}

	public void setPrefix(PyText prefix) {
		this.team.setPrefix(prefix.text);
	}

	public boolean shouldShowFriendlyInvisibles() {
		return this.team.shouldShowFriendlyInvisibles();
	}

	public void setNameTagVisibilityRule(PyVisibilityRules nameTagVisibilityRule) {
		this.team.setNameTagVisibilityRule(nameTagVisibilityRule.toVisibilityRule());
	}

	public void setFriendlyFireAllowed(boolean friendlyFireAllowed) {
		this.team.setFriendlyFireAllowed(friendlyFireAllowed);
	}

	public void setDisplayName(PyText displayName) {
		this.team.setDisplayName(displayName.text);
	}

	public void setDeathMessageVisibilityRule(PyVisibilityRules deathMessageVisibilityRule) {
		this.team.setDeathMessageVisibilityRule(deathMessageVisibilityRule.toVisibilityRule());
	}

	public void setColor(PyFormatting formatting) {
		this.team.setColor(formatting.toFormatting());
	}

	public void setCollisionRule(PyCollisionRules collisionRule) {
		this.team.setCollisionRule(collisionRule.toCollisionRule());
	}

	public boolean isFriendlyFireAllowed() {
		return this.team.isFriendlyFireAllowed();
	}

	public PyText getSuffix() {
		return new PyText(this.team.getSuffix());
	}

	public List<String> getPlayerList() {
		return this.team.getPlayerList().stream().toList();
	}

	public PyText getPrefix() {
		return new PyText(this.team.getPrefix());
	}

	public PyVisibilityRules getNameTagVisibilityRule() {
		return PyVisibilityRules.fromVisibilityRule(this.team.getNameTagVisibilityRule());
	}

	public String getName() {
		return this.team.getName();
	}

	public PyText getDisplayName() {
		return new PyText(this.team.getDisplayName());
	}

	public PyVisibilityRules getDeathMessageVisibilityRule() {
		return PyVisibilityRules.fromVisibilityRule(this.team.getDeathMessageVisibilityRule());
	}

	public PyFormatting getColor() {
		return PyFormatting.fromFormatting(this.team.getColor());
	}

	public PyCollisionRules getCollisionRule() {
		return PyCollisionRules.fromCollisionRule(this.team.getCollisionRule());
	}
}
