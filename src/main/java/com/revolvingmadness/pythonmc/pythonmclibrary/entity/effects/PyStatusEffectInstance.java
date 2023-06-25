package com.revolvingmadness.pythonmc.pythonmclibrary.entity.effects;

import net.minecraft.entity.effect.StatusEffectInstance;

public class PyStatusEffectInstance {
	public final int duration;
	public final int amplifier;
	final StatusEffectInstance instance;
	
	public PyStatusEffectInstance(StatusEffectInstance instance) {
		this.instance = instance;
		this.duration = instance.getDuration();
		this.amplifier = instance.getAmplifier();
	}
}
