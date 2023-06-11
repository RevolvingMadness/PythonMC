package com.revolvingmadness.pythonmc;

import com.revolvingmadness.pythonmc.pythonmclibrary.*;
import jep.JepException;
import jep.SharedInterpreter;
import net.minecraft.server.command.ServerCommandSource;
import net.minecraft.server.world.ServerWorld;
import net.minecraft.text.Text;

public class PythonExecutor {
    static final SharedInterpreter interpreter = new SharedInterpreter();

    public static void execute(ServerCommandSource source, String code) {
        try {
            ServerWorld world = source.getWorld();
            interpreter.set("Arm", PyArm.class);
            interpreter.set("Block", PyBlock.class);
            interpreter.set("BlockPos", PyBlockPos.class);
            interpreter.set("Blocks", PyBlocks.class);
            interpreter.set("BlockState", PyBlockState.class);
            interpreter.set("DamageSources", PyDamageSources.class);
            interpreter.set("Difficulty", PyDifficulty.class);
            interpreter.set("Enchantments", PyEnchantments.class);
            interpreter.set("EnderChestInventory", PyEnderChestInventory.class);
            interpreter.set("Entities", PyEntities.class);
            interpreter.set("Entity", PyEntity.class);
            interpreter.set("Executor", PyExecutor.class);
            interpreter.set("Hand", PyHand.class);
            interpreter.set("HungerManager", PyHungerManager.class);
            interpreter.set("Item", PyItem.class);
            interpreter.set("Items", PyItems.class);
            interpreter.set("ItemStack", PyItemStack.class);
            interpreter.set("LivingEntity", PyLivingEntity.class);
            interpreter.set("NbtCompound", PyNbtCompound.class);
            interpreter.set("PlayerEntity", PyPlayerEntity.class);
            interpreter.set("PlayerInventory", PyPlayerInventory.class);
            interpreter.set("RemovalReasons", PyRemovalReasons.class);
            interpreter.set("StatusEffectInstance", PyStatusEffectInstance.class);
            interpreter.set("StatusEffects", PyStatusEffects.class);
            interpreter.set("Time", PyTime.class);
            interpreter.set("Vec2f", PyVec2f.class);
            interpreter.set("Vec3d", PyVec3d.class);
            interpreter.set("Weather", PyWeather.class);
            interpreter.set("World", PyWorld.class);

            interpreter.set("Text", Text.class);

            interpreter.set("world", new PyWorld(world));
            interpreter.set("executor", new PyExecutor(source));

            interpreter.exec(code);
        } catch (JepException e) {
            source.sendError(Text.of(e.getMessage()));
        }
    }
}
