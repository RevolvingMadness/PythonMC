package com.revolvingmadness.pythonmc.pythonmclibrary.player;

import com.revolvingmadness.pythonmc.pythonmclibrary.item.PyItemStack;
import net.minecraft.entity.player.PlayerInventory;

import java.util.ArrayList;
import java.util.List;

public class PyPlayerInventory {
    public final List<PyItemStack> main;
    public final List<PyItemStack> armor;
    public final List<PyItemStack> offHand;
    public final int selectedSlot;
    final PlayerInventory inventory;

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

    public void clear() {
        this.inventory.clear();
    }

    public boolean contains(PyItemStack stack) {
        return this.inventory.contains(stack.itemStack);
    }

    public void dropAll() {
        this.inventory.dropAll();
    }

    public void dropSelectedItem(boolean dropEntireStack) {
        this.inventory.dropSelectedItem(dropEntireStack);
    }

    public PyItemStack getArmorStack(Number slot) {
        return new PyItemStack(this.inventory.getArmorStack(slot.intValue()));
    }

    public int getEmptySlot() {
        return this.inventory.getEmptySlot();
    }

    public PyItemStack getMainHandStack() {
        return new PyItemStack(this.inventory.getMainHandStack());
    }

    public int getSlotWithStack(PyItemStack stack) {
        return this.inventory.getSlotWithStack(stack.itemStack);
    }

    public PyItemStack getStack(Number slot) {
        return new PyItemStack(this.inventory.getStack(slot.intValue()));
    }

    public int indexOf(PyItemStack stack) {
        return this.inventory.indexOf(stack.itemStack);
    }

    public void insertStack(PyItemStack stack) {
        this.insertStack(-1, stack);
    }

    public void insertStack(Number slot, PyItemStack stack) {
        this.inventory.insertStack(slot.intValue(), stack.itemStack);
    }

    public boolean isEmpty() {
        return this.inventory.isEmpty();
    }

    public void removeOne(PyItemStack stack) {
        this.inventory.removeOne(stack.itemStack);
    }

    public void removeStack(Number slot, Number amount) {
        this.inventory.removeStack(slot.intValue(), amount.intValue());
    }

    public void removeStack(Number slot) {
        this.inventory.removeStack(slot.intValue());
    }

    public void setStack(Number slot, PyItemStack stack) {
        this.inventory.setStack(slot.intValue(), stack.itemStack);
    }
}
