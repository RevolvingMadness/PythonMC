package com.revolvingmadness.pythonmc.pythonmclibrary;

import com.revolvingmadness.pythonmc.util.NbtElementUtil;
import net.minecraft.item.Item;
import net.minecraft.item.ItemStack;
import net.minecraft.text.Text;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

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

    public void addHideFlag(PyHideFlags hideFlag) {
        this.itemStack.addHideFlag(hideFlag.toHideFlag());
    }

    public int getCount() {
        return this.itemStack.getCount();
    }

    public int getDamage() {
        return this.itemStack.getDamage();
    }

    public List<PyEnchantment> getEnchantments() {
        List<PyEnchantment> result = new ArrayList<>();
        // noinspection unchecked
        List<Map<String, Object>> nbtEnchantments = (List<Map<String, Object>>) NbtElementUtil.toObject(this.itemStack.getEnchantments());
        nbtEnchantments.forEach(nbtEnchantment -> result.add(PyEnchantment.fromNbt(nbtEnchantment)));
        return result;
    }

    @Override
    public String toString() {
        return Text.translatable(this.itemStack.getTranslationKey()).getString();
    }
}
