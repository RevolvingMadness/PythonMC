package com.revolvingmadness.pythonmc.pythonmclibrary.player;

import com.revolvingmadness.pythonmc.pythonmclibrary.item.PyItemStack;
import net.minecraft.inventory.EnderChestInventory;

import java.util.ArrayList;
import java.util.List;

public class PyEnderChestInventory {
    public final List<PyItemStack> stacks;
    final EnderChestInventory enderChestInventory;

    public PyEnderChestInventory(EnderChestInventory enderChestInventory) {
        this.enderChestInventory = enderChestInventory;
        this.stacks = new ArrayList<>();
        enderChestInventory.stacks.forEach(stack -> this.stacks.add(new PyItemStack(stack)));
    }
}
