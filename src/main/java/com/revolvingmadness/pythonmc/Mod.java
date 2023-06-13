package com.revolvingmadness.pythonmc;

import com.revolvingmadness.pythonmc.commands.ModCommands;
import com.revolvingmadness.pythonmc.pythonrunner.PythonExecutor;
import com.revolvingmadness.pythonmc.pythonrunner.PythonInterpreterThread;
import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.event.lifecycle.v1.ServerLifecycleEvents;
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

		ServerLifecycleEvents.SERVER_STARTING.register(server -> {
			PythonExecutor.interpreterThread = new PythonInterpreterThread();
			PythonExecutor.interpreterThread.start();
		});

		ServerLifecycleEvents.SERVER_STOPPING.register(server -> PythonExecutor.interpreterThread.interrupt());
	}
}