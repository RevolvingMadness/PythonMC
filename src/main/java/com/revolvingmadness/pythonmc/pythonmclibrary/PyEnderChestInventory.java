package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.inventory.EnderChestInventory;

import java.util.ArrayList;
import java.util.List;

public class PyEnderChestInventory {
	EnderChestInventory enderChestInventory;
	public List<PyItemStack> stacks;
	
	public PyEnderChestInventory(EnderChestInventory enderChestInventory) {
		this.enderChestInventory = enderChestInventory;
		stacks = new ArrayList<>();
		enderChestInventory.stacks.forEach(stack -> stacks.add(new PyItemStack(stack)));
	}
}
