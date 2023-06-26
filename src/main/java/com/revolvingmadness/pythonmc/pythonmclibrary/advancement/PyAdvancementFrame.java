package com.revolvingmadness.pythonmc.pythonmclibrary.advancement;

import net.minecraft.advancement.AdvancementFrame;

public enum PyAdvancementFrame {
    TASK, CHALLENGE, GOAL;

    public static PyAdvancementFrame fromFrame(AdvancementFrame frame) {
        return switch (frame) {
            case TASK -> TASK;
            case CHALLENGE -> CHALLENGE;
            case GOAL -> GOAL;
        };
    }
}
