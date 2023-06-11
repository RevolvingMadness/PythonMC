package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.entity.effect.StatusEffectInstance;

public class PyStatusEffectInstance {
	StatusEffectInstance instance;
	public int duration;
	public int amplifier;
	
	public PyStatusEffectInstance(StatusEffectInstance instance) {
		this.instance = instance;
		this.duration = instance.getDuration();
		this.amplifier = instance.getAmplifier();
	}
}
