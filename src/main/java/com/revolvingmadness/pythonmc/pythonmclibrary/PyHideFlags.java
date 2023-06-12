package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.item.ItemStack;

public enum PyHideFlags {
    ENCHANTMENTS, MODIFIERS, UNBREAKABLE, CAN_DESTROY, CAN_PLACE, ADDITIONAL, DYE, UPGRADES;

    public ItemStack.TooltipSection toHideFlag() {
        return switch (this) {
            case ENCHANTMENTS -> ItemStack.TooltipSection.ENCHANTMENTS;
            case MODIFIERS -> ItemStack.TooltipSection.MODIFIERS;
            case UNBREAKABLE -> ItemStack.TooltipSection.UNBREAKABLE;
            case CAN_DESTROY -> ItemStack.TooltipSection.CAN_DESTROY;
            case CAN_PLACE -> ItemStack.TooltipSection.CAN_PLACE;
            case ADDITIONAL -> ItemStack.TooltipSection.ADDITIONAL;
            case DYE -> ItemStack.TooltipSection.DYE;
            case UPGRADES -> ItemStack.TooltipSection.UPGRADES;
        };
    }
}
