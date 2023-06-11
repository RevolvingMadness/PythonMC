package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.item.Item;
import net.minecraft.item.ItemStack;

public class PyItemStack {
    final ItemStack itemStack;
    final Item item;

    public PyItemStack(ItemStack itemStack) {
        this.itemStack = itemStack;
        this.item = itemStack.getItem();
    }

    public void decrement(Number amount) {
        this.itemStack.decrement(amount.intValue());
    }

    public void addEnchantment(PyEnchantments enchantment, Number level) {
        this.itemStack.addEnchantment(enchantment.toEnchantment(), level.intValue());
    }
}
