package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.util.Rarity;

public enum PyItemRarity {
    COMMON, UNCOMMON, RARE, EPIC;

    public static PyItemRarity fromRarity(Rarity rarity) {
        return switch (rarity) {
            case COMMON -> COMMON;
            case UNCOMMON -> UNCOMMON;
            case RARE -> RARE;
            case EPIC -> EPIC;
        };
    }

    public Rarity toRarity() {
        return switch (this) {
            case COMMON -> Rarity.COMMON;
            case UNCOMMON -> Rarity.UNCOMMON;
            case RARE -> Rarity.RARE;
            case EPIC -> Rarity.EPIC;
        };
    }
}
