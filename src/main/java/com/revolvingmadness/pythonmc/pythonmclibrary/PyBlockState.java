package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.block.BlockState;

public class PyBlockState {
	BlockState blockState;
	public PyBlock block;
	
	public PyBlockState(BlockState blockState) {
		this.block = new PyBlock(blockState.getBlock());
		this.blockState = blockState;
	}
	
	public PyBlockState(PyBlocks block) {
		this.block = new PyBlock(block.toBlock());
		this.blockState = this.block.block.getDefaultState();
	}
	
	public boolean isOf(PyBlock block) {
		return this.blockState.isOf(block.block);
	}
	
	@Override
	public String toString() {
		return this.block.toString();
	}
}
