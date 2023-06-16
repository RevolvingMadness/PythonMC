package com.revolvingmadness.pythonmc.pythonmclibrary.player;

import com.revolvingmadness.pythonmc.pythonmclibrary.block.PyBlockState;
import com.revolvingmadness.pythonmc.pythonmclibrary.block.PyBlocks;
import com.revolvingmadness.pythonmc.pythonmclibrary.entity.PyArm;
import com.revolvingmadness.pythonmc.pythonmclibrary.entity.PyEntity;
import com.revolvingmadness.pythonmc.pythonmclibrary.entity.PyLivingEntity;
import com.revolvingmadness.pythonmc.pythonmclibrary.server.text.PyText;
import com.revolvingmadness.pythonmc.util.NbtCompoundUtil;
import com.revolvingmadness.pythonmc.util.NbtElementUtil;
import net.minecraft.entity.player.PlayerEntity;
import net.minecraft.text.Text;

import java.util.Map;

public class PyPlayerEntity extends PyLivingEntity {
	final PlayerEntity playerEntity;

	public PyPlayerEntity(PlayerEntity playerEntity) {
		super(playerEntity);
		this.playerEntity = playerEntity;
	}

	public boolean isMainPlayer() {
		return this.playerEntity.isMainPlayer();
	}

	public float getAttackCooldownProgress(Number baseTime) {
		return this.playerEntity.getAttackCooldownProgress(baseTime.floatValue());
	}

	public void addExhaustion(Number exhaustion) {
		this.playerEntity.addExhaustion(exhaustion.floatValue());
	}

	public boolean isUsingSpyglass() {
		return this.playerEntity.isUsingSpyglass();
	}

	public boolean canFoodHeal() {
		return this.playerEntity.canFoodHeal();
	}

	public PyPlayerInventory getInventory() {
		return new PyPlayerInventory(this.playerEntity.getInventory());
	}

	public void addScore(Number score) {
		this.playerEntity.addScore(score.intValue());
	}

	public boolean isCreative() {
		return this.playerEntity.isCreative();
	}

	public Map<String, Object> getShoulderEntityLeft() {
		// noinspection unchecked
		return (Map<String, Object>) NbtElementUtil.toObject(this.playerEntity.getShoulderEntityLeft());
	}

	public Map<String, Object> getShoulderEntityRight() {
		// noinspection unchecked
		return (Map<String, Object>) NbtElementUtil.toObject(this.playerEntity.getShoulderEntityRight());
	}

	public PyEnderChestInventory getEnderChestInventory() {
		return new PyEnderChestInventory(this.playerEntity.getEnderChestInventory());
	}

	public void addShoulderEntity(Map<String, Object> entityNbt) {
		this.playerEntity.addShoulderEntity(NbtCompoundUtil.fromMap(entityNbt));
	}

	public void addExperience(Number experience) {
		this.playerEntity.addExperience(experience.intValue());
	}

	public void attack(PyEntity entity) {
		this.playerEntity.attack(entity.entity);
	}

	public boolean canConsume(boolean ignoreHunger) {
		return this.playerEntity.canConsume(ignoreHunger);
	}

	public boolean checkFallFlying() {
		return this.playerEntity.checkFallFlying();
	}

	public PyHungerManager getHungerManager() {
		return new PyHungerManager(this.playerEntity.getHungerManager());
	}

	public void addExperienceLevels(Number levels) {
		this.playerEntity.addExperienceLevels(levels.intValue());
	}

	public void disableShield(boolean sprinting) {
		this.playerEntity.disableShield(sprinting);
	}

	public boolean canHarvest(PyBlockState block) {
		return this.playerEntity.canHarvest(block.blockState);
	}

	public boolean canHarvest(PyBlocks block) {
		return this.playerEntity.canHarvest(block.toBlock().getDefaultState());
	}

	public void requestRespawn() {
		this.playerEntity.requestRespawn();
	}

	public void sendMessage(Object message) {
		this.playerEntity.sendMessage(Text.of(String.valueOf(message)));
	}

	public void sendMessage(PyText text) {
		this.playerEntity.sendMessage(text.text);
	}

	public void setMainArm(PyArm arm) {
		this.playerEntity.setMainArm(arm.toArm());
	}
}
