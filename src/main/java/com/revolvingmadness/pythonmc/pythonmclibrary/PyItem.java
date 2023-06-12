package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.item.Item;
import net.minecraft.item.ItemStack;
import net.minecraft.text.Text;

public class PyItem {
    final Item item;
    final ItemStack itemStack;
    public final String name;

    public PyItem(Item item) {
        this.item = item;
        this.itemStack = item.getDefaultStack();
        this.name = Text.translatable(item.getTranslationKey()).getString();
    }

    public PyItem(PyItems item) {
        this.item = item.toItem();
        this.itemStack = this.item.getDefaultStack();
        this.name = Text.translatable(this.item.getTranslationKey()).getString();
    }

    @Override
    public String toString() {
        return this.name;
    }
}
