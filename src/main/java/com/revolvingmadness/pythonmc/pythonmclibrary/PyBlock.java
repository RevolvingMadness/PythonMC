package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.block.Block;

public class PyBlock {
	Block block;
	public PyItem item;
	public String name;
	public Float blastResistance;
	public Float velocityMultiplier;
	public Float jumpVelocityMultiplier;
	public Float slipperiness;
	
	public PyBlock(Block block) {
		this.block = block;
		this.item = new PyItem(block.asItem());
		this.name = block.getName().getString();
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
