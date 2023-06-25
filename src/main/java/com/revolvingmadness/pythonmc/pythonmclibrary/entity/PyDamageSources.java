package com.revolvingmadness.pythonmc.pythonmclibrary.entity;

import net.minecraft.entity.damage.DamageSource;
import net.minecraft.entity.damage.DamageSources;
import net.minecraft.world.World;

public enum PyDamageSources {
    IN_FIRE, LIGHTNING_BOLT, ON_FIRE, LAVA, HOT_FLOOR, IN_WALL, CRAMMING, DROWN, STARVE, CACTUS, FALL, FLY_INTO_WALL, OUT_OF_WORLD, GENERIC, MAGIC, WITHER, DRAGON_BREATH, DRY_OUT, SWEET_BERRY_BUSH, FREEZE, STALAGMITE, OUTSIDE_BORDER, GENERIC_KILL;

    public DamageSource toDamageSource(World world) {
        DamageSources damageSources = world.getDamageSources();

        return switch (this) {
            case IN_FIRE -> damageSources.inFire();
            case LIGHTNING_BOLT -> damageSources.lightningBolt();
            case ON_FIRE -> damageSources.onFire();
            case LAVA -> damageSources.lava();
            case HOT_FLOOR -> damageSources.hotFloor();
            case IN_WALL -> damageSources.inWall();
            case CRAMMING -> damageSources.cramming();
            case DROWN -> damageSources.drown();
            case STARVE -> damageSources.starve();
            case CACTUS -> damageSources.cactus();
            case FALL -> damageSources.fall();
            case FLY_INTO_WALL -> damageSources.flyIntoWall();
            case OUT_OF_WORLD -> damageSources.outOfWorld();
            case GENERIC -> damageSources.generic();
            case MAGIC -> damageSources.magic();
            case WITHER -> damageSources.wither();
            case DRAGON_BREATH -> damageSources.dragonBreath();
            case DRY_OUT -> damageSources.dryOut();
            case SWEET_BERRY_BUSH -> damageSources.sweetBerryBush();
            case FREEZE -> damageSources.freeze();
            case STALAGMITE -> damageSources.stalagmite();
            case OUTSIDE_BORDER -> damageSources.outsideBorder();
            case GENERIC_KILL -> damageSources.genericKill();
        };
    }
}
