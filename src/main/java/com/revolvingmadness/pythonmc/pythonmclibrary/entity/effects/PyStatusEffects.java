package com.revolvingmadness.pythonmc.pythonmclibrary.entity.effects;

import net.minecraft.entity.effect.StatusEffect;
import net.minecraft.entity.effect.StatusEffects;

public enum PyStatusEffects {
	SPEED, SLOWNESS, HASTE, MINING_FATIGUE, STRENGTH, INSTANT_HEALTH, INSTANT_DAMAGE, JUMP_BOOST, NAUSEA, REGENERATION, RESISTANCE, FIRE_RESISTANCE, WATER_BREATHING, INVISIBILITY, BLINDNESS, NIGHT_VISION, HUNGER, WEAKNESS, POISON, WITHER, HEALTH_BOOST, ABSORPTION, SATURATION, GLOWING, LEVITATION, LUCK, UNLUCK, SLOW_FALLING, CONDUIT_POWER, DOLPHINS_GRACE, BAD_OMEN, HERO_OF_THE_VILLAGE, DARKNESS;
	
	public StatusEffect toStatusEffect() {
		return switch (this) {
			case SPEED -> StatusEffects.SPEED;
			case SLOWNESS -> StatusEffects.SLOWNESS;
			case HASTE -> StatusEffects.HASTE;
			case MINING_FATIGUE -> StatusEffects.MINING_FATIGUE;
			case STRENGTH -> StatusEffects.STRENGTH;
			case INSTANT_HEALTH -> StatusEffects.INSTANT_HEALTH;
			case INSTANT_DAMAGE -> StatusEffects.INSTANT_DAMAGE;
			case JUMP_BOOST -> StatusEffects.JUMP_BOOST;
			case NAUSEA -> StatusEffects.NAUSEA;
			case REGENERATION -> StatusEffects.REGENERATION;
			case RESISTANCE -> StatusEffects.RESISTANCE;
			case FIRE_RESISTANCE -> StatusEffects.FIRE_RESISTANCE;
			case WATER_BREATHING -> StatusEffects.WATER_BREATHING;
			case INVISIBILITY -> StatusEffects.INVISIBILITY;
			case BLINDNESS -> StatusEffects.BLINDNESS;
			case NIGHT_VISION -> StatusEffects.NIGHT_VISION;
			case HUNGER -> StatusEffects.HUNGER;
			case WEAKNESS -> StatusEffects.WEAKNESS;
			case POISON -> StatusEffects.POISON;
			case WITHER -> StatusEffects.WITHER;
			case HEALTH_BOOST -> StatusEffects.HEALTH_BOOST;
			case ABSORPTION -> StatusEffects.ABSORPTION;
			case SATURATION -> StatusEffects.SATURATION;
			case GLOWING -> StatusEffects.GLOWING;
			case LEVITATION -> StatusEffects.LEVITATION;
			case LUCK -> StatusEffects.LUCK;
			case UNLUCK -> StatusEffects.UNLUCK;
			case SLOW_FALLING -> StatusEffects.SLOW_FALLING;
			case CONDUIT_POWER -> StatusEffects.CONDUIT_POWER;
			case DOLPHINS_GRACE -> StatusEffects.DOLPHINS_GRACE;
			case BAD_OMEN -> StatusEffects.BAD_OMEN;
			case HERO_OF_THE_VILLAGE -> StatusEffects.HERO_OF_THE_VILLAGE;
			case DARKNESS -> StatusEffects.DARKNESS;
		};
	}
}
