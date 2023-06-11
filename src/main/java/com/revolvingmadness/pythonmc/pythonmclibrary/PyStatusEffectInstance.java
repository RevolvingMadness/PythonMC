package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.entity.effect.StatusEffectInstance;

public class PyStatusEffectInstance {
    final StatusEffectInstance instance;
    public final int duration;
    public final int amplifier;

    public PyStatusEffectInstance(StatusEffectInstance instance) {
        this.instance = instance;
        this.duration = instance.getDuration();
        this.amplifier = instance.getAmplifier();
    }
}
