package com.revolvingmadness.pythonmc.pythonmclibrary.world.position;

import net.minecraft.util.math.Vec3d;

public class PyVec3d {
	public final Vec3d vec;
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
		this(new Vec3d(x.floatValue(), y.floatValue(), z.floatValue()));
	}

	@Override
	public String toString() {
		return "(" + this.x + ", " + this.y + ", " + this.z + ")";
	}
}
