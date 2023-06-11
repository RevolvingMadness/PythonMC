package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.entity.damage.DamageSource;
import net.minecraft.entity.damage.DamageSources;
import net.minecraft.world.World;

public enum PyDamageSources {
	INFIRE, LIGHTNINGBOLT, ONFIRE, LAVA, HOTFLOOR, INWALL, CRAMMING, DROWN, STARVE, CACTUS, FALL, FLYINTOWALL, OUTOFWORLD, GENERIC, MAGIC, WITHER, DRAGONBREATH, DRYOUT, SWEETBERRYBUSH, FREEZE, STALAGMITE;
	
	public DamageSource toDamageSource(World world) {
		DamageSources damageSources = world.getDamageSources();
		
		return switch (this) {
			case INFIRE -> damageSources.inFire();
			case LIGHTNINGBOLT -> damageSources.lightningBolt();
			case ONFIRE -> damageSources.onFire();
			case LAVA -> damageSources.lava();
			case HOTFLOOR -> damageSources.hotFloor();
			case INWALL -> damageSources.inWall();
			case CRAMMING -> damageSources.cramming();
			case DROWN -> damageSources.drown();
			case STARVE -> damageSources.starve();
			case CACTUS -> damageSources.cactus();
			case FALL -> damageSources.fall();
			case FLYINTOWALL -> damageSources.flyIntoWall();
			case OUTOFWORLD -> damageSources.outOfWorld();
			case GENERIC -> damageSources.generic();
			case MAGIC -> damageSources.magic();
			case WITHER -> damageSources.wither();
			case DRAGONBREATH -> damageSources.dragonBreath();
			case DRYOUT -> damageSources.dryOut();
			case SWEETBERRYBUSH -> damageSources.sweetBerryBush();
			case FREEZE -> damageSources.freeze();
			case STALAGMITE -> damageSources.stalagmite();
		};
	}
}
