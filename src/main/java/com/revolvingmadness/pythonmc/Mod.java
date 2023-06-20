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

import java.nio.file.Path;
import java.util.Optional;

public class Mod implements ModInitializer {
	public static final String MOD_ID = "pythonmc";
	public static final Logger LOGGER = LoggerFactory.getLogger(MOD_ID);
	public static final Integer major = 1;
	public static final Integer minor = 0;
	public static final Integer patch = 0;
	public static String pythonMCVersion;

	@Override
	public void onInitialize() {
		if (System.getenv("PYTHONHOME") == null) {
			throw new RuntimeException("Environment variable 'PYTHONHOME' is not set.");
		}
		System.setProperty("java.library.path", "");

		pythonMCVersion = major + "." + minor + "." + patch;

		ModCommands.registerCommands();


		ServerLifecycleEvents.SERVER_STARTING.register(server -> {
			Optional<Path> path = FabricLoader.getInstance().getModContainer(MOD_ID).get().findPath("pythonmclibrary");
			JepConfig config = new JepConfig().redirectStdErr(PythonExecutor.outputStream).redirectStdErr(PythonExecutor.errorOutputStream);
			path.ifPresent(value -> config.addIncludePaths(value.toString()));
			PythonExecutor.interpreter = new SubInterpreter(config);
		});

		ServerLifecycleEvents.SERVER_STOPPING.register(server -> PythonExecutor.interpreter.close());
	}
}