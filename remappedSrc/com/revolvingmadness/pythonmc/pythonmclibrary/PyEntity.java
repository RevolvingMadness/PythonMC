package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.entity.Entity;
import net.minecraft.text.Text;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class PyEntity {
    final Entity entity;

    public PyEntity(Entity entity) {
        this.entity = entity;
    }

    public PyEntity(PyEntities entity, PyWorld world) {
        this.entity = entity.toEntityType().create(world.world);
    }

    public void setVelocity(PyVec3d velocity) {
        this.entity.setVelocity(velocity.vec);
    }

    public void addVelocity(PyVec3d velocity) {
        this.entity.addVelocity(velocity.vec);
    }

    public PyVec3d getVelocity() {
        return new PyVec3d(this.entity.getVelocity());
    }

    public boolean isWet() {
        return this.entity.isWet();
    }

    public List<PyItemStack> getArmorItems() {
        List<PyItemStack> result = new ArrayList<>();
        this.entity.getArmorItems().forEach(stack -> result.add(new PyItemStack(stack)));
        return result;
    }

    public void kill() {
        this.entity.kill();
    }

    public boolean isAlive() {
        return this.entity.isAlive();
    }

    public void setInvisible(boolean invisible) {
        this.entity.setInvisible(invisible);
    }

    public void teleport(PyVec3d position) {
        this.entity.teleport(position.x, position.y, position.z);
    }

    public boolean isSpectator() {
        return this.entity.isSpectator();
    }

    public void remove(PyRemovalReasons reason) {
        this.entity.remove(reason.toRemovalReason());
    }

    public PyBlockPos getBlockPos() {
        return new PyBlockPos(this.entity.getBlockPos());
    }

    public boolean isInsideWall() {
        return this.entity.isInsideWall();
    }

    public boolean isInRange(PyEntity entity, Number range) {
        return this.entity.isInRange(entity.entity, range.doubleValue());
    }

    public boolean hasVehicle() {
        return this.entity.hasVehicle();
    }

    public void setOnFireFor(Number seconds) {
        this.entity.setOnFireFor(seconds.intValue());
    }

    public boolean isInsideWaterOrBubbleColumn() {
        return this.entity.isInsideWaterOrBubbleColumn();
    }

    public void setOnFire(boolean onFire) {
        this.entity.setOnFire(onFire);
    }

    public void setGlowing(boolean glowing) {
        this.entity.setGlowing(glowing);
    }

    public void extinguishWithSound() {
        this.entity.extinguishWithSound();
    }

    public void setFireTicks(Number fireTicks) {
        this.entity.setFireTicks(fireTicks.intValue());
    }

    public PyEntity getVehicle() {
        return new PyEntity(this.entity.getVehicle());
    }

    public boolean isSubmergedInWater() {
        return this.entity.isSubmergedInWater();
    }

    public void dismountVehicle() {
        this.entity.dismountVehicle();
    }

    public List<PyItemStack> getHandItems() {
        List<PyItemStack> result = new ArrayList<>();
        this.entity.getHandItems().forEach(stack -> result.add(new PyItemStack(stack)));
        return result;
    }

    public void setOnFireFromLava() {
        this.entity.setOnFireFromLava();
    }

    public void damage(PyDamageSources source, Number amount) {
        this.entity.damage(source.toDamageSource(this.entity.world), amount.floatValue());
    }

    public void setCustomName(String customName) {
        this.entity.setCustomName(Text.of(customName));
    }

    public boolean canUsePortals() {
        return this.entity.canUsePortals();
    }

    public void setPosition(PyVec3d position) {
        this.entity.setPosition(position.vec);
    }

    public boolean hasCustomName() {
        return this.entity.hasCustomName();
    }

    public List<String> getCommandTags() {
        return this.entity.getCommandTags().stream().toList();
    }

    public void extinguish() {
        this.entity.extinguish();
    }

    public boolean isSprinting() {
        return this.entity.isSprinting();
    }

    public boolean isTouchingWater() {
        return this.entity.isTouchingWater();
    }

    public boolean hasPassenger(PyEntity entity) {
        return this.entity.hasPassenger(entity.entity);
    }

    public PyVec3d getPosition() {
        return new PyVec3d(this.entity.getPos());
    }

    public void stopRiding() {
        this.entity.stopRiding();
    }

    public double getX() {
        return this.entity.getX();
    }

    public double getY() {
        return this.entity.getY();
    }

    public double getZ() {
        return this.entity.getZ();
    }

    public boolean shouldRenderName() {
        return this.entity.shouldRenderName();
    }

    public void setSilent(boolean silent) {
        this.entity.setSilent(silent);
    }

    public boolean isSneaking() {
        return this.entity.isSneaking();
    }

    public boolean isTouchingWaterOrRain() {
        return this.entity.isTouchingWaterOrRain();
    }

    public boolean hasPermissionLevel(Number level) {
        return this.entity.hasPermissionLevel(level.intValue());
    }

    public float distanceTo(PyEntity entity) {
        return this.entity.distanceTo(entity.entity);
    }

    public boolean canFreeze() {
        return this.entity.canFreeze();
    }

    public void startRiding(PyEntity entity) {
        this.entity.startRiding(entity.entity);
    }

    public boolean isOnGround() {
        return this.entity.isOnGround();
    }

    public boolean isCustomNameVisible() {
        return this.entity.isCustomNameVisible();
    }

    public boolean isFireImmune() {
        return this.entity.isFireImmune();
    }

    public boolean hasPortalCooldown() {
        return this.entity.hasPortalCooldown();
    }

    public boolean isSwimming() {
        return this.entity.isSwimming();
    }

    public void setOnGround(boolean onGround) {
        this.entity.setOnGround(onGround);
    }

    public void setSprinting(boolean sprinting) {
        this.entity.setSprinting(sprinting);
    }

    public boolean isLiving() {
        return this.entity.isLiving();
    }

    public boolean isCrawling() {
        return this.entity.isCrawling();
    }

    public void removeAllPassengers() {
        this.entity.removeAllPassengers();
    }

    public boolean hasNoGravity() {
        return this.entity.hasNoGravity();
    }

    public boolean hasPassengers() {
        return this.entity.hasPassengers();
    }

    public void setNoGravity(boolean noGravity) {
        this.entity.setNoGravity(noGravity);
    }

    public boolean collidesWith(PyEntity entity) {
        return this.entity.collidesWith(entity.entity);
    }

    public boolean isInLava() {
        return this.entity.isInLava();
    }

    public String getDisplayName() {
        return this.entity.getDisplayName().getString();
    }

    public void setCustomNameVisible(boolean customNameVisible) {
        this.entity.setCustomNameVisible(customNameVisible);
    }

    public boolean isSilent() {
        return this.entity.isSilent();
    }

    public boolean shouldDismountUnderwater() {
        return this.entity.shouldDismountUnderwater();
    }

    public boolean isGlowing() {
        return this.entity.isGlowing();
    }

    public boolean isOnFire() {
        return this.entity.isOnFire();
    }

    public boolean isInvisible() {
        return this.entity.isInvisible();
    }

    public void setInPowderSnow(boolean inPowderSnow) {
        this.entity.setInPowderSnow(inPowderSnow);
    }

    public boolean isPushable() {
        return this.entity.isPushable();
    }

    public boolean isPlayer() {
        return this.entity.isPlayer();
    }

    public String getCustomName() {
        if (this.entity.hasCustomName()) {
            return Objects.requireNonNull(this.entity.getCustomName()).getString();
        }
        return null;
    }

    public String getName() {
        return Text.translatable(this.entity.getType().getTranslationKey()).getString();
    }

    public void setSneaking(boolean sneaking) {
        this.entity.setSneaking(sneaking);
    }

    public boolean isCollidable() {
        return this.entity.isCollidable();
    }

    public boolean isDescending() {
        return this.entity.isDescending();
    }
}
