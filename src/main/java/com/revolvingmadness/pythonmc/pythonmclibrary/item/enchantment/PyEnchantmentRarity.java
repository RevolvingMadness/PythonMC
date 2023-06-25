package com.revolvingmadness.pythonmc.pythonmclibrary.item.enchantment;

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
}
