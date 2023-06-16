package com.revolvingmadness.pythonmc.pythonmclibrary.item;

import com.revolvingmadness.pythonmc.pythonmclibrary.item.enchantment.PyEnchantment;
import com.revolvingmadness.pythonmc.pythonmclibrary.item.enchantment.PyEnchantments;
import com.revolvingmadness.pythonmc.pythonmclibrary.server.text.PyText;
import com.revolvingmadness.pythonmc.util.NbtCompoundUtil;
import com.revolvingmadness.pythonmc.util.NbtElementUtil;
import net.minecraft.item.Item;
import net.minecraft.item.ItemStack;
import net.minecraft.nbt.NbtCompound;
import net.minecraft.text.Text;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class PyItemStack {
	final ItemStack itemStack;
	final Item item;

	public PyItemStack(ItemStack itemStack) {
		this.itemStack = itemStack;
		this.item = itemStack.getItem();
	}

	public PyItemStack(PyItems item, Number count, Map<String, Object> nbt) {
		this.itemStack = new ItemStack(item.toItem(), count.intValue());
		this.itemStack.setNbt(NbtCompoundUtil.fromMap(nbt));
		this.item = this.itemStack.getItem();
	}

	public PyItemStack(PyItems item, Map<String, Object> nbt) {
		this(item, 1, nbt);
	}

	public PyItemStack(PyItems item, Number count) {
		this(item, count.intValue(), new HashMap<>());
	}

	public PyItemStack(PyItems item) {
		this(item, 1);
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

	public int getMaxCount() {
		return this.itemStack.getMaxCount();
	}

	public int getMaxDamage() {
		return this.itemStack.getMaxDamage();
	}

	public String getName() {
		return this.itemStack.getName().getString();
	}

	public Map<String, Object> getNbt() {
		NbtCompound nbtCompound = this.itemStack.getNbt();
		if (nbtCompound == null) {
			return new HashMap<>();
		}
		// noinspection unchecked
		return (Map<String, Object>) NbtElementUtil.toObject(nbtCompound);
	}

	public PyItemRarity getRarity() {
		return PyItemRarity.fromRarity(this.itemStack.getRarity());
	}

	public int getRepairCost() {
		return this.itemStack.getRepairCost();
	}

	public boolean hasCustomName() {
		return this.itemStack.hasCustomName();
	}

	public boolean hasEnchantments() {
		return this.itemStack.hasEnchantments();
	}

	public boolean hasGlint() {
		return this.itemStack.hasGlint();
	}

	public boolean hasNbt() {
		return this.itemStack.hasNbt();
	}

	public void increment(Number amount) {
		this.itemStack.increment(amount.intValue());
	}

	public boolean isDamageable() {
		return this.itemStack.isDamageable();
	}

	public boolean isDamaged() {
		return this.itemStack.isDamaged();
	}

	public boolean isEnchantable() {
		return this.itemStack.isEnchantable();
	}

	public boolean isFood() {
		return this.itemStack.isFood();
	}

	public boolean isItemBarVisible() {
		return this.itemStack.isItemBarVisible();
	}

	public boolean isStackable() {
		return this.itemStack.isStackable();
	}

	public void removeCustomName() {
		this.itemStack.removeCustomName();
	}

	public void setCount(Number count) {
		this.itemStack.setCount(count.intValue());
	}

	public void setCustomName(String name) {
		this.itemStack.setCustomName(Text.of(name));
	}

	public void setCustomName(PyText text) {
		this.itemStack.setCustomName(text.text);
	}

	public void setDamage(Number damage) {
		this.itemStack.setDamage(damage.intValue());
	}

	public void setRepairCost(Number repairCost) {
		this.itemStack.setRepairCost(repairCost.intValue());
	}


	@Override
	public String toString() {
		return Text.translatable(this.itemStack.getTranslationKey()).getString();
	}
}
