package com.revolvingmadness.pythonmc.commands;

import com.revolvingmadness.pythonmc.commands.custom.RunPython;
import net.fabricmc.fabric.api.command.v2.CommandRegistrationCallback;

public class ModCommands {
	public static void registerCommands() {
		CommandRegistrationCallback.EVENT.register(RunPython::register);
	}
}
