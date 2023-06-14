package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.util.Formatting;

public enum PyFormatting {
	BLACK, DARK_BLUE, DARK_GREEN, DARK_AQUA, DARK_RED, DARK_PURPLE, GOLD, GRAY, DARK_GRAY, BLUE, GREEN, AQUA, RED, LIGHT_PURPLE, YELLOW, WHITE, OBFUSCATED, BOLD, STRIKETHROUGH, UNDERLINE, ITALIC, RESET;

	public Formatting toFormatting() {
		return switch (this) {
			case BLACK -> Formatting.BLACK;
			case DARK_BLUE -> Formatting.DARK_BLUE;
			case DARK_GREEN -> Formatting.DARK_GREEN;
			case DARK_AQUA -> Formatting.DARK_AQUA;
			case DARK_RED -> Formatting.DARK_RED;
			case DARK_PURPLE -> Formatting.DARK_PURPLE;
			case GOLD -> Formatting.GOLD;
			case GRAY -> Formatting.GRAY;
			case DARK_GRAY -> Formatting.DARK_GRAY;
			case BLUE -> Formatting.BLUE;
			case GREEN -> Formatting.GREEN;
			case AQUA -> Formatting.AQUA;
			case RED -> Formatting.RED;
			case LIGHT_PURPLE -> Formatting.LIGHT_PURPLE;
			case YELLOW -> Formatting.YELLOW;
			case WHITE -> Formatting.WHITE;
			case OBFUSCATED -> Formatting.OBFUSCATED;
			case BOLD -> Formatting.BOLD;
			case STRIKETHROUGH -> Formatting.STRIKETHROUGH;
			case UNDERLINE -> Formatting.UNDERLINE;
			case ITALIC -> Formatting.ITALIC;
			case RESET -> Formatting.RESET;
		};
	}
}
