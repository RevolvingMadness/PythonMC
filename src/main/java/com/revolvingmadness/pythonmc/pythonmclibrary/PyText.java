package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.text.MutableText;
import net.minecraft.text.Text;

public class PyText {
	public MutableText text;

	public PyText(String message) {
		this.text = Text.empty();
		this.text.append(message);
	}

	public PyText withFormatting(PyFormatting formatting) {
		this.text.formatted(formatting.toFormatting());
		return this;
	}
}
