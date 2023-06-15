package com.revolvingmadness.pythonmc;

import com.revolvingmadness.pythonmc.commands.ModCommands;
import com.revolvingmadness.pythonmc.pythonrunner.PythonExecutor;
import jep.JepConfig;
import jep.SubInterpreter;
import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.event.lifecycle.v1.ServerLifecycleEvents;
import net.fabricmc.loader.api.FabricLoader;
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

		ServerLifecycleEvents.SERVER_STARTING.register(server -> PythonExecutor.interpreter = new SubInterpreter(new JepConfig().redirectStdErr(PythonExecutor.outputStream).redirectStdErr(PythonExecutor.errorOutputStream).addIncludePaths(FabricLoader.getInstance().getModContainer(MOD_ID).get().getRootPaths().get(0).toString() + "/pythonmclibrary")));

		ServerLifecycleEvents.SERVER_STOPPING.register(server -> PythonExecutor.interpreter.close());
	}
}