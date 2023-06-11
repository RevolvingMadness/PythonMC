package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.item.Item;
import net.minecraft.item.ItemStack;

public class PyItemStack {
	ItemStack itemStack;
	Item item;
	
	public PyItemStack(ItemStack itemStack) {
		this.itemStack = itemStack;
		this.item = itemStack.getItem();
	}
	
	public void decrement(int amount) {
		this.itemStack.decrement(amount);
	}
	
	public void addEnchantment(PyEnchantments enchantment, int level) {
		this.itemStack.addEnchantment(enchantment.toEnchantment(), level);
	}
}
