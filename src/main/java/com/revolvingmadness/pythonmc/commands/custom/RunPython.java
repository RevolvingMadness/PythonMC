package com.revolvingmadness.pythonmc.commands.custom;

import com.mojang.brigadier.CommandDispatcher;
import com.mojang.brigadier.context.CommandContext;
import com.mojang.brigadier.exceptions.CommandSyntaxException;
import com.revolvingmadness.pythonmc.pythonrunner.PythonExecutor;
import net.minecraft.command.CommandRegistryAccess;
import net.minecraft.command.argument.MessageArgumentType;
import net.minecraft.server.command.CommandManager;
import net.minecraft.server.command.ServerCommandSource;

public class RunPython {
	public static void register(CommandDispatcher<ServerCommandSource> dispatcher, CommandRegistryAccess access, CommandManager.RegistrationEnvironment environment) {
		dispatcher.register(CommandManager.literal("runpython").then(CommandManager.literal("code").then(CommandManager.argument("code", MessageArgumentType.message()).executes(RunPython::runCode))));
	}

	@SuppressWarnings("SameReturnValue")
	private static int runCode(CommandContext<ServerCommandSource> context) throws CommandSyntaxException {
		String code = MessageArgumentType.getMessage(context, "code").getString();

		PythonExecutor.execute(context.getSource(), null, null, code);

		return 1;
	}
}
