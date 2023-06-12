package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.block.Block;
import net.minecraft.text.Text;

public class PyBlock {
    final Block block;
    public final PyItem item;
    public final String name;
    public final Float blastResistance;
    public final Float velocityMultiplier;
    public final Float jumpVelocityMultiplier;
    public final Float slipperiness;

    public PyBlock(Block block) {
        this.block = block;
        this.item = new PyItem(block.asItem());
        this.name = Text.translatable(block.getTranslationKey()).getString();
        this.blastResistance = block.getBlastResistance();
        this.velocityMultiplier = block.getVelocityMultiplier();
        this.jumpVelocityMultiplier = block.getJumpVelocityMultiplier();
        this.slipperiness = block.getSlipperiness();
    }

    @Override
    public String toString() {
        return this.block.toString();
    }
}
