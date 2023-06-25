package com.revolvingmadness.pythonmc.pythonmclibrary.block;

import net.minecraft.block.BlockState;

public class PyBlockState {
	public final BlockState blockState;
	public final PyBlock block;
	
	public PyBlockState(PyBlocks block) {
		this(block.toBlock().getDefaultState());
	}
	
	public PyBlockState(BlockState blockState) {
		this.block = new PyBlock(blockState.getBlock());
		this.blockState = blockState;
	}
	
	public boolean isOf(PyBlocks block) {
		return this.isOf(new PyBlock(block.toBlock()));
	}
	
	public boolean isOf(PyBlock block) {
		return this.blockState.isOf(block.block);
	}
	
	@Override
	public String toString() {
		return this.block.name;
	}
}
