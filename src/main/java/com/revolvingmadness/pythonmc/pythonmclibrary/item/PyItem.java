package com.revolvingmadness.pythonmc.pythonmclibrary.item;

import net.minecraft.item.Item;
import net.minecraft.item.ItemStack;
import net.minecraft.text.Text;

public class PyItem {
    public final Item item;
    public final String name;
    final ItemStack itemStack;

    public PyItem(PyItems item) {
        this(item.toItem());
    }

    public PyItem(Item item) {
        this.item = item;
        this.itemStack = item.getDefaultStack();
        this.name = Text.translatable(item.getTranslationKey()).getString();
    }

    @Override
    public String toString() {
        return this.name;
    }
}
