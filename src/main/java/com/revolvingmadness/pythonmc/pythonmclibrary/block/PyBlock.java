package com.revolvingmadness.pythonmc.pythonmclibrary.block;

import com.revolvingmadness.pythonmc.pythonmclibrary.item.PyItem;
import net.minecraft.block.Block;
import net.minecraft.text.Text;

public class PyBlock {
	final Block block;
	public final PyItem item;
	public final String name;
	public final float blastResistance;
	public final float velocityMultiplier;
	public final float jumpVelocityMultiplier;
	public final float slipperiness;

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
