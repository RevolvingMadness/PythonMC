package com.revolvingmadness.pythonmc.pythonmclibrary.advancement;

import net.minecraft.server.command.AdvancementCommand;

public enum PyOperation {
    GRANT, REVOKE;

    public AdvancementCommand.Operation toOperation() {
        return switch (this) {
            case GRANT -> AdvancementCommand.Operation.GRANT;
            case REVOKE -> AdvancementCommand.Operation.REVOKE;
        };
    }
}
