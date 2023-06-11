package com.revolvingmadness.pythonmc;

import com.revolvingmadness.pythonmc.commands.ModCommands;
import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.event.lifecycle.v1.ServerLifecycleEvents;
import net.minecraft.server.MinecraftServer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class Mod implements ModInitializer {
	public static final String MOD_ID = "pythonmc";
	public static final Logger LOGGER = LoggerFactory.getLogger(MOD_ID);
	public static MinecraftServer server = null;
	
	@Override
	public void onInitialize() {
		ModCommands.registerCommands();
		
		ServerLifecycleEvents.SERVER_STARTED.register(server -> Mod.server = server);
		
		ServerLifecycleEvents.SERVER_STOPPED.register(server -> Mod.server = null);
	}
}