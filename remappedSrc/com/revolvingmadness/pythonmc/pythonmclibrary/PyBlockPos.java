package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.util.math.BlockPos;

public class PyBlockPos {
    final BlockPos blockPos;
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
        this.x = x.intValue();
        this.y = y.intValue();
        this.z = z.intValue();
        this.blockPos = new BlockPos(this.x, this.y, this.z);
    }

    @Override
    public String toString() {
        return "(" + this.x + ", " + this.y + ", " + this.z + ")";
    }
}
