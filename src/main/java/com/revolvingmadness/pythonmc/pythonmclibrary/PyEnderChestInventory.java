package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.inventory.EnderChestInventory;

import java.util.ArrayList;
import java.util.List;

public class PyEnderChestInventory {
    final EnderChestInventory enderChestInventory;
    public final List<PyItemStack> stacks;

    public PyEnderChestInventory(EnderChestInventory enderChestInventory) {
        this.enderChestInventory = enderChestInventory;
        this.stacks = new ArrayList<>();
        enderChestInventory.stacks.forEach(stack -> this.stacks.add(new PyItemStack(stack)));
    }
}
