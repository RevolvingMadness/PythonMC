package com.revolvingmadness.pythonmc.mixin;

import com.mojang.datafixers.DataFixer;
import com.revolvingmadness.pythonmc.accessor.DatapackContentsAccessor;
import com.revolvingmadness.pythonmc.pythondatapacks.PythonScriptManager;
import net.minecraft.resource.ResourcePackManager;
import net.minecraft.server.MinecraftServer;
import net.minecraft.server.SaveLoader;
import net.minecraft.server.WorldGenerationProgressListenerFactory;
import net.minecraft.util.ApiServices;
import net.minecraft.world.level.storage.LevelStorage;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Shadow;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfoReturnable;

import java.net.Proxy;
import java.util.Collection;
import java.util.concurrent.CompletableFuture;
import java.util.function.BooleanSupplier;

@Mixin(MinecraftServer.class)
public abstract class MinecraftServerMixin {
    PythonScriptManager pythonScriptManager;
    @Shadow
    private MinecraftServer.ResourceManagerHolder resourceManagerHolder;

    @Inject(at = @At("TAIL"), method = "<init>")
    public void injectInit(Thread serverThread, LevelStorage.Session session, ResourcePackManager dataPackManager, SaveLoader saveLoader, Proxy proxy, DataFixer dataFixer, ApiServices apiServices, WorldGenerationProgressListenerFactory worldGenerationProgressListenerFactory, CallbackInfo ci) {
        this.pythonScriptManager = new PythonScriptManager((MinecraftServer) (Object) this, ((DatapackContentsAccessor) this.resourceManagerHolder.dataPackContents()).getPythonScriptLoader());
    }

    @Inject(at = @At("HEAD"), method = "tickWorlds")
    public void injectTickWorlds(BooleanSupplier shouldKeepTicking, CallbackInfo ci) {
        this.getPythonScriptManager().tick();
    }

    public PythonScriptManager getPythonScriptManager() {
        return this.pythonScriptManager;
    }

    @Inject(at = @At("TAIL"), method = "reloadResources")
    public void injectReloadResources(Collection<String> dataPacks, CallbackInfoReturnable<CompletableFuture<Void>> cir) {
        this.pythonScriptManager.setScripts(((DatapackContentsAccessor) this.resourceManagerHolder.dataPackContents()).getPythonScriptLoader());
    }
}
