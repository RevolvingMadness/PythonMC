package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.enchantment.Enchantment;

public enum PyEnchantmentRarity {
    COMMON, UNCOMMON, RARE, VERY_RARE;

    public static PyEnchantmentRarity fromRarity(Enchantment.Rarity rarity) {
        return switch (rarity) {
            case COMMON -> COMMON;
            case UNCOMMON -> UNCOMMON;
            case RARE -> RARE;
            case VERY_RARE -> VERY_RARE;
        };
    }

    public Enchantment.Rarity toRarity() {
        return switch (this) {
            case COMMON -> Enchantment.Rarity.COMMON;
            case UNCOMMON -> Enchantment.Rarity.UNCOMMON;
            case RARE -> Enchantment.Rarity.RARE;
            case VERY_RARE -> Enchantment.Rarity.VERY_RARE;
        };
    }
}
