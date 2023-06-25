package com.revolvingmadness.pythonmc.pythonmclibrary.item.enchantment;

import net.minecraft.enchantment.Enchantment;
import net.minecraft.enchantment.Enchantments;

public enum PyEnchantments {
    PROTECTION, FIRE_PROTECTION, FEATHER_FALLING, BLAST_PROTECTION, PROJECTILE_PROTECTION, RESPIRATION, AQUA_AFFINITY, THORNS, DEPTH_STRIDER, FROST_WALKER, BINDING_CURSE, SOUL_SPEED, SWIFT_SNEAK, SHARPNESS, SMITE, BANE_OF_ARTHROPODS, KNOCKBACK, FIRE_ASPECT, LOOTING, SWEEPING, EFFICIENCY, SILK_TOUCH, UNBREAKING, FORTUNE, POWER, PUNCH, FLAME, INFINITY, LUCK_OF_THE_SEA, LURE, LOYALTY, IMPALING, RIPTIDE, CHANNELING, MULTISHOT, QUICK_CHARGE, PIERCING, MENDING, VANISHING_CURSE;

    public Enchantment toEnchantment() {
        return switch (this) {
            case PROTECTION -> Enchantments.PROTECTION;
            case FIRE_PROTECTION -> Enchantments.FIRE_PROTECTION;
            case FEATHER_FALLING -> Enchantments.FEATHER_FALLING;
            case BLAST_PROTECTION -> Enchantments.BLAST_PROTECTION;
            case PROJECTILE_PROTECTION -> Enchantments.PROJECTILE_PROTECTION;
            case RESPIRATION -> Enchantments.RESPIRATION;
            case AQUA_AFFINITY -> Enchantments.AQUA_AFFINITY;
            case THORNS -> Enchantments.THORNS;
            case DEPTH_STRIDER -> Enchantments.DEPTH_STRIDER;
            case FROST_WALKER -> Enchantments.FROST_WALKER;
            case BINDING_CURSE -> Enchantments.BINDING_CURSE;
            case SOUL_SPEED -> Enchantments.SOUL_SPEED;
            case SWIFT_SNEAK -> Enchantments.SWIFT_SNEAK;
            case SHARPNESS -> Enchantments.SHARPNESS;
            case SMITE -> Enchantments.SMITE;
            case BANE_OF_ARTHROPODS -> Enchantments.BANE_OF_ARTHROPODS;
            case KNOCKBACK -> Enchantments.KNOCKBACK;
            case FIRE_ASPECT -> Enchantments.FIRE_ASPECT;
            case LOOTING -> Enchantments.LOOTING;
            case SWEEPING -> Enchantments.SWEEPING;
            case EFFICIENCY -> Enchantments.EFFICIENCY;
            case SILK_TOUCH -> Enchantments.SILK_TOUCH;
            case UNBREAKING -> Enchantments.UNBREAKING;
            case FORTUNE -> Enchantments.FORTUNE;
            case POWER -> Enchantments.POWER;
            case PUNCH -> Enchantments.PUNCH;
            case FLAME -> Enchantments.FLAME;
            case INFINITY -> Enchantments.INFINITY;
            case LUCK_OF_THE_SEA -> Enchantments.LUCK_OF_THE_SEA;
            case LURE -> Enchantments.LURE;
            case LOYALTY -> Enchantments.LOYALTY;
            case IMPALING -> Enchantments.IMPALING;
            case RIPTIDE -> Enchantments.RIPTIDE;
            case CHANNELING -> Enchantments.CHANNELING;
            case MULTISHOT -> Enchantments.MULTISHOT;
            case QUICK_CHARGE -> Enchantments.QUICK_CHARGE;
            case PIERCING -> Enchantments.PIERCING;
            case MENDING -> Enchantments.MENDING;
            case VANISHING_CURSE -> Enchantments.VANISHING_CURSE;
        };
    }
}
