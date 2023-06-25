package com.revolvingmadness.pythonmc.pythonmclibrary.item.enchantment;

import net.minecraft.enchantment.Enchantment;
import net.minecraft.registry.Registries;
import net.minecraft.text.Text;
import net.minecraft.util.Identifier;

import java.util.Map;
import java.util.Objects;

public class PyEnchantment {
	final Enchantment enchantment;
	public final int level;
	public final PyEnchantmentRarity rarity;
	
	public PyEnchantment(Enchantment enchantment, Number level) {
		this.enchantment = enchantment;
		this.rarity = PyEnchantmentRarity.fromRarity(enchantment.getRarity());
		this.level = level.intValue();
	}
	
	public PyEnchantment(Enchantment enchantment) {
		this(enchantment, 1);
	}
	
	public static PyEnchantment fromNbt(Map<String, Object> nbtEnchantment) {
		String enchantment = (String) nbtEnchantment.get("id");
		String[] splitEnchantment = enchantment.split(":");
		Identifier enchantmentIdentifier = new Identifier(splitEnchantment[0], splitEnchantment[1]);
		return new PyEnchantment(Objects.requireNonNull(Registries.ENCHANTMENT.get(enchantmentIdentifier)), (Number) nbtEnchantment.get("lvl"));
	}
	
	@Override
	public String toString() {
		return Text.translatable(this.enchantment.getTranslationKey()).getString() + " " + this.level;
	}
}
