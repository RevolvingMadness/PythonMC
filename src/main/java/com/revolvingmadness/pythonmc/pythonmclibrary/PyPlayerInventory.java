package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.entity.player.PlayerInventory;

import java.util.ArrayList;
import java.util.List;

public class PyPlayerInventory {
	PlayerInventory inventory;
	public List<PyItemStack> main;
	public List<PyItemStack> armor;
	public List<PyItemStack> offHand;
	public int selectedSlot;
	
	public PyPlayerInventory(PlayerInventory inventory) {
		this.inventory = inventory;
		this.main = new ArrayList<>();
		inventory.main.forEach(itemStack -> this.main.add(new PyItemStack(itemStack)));
		this.armor = new ArrayList<>();
		inventory.armor.forEach(itemStack -> this.armor.add(new PyItemStack(itemStack)));
		this.offHand = new ArrayList<>();
		inventory.offHand.forEach(itemStack -> this.offHand.add(new PyItemStack(itemStack)));
		this.selectedSlot = inventory.selectedSlot;
	}
}
