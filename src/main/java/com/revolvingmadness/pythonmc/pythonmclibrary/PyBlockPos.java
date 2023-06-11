package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.util.math.BlockPos;

public class PyBlockPos {
	BlockPos blockPos;
	public int x;
	public int y;
	public int z;
	
	public PyBlockPos(BlockPos blockPos) {
		this.blockPos = blockPos;
		this.x = blockPos.getX();
		this.y = blockPos.getY();
		this.z = blockPos.getZ();
	}
	
	public PyBlockPos(int x, int y, int z) {
		this.blockPos = new BlockPos(x, y, z);
		this.x = x;
		this.y = y;
		this.z = z;
	}
	
	@Override
	public String toString() {
		return "(" + this.x + ", " + this.y + ", " + this.z + ")";
	}
}
