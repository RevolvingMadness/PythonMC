package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.util.Arm;

public enum PyArm {
	LEFT, RIGHT;
	
	public static PyArm fromArm(Arm arm) {
		return switch (arm) {
			case LEFT -> LEFT;
			case RIGHT -> RIGHT;
		};
	}
	
	public Arm toArm() {
		return switch (this) {
			case LEFT -> Arm.LEFT;
			case RIGHT -> Arm.RIGHT;
		};
	}
}
