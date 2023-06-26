package com.revolvingmadness.pythonmc.pythonmclibrary.advancement;

import net.minecraft.server.command.AdvancementCommand;

public enum PySelection {
    ONLY, THROUGH, FROM, UNTIL, EVERYTHING;

    public AdvancementCommand.Selection toSelection() {
        return switch (this) {
            case ONLY -> AdvancementCommand.Selection.ONLY;
            case THROUGH -> AdvancementCommand.Selection.THROUGH;
            case FROM -> AdvancementCommand.Selection.FROM;
            case UNTIL -> AdvancementCommand.Selection.UNTIL;
            case EVERYTHING -> AdvancementCommand.Selection.EVERYTHING;
        };
    }
}
