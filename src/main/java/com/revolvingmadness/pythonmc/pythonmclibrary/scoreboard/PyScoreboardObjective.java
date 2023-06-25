package com.revolvingmadness.pythonmc.pythonmclibrary.scoreboard;

import com.revolvingmadness.pythonmc.pythonmclibrary.server.text.PyText;
import net.minecraft.scoreboard.ScoreboardObjective;

public class PyScoreboardObjective {
    final ScoreboardObjective objective;

    public PyScoreboardObjective(ScoreboardObjective objective) {
        this.objective = objective;
    }

    public PyScoreboardCriterions getCriterion() {
        return PyScoreboardCriterions.fromScoreboardCriterion(this.objective.getCriterion());
    }

    public PyText getDisplayName() {
        return new PyText(this.objective.getDisplayName());
    }

    public void setDisplayName(PyText displayName) {
        this.objective.setDisplayName(displayName.text);
    }

    public String getName() {
        return this.objective.getName();
    }

    public PyRenderTypes getRenderType() {
        return PyRenderTypes.fromRenderType(this.objective.getRenderType());
    }

    public void setRenderType(PyRenderTypes renderType) {
        this.objective.setRenderType(renderType.toRenderType());
    }
}
