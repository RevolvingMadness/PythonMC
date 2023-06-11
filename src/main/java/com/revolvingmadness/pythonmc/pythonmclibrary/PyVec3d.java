package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.util.math.Vec3d;

public class PyVec3d {
	Vec3d vec;
	public double x;
	public double y;
	public double z;
	
	public PyVec3d(Vec3d vec) {
		this.vec = vec;
		this.x = vec.x;
		this.y = vec.y;
		this.z = vec.z;
	}
	
	public PyVec3d(double x, double y, double z) {
		this.vec = new Vec3d(x, y, z);
		this.x = x;
		this.y = y;
		this.z = z;
	}
	
	@Override
	public String toString() {
		return "(" + this.x + ", " + this.y + ", " + this.z + ")";
	}
}
