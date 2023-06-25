package com.revolvingmadness.pythonmc.pythonmclibrary.scoreboard;

import com.revolvingmadness.pythonmc.pythonmclibrary.scoreboard.rules.PyCollisionRules;
import com.revolvingmadness.pythonmc.pythonmclibrary.scoreboard.rules.PyVisibilityRules;
import com.revolvingmadness.pythonmc.pythonmclibrary.server.text.PyFormatting;
import com.revolvingmadness.pythonmc.pythonmclibrary.server.text.PyText;
import net.minecraft.scoreboard.Team;

import java.util.List;

public class PyTeam {
    final Team team;

    public PyTeam(Team team) {
        this.team = team;
    }

    public void setShowFriendlyInvisibles(boolean showFriendlyInvisibles) {
        this.team.setShowFriendlyInvisibles(showFriendlyInvisibles);
    }

    public boolean shouldShowFriendlyInvisibles() {
        return this.team.shouldShowFriendlyInvisibles();
    }

    public boolean isFriendlyFireAllowed() {
        return this.team.isFriendlyFireAllowed();
    }

    public void setFriendlyFireAllowed(boolean friendlyFireAllowed) {
        this.team.setFriendlyFireAllowed(friendlyFireAllowed);
    }

    public PyText getSuffix() {
        return new PyText(this.team.getSuffix());
    }

    public void setSuffix(PyText suffix) {
        this.team.setSuffix(suffix.text);
    }

    public List<String> getPlayerList() {
        return this.team.getPlayerList().stream().toList();
    }

    public PyText getPrefix() {
        return new PyText(this.team.getPrefix());
    }

    public void setPrefix(PyText prefix) {
        this.team.setPrefix(prefix.text);
    }

    public PyVisibilityRules getNameTagVisibilityRule() {
        return PyVisibilityRules.fromVisibilityRule(this.team.getNameTagVisibilityRule());
    }

    public void setNameTagVisibilityRule(PyVisibilityRules nameTagVisibilityRule) {
        this.team.setNameTagVisibilityRule(nameTagVisibilityRule.toVisibilityRule());
    }

    public String getName() {
        return this.team.getName();
    }

    public PyText getDisplayName() {
        return new PyText(this.team.getDisplayName());
    }

    public void setDisplayName(PyText displayName) {
        this.team.setDisplayName(displayName.text);
    }

    public PyVisibilityRules getDeathMessageVisibilityRule() {
        return PyVisibilityRules.fromVisibilityRule(this.team.getDeathMessageVisibilityRule());
    }

    public void setDeathMessageVisibilityRule(PyVisibilityRules deathMessageVisibilityRule) {
        this.team.setDeathMessageVisibilityRule(deathMessageVisibilityRule.toVisibilityRule());
    }

    public PyFormatting getColor() {
        return PyFormatting.fromFormatting(this.team.getColor());
    }

    public void setColor(PyFormatting formatting) {
        this.team.setColor(formatting.toFormatting());
    }

    public PyCollisionRules getCollisionRule() {
        return PyCollisionRules.fromCollisionRule(this.team.getCollisionRule());
    }

    public void setCollisionRule(PyCollisionRules collisionRule) {
        this.team.setCollisionRule(collisionRule.toCollisionRule());
    }
}
