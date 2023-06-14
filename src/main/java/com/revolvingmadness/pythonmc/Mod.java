package com.revolvingmadness.pythonmc;

import com.revolvingmadness.pythonmc.commands.ModCommands;
import net.fabricmc.api.ModInitializer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class Mod implements ModInitializer {
	public static final String MOD_ID = "pythonmc";
	public static final Logger LOGGER = LoggerFactory.getLogger(MOD_ID);
	public static String pythonMCVersion;
	public static final Integer major = 1;
	public static final Integer minor = 0;
	public static final Integer patch = 0;

	@Override
	public void onInitialize() {
		ModCommands.registerCommands();

		pythonMCVersion = major + "." + minor + "." + patch;
	}
}