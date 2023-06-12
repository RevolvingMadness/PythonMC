package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.block.BlockState;

public class PyBlockState {
	final BlockState blockState;
	public final PyBlock block;

	public PyBlockState(BlockState blockState) {
		this.block = new PyBlock(blockState.getBlock());
		this.blockState = blockState;
	}

	public PyBlockState(PyBlocks block) {
		this(block.toBlock().getDefaultState());
	}

	public boolean isOf(PyBlock block) {
		return this.blockState.isOf(block.block);
	}

	@Override
	public String toString() {
		return this.block.name;
	}
}
