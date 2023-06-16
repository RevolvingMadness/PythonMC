package com.revolvingmadness.pythonmc.pythonmclibrary.block;

import net.minecraft.util.math.BlockPos;

public class PyBlockPos {
	public final BlockPos blockPos;
	public final int x;
	public final int y;
	public final int z;

	public PyBlockPos(BlockPos blockPos) {
		this.blockPos = blockPos;
		this.x = blockPos.getX();
		this.y = blockPos.getY();
		this.z = blockPos.getZ();
	}

	public PyBlockPos(Number x, Number y, Number z) {
		this(new BlockPos(x.intValue(), y.intValue(), z.intValue()));
	}

	@Override
	public String toString() {
		return "(" + this.x + ", " + this.y + ", " + this.z + ")";
	}
}
