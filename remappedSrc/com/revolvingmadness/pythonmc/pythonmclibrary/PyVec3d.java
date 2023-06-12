package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.util.math.Vec3d;

public class PyVec3d {
    final Vec3d vec;
    public final double x;
    public final double y;
    public final double z;

    public PyVec3d(Vec3d vec) {
        this.vec = vec;
        this.x = vec.x;
        this.y = vec.y;
        this.z = vec.z;
    }

    public PyVec3d(Number x, Number y, Number z) {
        this.x = x.doubleValue();
        this.y = y.doubleValue();
        this.z = z.doubleValue();
        this.vec = new Vec3d(this.x, this.y, this.z);
    }

    @Override
    public String toString() {
        return "(" + this.x + ", " + this.y + ", " + this.z + ")";
    }
}
