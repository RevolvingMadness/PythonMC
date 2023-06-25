package com.revolvingmadness.pythonmc.pythonmclibrary.scoreboard.rules;

import net.minecraft.scoreboard.AbstractTeam;

public enum PyCollisionRules {
    ALWAYS, NEVER, PUSH_OTHER_TEAMS, PUSH_OWN_TEAM;

    public static PyCollisionRules fromCollisionRule(AbstractTeam.CollisionRule collisionRule) {
        return switch (collisionRule) {
            case ALWAYS -> ALWAYS;
            case NEVER -> NEVER;
            case PUSH_OTHER_TEAMS -> PUSH_OTHER_TEAMS;
            case PUSH_OWN_TEAM -> PUSH_OWN_TEAM;
        };
    }

    public AbstractTeam.CollisionRule toCollisionRule() {
        return switch (this) {
            case ALWAYS -> AbstractTeam.CollisionRule.ALWAYS;
            case NEVER -> AbstractTeam.CollisionRule.NEVER;
            case PUSH_OTHER_TEAMS -> AbstractTeam.CollisionRule.PUSH_OTHER_TEAMS;
            case PUSH_OWN_TEAM -> AbstractTeam.CollisionRule.PUSH_OWN_TEAM;
        };
    }
}
