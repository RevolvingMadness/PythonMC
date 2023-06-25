package com.revolvingmadness.pythonmc.pythonmclibrary.entity;

import com.revolvingmadness.pythonmc.pythonmclibrary.entity.effects.PyStatusEffectInstance;
import com.revolvingmadness.pythonmc.pythonmclibrary.entity.effects.PyStatusEffects;
import com.revolvingmadness.pythonmc.pythonmclibrary.item.PyItem;
import com.revolvingmadness.pythonmc.pythonmclibrary.item.PyItemStack;
import com.revolvingmadness.pythonmc.pythonmclibrary.player.PyPlayerEntity;
import net.minecraft.entity.LivingEntity;
import net.minecraft.entity.effect.StatusEffectInstance;
import net.minecraft.util.math.Vec3d;

import java.util.ArrayList;
import java.util.List;

public class PyLivingEntity extends PyEntity {
	final LivingEntity livingEntity;
	
	public PyLivingEntity(LivingEntity livingEntity) {
		super(livingEntity);
		this.livingEntity = livingEntity;
	}
	
	public boolean canBreatheInWater() {
		return this.livingEntity.canBreatheInWater();
	}
	
	public boolean canSee(PyEntity entity) {
		return this.livingEntity.canSee(entity.entity);
	}
	
	public boolean canHaveStatusEffect(PyStatusEffects effect) {
		return this.livingEntity.canHaveStatusEffect(new StatusEffectInstance(effect.toStatusEffect()));
	}
	
	public boolean canTakeDamage() {
		return this.livingEntity.canTakeDamage();
	}
	
	public void addStatusEffect(PyStatusEffects effect, Number duration, Number amplifier, boolean visible) {
		this.livingEntity.addStatusEffect(new StatusEffectInstance(effect.toStatusEffect(), duration.intValue(), amplifier.intValue(), false, visible));
	}
	
	public void clearStatusEffects() {
		this.livingEntity.clearStatusEffects();
	}
	
	public void damageArmor(PyDamageSources source, Number amount) {
		this.livingEntity.damageArmor(source.toDamageSource(this.livingEntity.getWorld()), amount.floatValue());
	}
	
	public void damageHelmet(PyDamageSources source, Number amount) {
		this.livingEntity.damageHelmet(source.toDamageSource(this.livingEntity.getWorld()), amount.floatValue());
	}
	
	public void damageShield(Number amount) {
		this.livingEntity.damageShield(amount.floatValue());
	}
	
	public void eatFood(PyItemStack stack) {
		this.livingEntity.eatFood(this.livingEntity.getWorld(), stack.itemStack);
	}
	
	public float getAbsorptionAmount() {
		return this.livingEntity.getAbsorptionAmount();
	}
	
	public void setAbsorptionAmount(Number amount) {
		this.livingEntity.setAbsorptionAmount(amount.floatValue());
	}
	
	public PyHand getActiveHand() {
		return PyHand.fromHand(this.livingEntity.getActiveHand());
	}
	
	public PyItemStack getActiveItem() {
		return new PyItemStack(this.livingEntity.getActiveItem());
	}
	
	public List<PyItemStack> getArmorItems() {
		List<PyItemStack> result = new ArrayList<>();
		this.livingEntity.getArmorItems().forEach(stack -> result.add(new PyItemStack(stack)));
		return result;
	}
	
	public void remove(PyRemovalReasons reason) {
		this.livingEntity.remove(reason.toRemovalReason());
	}
	
	public void damage(PyDamageSources source, Number amount) {
		this.livingEntity.damage(source.toDamageSource(this.livingEntity.getWorld()), amount.floatValue());
	}
	
	public float getArmor() {
		return this.livingEntity.getArmor();
	}
	
	public PyLivingEntity getAttacking() {
		return new PyLivingEntity(this.livingEntity.getAttacking());
	}
	
	public void setAttacking(PyPlayerEntity attacking) {
		this.livingEntity.setAttacking(attacking.playerEntity);
	}
	
	public PyLivingEntity getAttacker() {
		return new PyLivingEntity(this.livingEntity.getAttacker());
	}
	
	public void setAttacker(PyLivingEntity attacker) {
		this.livingEntity.setAttacker(attacker.livingEntity);
	}
	
	public float getHealth() {
		return this.livingEntity.getHealth();
	}
	
	public void setHealth(Number health) {
		this.livingEntity.setHealth(health.floatValue());
	}
	
	public PyArm getMainArm() {
		return PyArm.fromArm(this.livingEntity.getMainArm());
	}
	
	public PyItemStack getMainHandStack() {
		return new PyItemStack(this.livingEntity.getMainHandStack());
	}
	
	public float getMaxHealth() {
		return this.livingEntity.getMaxHealth();
	}
	
	public float getMovementSpeed() {
		return this.livingEntity.getMovementSpeed();
	}
	
	public void setMovementSpeed(Number movementSpeed) {
		this.livingEntity.setMovementSpeed(movementSpeed.floatValue());
	}
	
	public float getScaleFactor() {
		return this.livingEntity.getScaleFactor();
	}
	
	public PyItemStack getStackInHand(PyHand hand) {
		return new PyItemStack(this.livingEntity.getStackInHand(hand.toHand()));
	}
	
	public PyStatusEffectInstance getStatusEffect(PyStatusEffects effect) {
		StatusEffectInstance instance = this.livingEntity.getStatusEffect(effect.toStatusEffect());
		if (instance != null) {
			return new PyStatusEffectInstance(instance);
		}
		return null;
	}
	
	public List<PyStatusEffectInstance> getStatusEffects() {
		List<PyStatusEffectInstance> result = new ArrayList<>();
		this.livingEntity.getStatusEffects().forEach(instance -> result.add(new PyStatusEffectInstance(instance)));
		return result;
	}
	
	public float getStuckArrowCount() {
		return this.livingEntity.getStuckArrowCount();
	}
	
	public void setStuckArrowCount(Number stuckArrowCount) {
		this.livingEntity.setStuckArrowCount(stuckArrowCount.intValue());
	}
	
	public boolean hasStatusEffect(PyStatusEffects effect) {
		return this.livingEntity.hasStatusEffect(effect.toStatusEffect());
	}
	
	public void heal(Number amount) {
		this.livingEntity.heal(amount.floatValue());
	}
	
	public boolean isHurtByWater() {
		return this.livingEntity.hurtByWater();
	}
	
	public boolean isAffectedBySplashPotions() {
		return this.livingEntity.isAffectedBySplashPotions();
	}
	
	public boolean isBaby() {
		return this.livingEntity.isBaby();
	}
	
	public boolean isBlocking() {
		return this.livingEntity.isBlocking();
	}
	
	public boolean isClimbing() {
		return this.livingEntity.isClimbing();
	}
	
	public boolean isDead() {
		return this.livingEntity.isDead();
	}
	
	public boolean isFallFlying() {
		return this.livingEntity.isFallFlying();
	}
	
	public boolean isHolding(PyItem item) {
		return this.livingEntity.isHolding(item.item);
	}
	
	public boolean isHoldingOntoLadder() {
		return this.livingEntity.isHoldingOntoLadder();
	}
	
	public boolean isMobOrPlayer() {
		return this.livingEntity.isMobOrPlayer();
	}
	
	public boolean isSleeping() {
		return this.livingEntity.isSleeping();
	}
	
	public boolean isUndead() {
		return this.livingEntity.isUndead();
	}
	
	public boolean isUsingItem() {
		return this.livingEntity.isUsingItem();
	}
	
	public boolean isUsingRiptide() {
		return this.livingEntity.isUsingRiptide();
	}
	
	public void removeStatusEffect(PyStatusEffects effect) {
		this.livingEntity.removeStatusEffect(effect.toStatusEffect());
	}
	
	public void setCurrentHand(PyHand hand) {
		this.livingEntity.setCurrentHand(hand.toHand());
	}
	
	public void setJumping(boolean jumping) {
		this.livingEntity.setJumping(jumping);
	}
	
	public void setStackInHand(PyHand hand, PyItemStack stack) {
		this.livingEntity.setStackInHand(hand.toHand(), stack.itemStack);
	}
	
	public void setStingerCount(Number stingerCount) {
		this.livingEntity.setStingerCount(stingerCount.intValue());
	}
	
	public boolean shouldDisplaySoulSpeedEffects() {
		return this.livingEntity.shouldDisplaySoulSpeedEffects();
	}
	
	public boolean shouldDropXp() {
		return this.livingEntity.shouldDropXp();
	}
	
	public void swingHand(PyHand hand) {
		this.livingEntity.swingHand(hand.toHand());
	}
	
	public void takeKnockback(Number strength, Number x, Number z) {
		this.livingEntity.takeKnockback(strength.doubleValue(), x.doubleValue(), z.doubleValue());
	}
	
	public void teleport(Vec3d position) {
		this.livingEntity.teleport(position.x, position.y, position.z);
	}
	
	public void tiltScreen(Number deltaX, Number deltaY) {
		this.livingEntity.tiltScreen(deltaX.doubleValue(), deltaY.doubleValue());
	}
}
