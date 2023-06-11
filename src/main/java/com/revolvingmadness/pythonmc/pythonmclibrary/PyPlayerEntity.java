package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.entity.player.PlayerEntity;
import net.minecraft.text.Text;

import java.util.Map;

public class PyPlayerEntity extends PyLivingEntity {
	PlayerEntity playerEntity;
	
	public PyPlayerEntity(PlayerEntity playerEntity) {
		super(playerEntity);
		this.playerEntity = playerEntity;
	}
	
	public boolean isMainPlayer() {
		return this.playerEntity.isMainPlayer();
	}
	
	public float getAttackCooldownProgress(float baseTime) {
		return this.playerEntity.getAttackCooldownProgress(baseTime);
	}
	
	public void addExhaustion(float exhaustion) {
		this.playerEntity.addExhaustion(exhaustion);
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
	
	public void addScore(int score) {
		this.playerEntity.addScore(score);
	}
	
	public boolean isCreative() {
		return this.playerEntity.isCreative();
	}
	
	public PyNbtCompound getShoulderEntityLeft() {
		return new PyNbtCompound(this.playerEntity.getShoulderEntityLeft());
	}
	
	public PyNbtCompound getShoulderEntityRight() {
		return new PyNbtCompound(this.playerEntity.getShoulderEntityRight());
	}
	
	public PyEnderChestInventory getEnderChestInventory() {
		return new PyEnderChestInventory(this.playerEntity.getEnderChestInventory());
	}
	
	public void addShoulderEntity(Map<String, Object> entityNbt) {
		this.playerEntity.addShoulderEntity(PyNbtCompound.fromMap(entityNbt));
	}
	
	public void addExperience(int experience) {
		this.playerEntity.addExperience(experience);
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
	
	public void addExperienceLevels(int levels) {
		this.playerEntity.addExperienceLevels(levels);
	}
	
	public void disableShield(boolean sprinting) {
		this.playerEntity.disableShield(sprinting);
	}
	
	public boolean canHarvest(PyBlockState state) {
		return this.playerEntity.canHarvest(state.blockState);
	}
	
	public void requestRespawn() {
		this.playerEntity.requestRespawn();
	}
	
	public void sendMessage(Object message) {
		this.playerEntity.sendMessage(Text.of(String.valueOf(message)));
	}
	
	public void setMainArm(PyArm arm) {
		this.playerEntity.setMainArm(arm.toArm());
	}
}
