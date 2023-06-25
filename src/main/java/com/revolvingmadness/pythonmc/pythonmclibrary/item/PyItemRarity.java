package com.revolvingmadness.pythonmc.pythonmclibrary.item;

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
}
