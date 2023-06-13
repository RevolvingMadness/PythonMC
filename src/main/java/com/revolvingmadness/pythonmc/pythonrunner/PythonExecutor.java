package com.revolvingmadness.pythonmc.pythonrunner;

import com.revolvingmadness.pythonmc.Mod;
import com.revolvingmadness.pythonmc.pythonmclibrary.*;
import jep.JepException;
import jep.SubInterpreter;
import net.minecraft.server.PlayerManager;
import net.minecraft.server.command.ServerCommandSource;
import net.minecraft.server.world.ServerWorld;
import net.minecraft.text.Text;
import net.minecraft.util.Formatting;

import java.io.ByteArrayOutputStream;

public class PythonExecutor {
	public static PythonInterpreterThread interpreterThread;
	private static boolean initialized;
	private static SubInterpreter interpreter;
	public static ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
	public static ByteArrayOutputStream errorOutputStream = new ByteArrayOutputStream();

	public static void init() {
		interpreter = interpreterThread.interpreter;
		initialized = true;
	}

	public static void execute(ServerCommandSource source, String code) {
		if (!initialized) {
			init();
		}
		try {
			ServerWorld world = source.getWorld();
			interpreter.set("Arm", PyArm.class);
			interpreter.set("Block", PyBlock.class);
			interpreter.set("BlockPos", PyBlockPos.class);
			interpreter.set("Blocks", PyBlocks.class);
			interpreter.set("BlockState", PyBlockState.class);
			interpreter.set("DamageSources", PyDamageSources.class);
			interpreter.set("Difficulties", PyDifficulties.class);
			interpreter.set("Difficulty", PyDifficulty.class);
			interpreter.set("Enchantment", PyEnchantment.class);
			interpreter.set("EnchantmentRarity", PyEnchantmentRarity.class);
			interpreter.set("Enchantments", PyEnchantments.class);
			interpreter.set("EnderChestInventory", PyEnderChestInventory.class);
			interpreter.set("Entities", PyEntities.class);
			interpreter.set("Entity", PyEntity.class);
			interpreter.set("Executor", PyExecutor.class);
			interpreter.set("GameMode", PyGameMode.class);
			interpreter.set("GameModes", PyGameModes.class);
			interpreter.set("Hand", PyHand.class);
			interpreter.set("HideFlags", PyHideFlags.class);
			interpreter.set("HungerManager", PyHungerManager.class);
			interpreter.set("Item", PyItem.class);
			interpreter.set("Items", PyItems.class);
			interpreter.set("ItemStack", PyItemStack.class);
			interpreter.set("LivingEntity", PyLivingEntity.class);
			interpreter.set("PlayerEntity", PyPlayerEntity.class);
			interpreter.set("PlayerInventory", PyPlayerInventory.class);
			interpreter.set("RemovalReasons", PyRemovalReasons.class);
			interpreter.set("Server", PyServer.class);
			interpreter.set("StatusEffectInstance", PyStatusEffectInstance.class);
			interpreter.set("StatusEffects", PyStatusEffects.class);
			interpreter.set("Time", PyTime.class);
			interpreter.set("Vec2f", PyVec2f.class);
			interpreter.set("Vec3d", PyVec3d.class);
			interpreter.set("Weather", PyWeather.class);
			interpreter.set("World", PyWorld.class);
			interpreter.set("Worlds", PyWorlds.class);

			interpreter.set("server", new PyServer(source.getServer()));
			interpreter.set("world", new PyWorld(world));
			interpreter.set("executor", new PyExecutor(source));
			interpreter.set("pythonMCVersion", Mod.pythonMCVersion);
			interpreter.set("pythonMCMajor", Mod.major);
			interpreter.set("pythonMCMinor", Mod.minor);
			interpreter.set("pythonMCPatch", Mod.patch);

			interpreter.exec(code);

			String output = outputStream.toString().trim();
			String errorOutput = errorOutputStream.toString().trim();
			PlayerManager playerManager = source.getServer().getPlayerManager();

			if (!output.equals("")) {
				playerManager.broadcast(Text.of(output), false);
			}
			if (!errorOutput.equals("")) {
				playerManager.broadcast(Text.of(errorOutput), false);
			}

			outputStream.reset();
			errorOutputStream.reset();

		} catch (JepException e) {
			source.getServer().getPlayerManager().broadcast(Text.empty().append(e.getMessage()).formatted(Formatting.RED), false);
		}
	}
}
