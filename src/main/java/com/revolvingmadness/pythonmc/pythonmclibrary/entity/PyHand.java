package com.revolvingmadness.pythonmc.pythonmclibrary.entity;

import net.minecraft.util.Hand;

public enum PyHand {
	MAIN_HAND, OFF_HAND;

	public static PyHand fromHand(Hand hand) {
		return switch (hand) {
			case MAIN_HAND -> MAIN_HAND;
			case OFF_HAND -> OFF_HAND;
		};
	}

	public Hand toHand() {
		return switch (this) {
			case MAIN_HAND -> Hand.MAIN_HAND;
			case OFF_HAND -> Hand.OFF_HAND;
		};
	}
}
