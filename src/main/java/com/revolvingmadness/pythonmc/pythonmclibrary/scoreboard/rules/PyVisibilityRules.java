package com.revolvingmadness.pythonmc.pythonmclibrary.scoreboard.rules;

import net.minecraft.scoreboard.AbstractTeam;

public enum PyVisibilityRules {
    ALWAYS, NEVER, HIDE_FOR_OTHER_TEAMS, HIDE_FOR_OWN_TEAM;

    public static PyVisibilityRules fromVisibilityRule(AbstractTeam.VisibilityRule visibilityRule) {
        return switch (visibilityRule) {
            case ALWAYS -> ALWAYS;
            case NEVER -> NEVER;
            case HIDE_FOR_OTHER_TEAMS -> HIDE_FOR_OTHER_TEAMS;
            case HIDE_FOR_OWN_TEAM -> HIDE_FOR_OWN_TEAM;
        };
    }

    public AbstractTeam.VisibilityRule toVisibilityRule() {
        return switch (this) {
            case ALWAYS -> AbstractTeam.VisibilityRule.ALWAYS;
            case NEVER -> AbstractTeam.VisibilityRule.NEVER;
            case HIDE_FOR_OTHER_TEAMS -> AbstractTeam.VisibilityRule.HIDE_FOR_OTHER_TEAMS;
            case HIDE_FOR_OWN_TEAM -> AbstractTeam.VisibilityRule.HIDE_FOR_OWN_TEAM;
        };
    }
}
