package com.revolvingmadness.pythonmc.pythondatapacks;

import com.revolvingmadness.pythonmc.Mod;
import com.revolvingmadness.pythonmc.pythonrunner.PythonExecutor;
import net.minecraft.server.MinecraftServer;
import net.minecraft.server.command.ServerCommandSource;
import net.minecraft.util.Identifier;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Optional;

public class PythonScriptManager {
	private static final Identifier TICK_TAG_ID = new Identifier(Mod.MOD_ID, "tick");

	private static final Identifier LOAD_TAG_ID = new Identifier(Mod.MOD_ID, "load");

	private Collection<PythonScript> tickScripts = new ArrayList<>();

	private boolean justLoaded;

	private final MinecraftServer server;

	private final ServerCommandSource source;

	private PythonScriptLoader loader;

	public PythonScriptManager(MinecraftServer server, PythonScriptLoader loader) {
		this.server = server;
		this.source = server.getCommandSource();
		this.loader = loader;
		this.load(loader);
	}

	private void load(PythonScriptLoader loader) {
		this.tickScripts = loader.getTagOrEmpty(TICK_TAG_ID);
		this.justLoaded = true;
	}

	public Optional<PythonScript> getScript(Identifier id) {
		return this.loader.get(id);
	}

	public Collection<PythonScript> getTag(Identifier id) {
		return this.loader.getTagOrEmpty(id);
	}

	public void setScripts(PythonScriptLoader loader) {
		this.loader = loader;
		this.load(loader);
	}

	public void tick() {
		if (this.justLoaded) {
			this.justLoaded = false;
			PythonExecutor.init();
			Collection<PythonScript> loadScripts = this.loader.getTagOrEmpty(LOAD_TAG_ID);
			this.executeAll(loadScripts, LOAD_TAG_ID);
		}
		this.executeAll(this.tickScripts, TICK_TAG_ID);
	}

	public void executeAll(Collection<PythonScript> scripts, Identifier label) {
		this.server.getProfiler().push(label::toString);
		for (PythonScript script : scripts) {
			this.execute(script);
		}
		this.server.getProfiler().pop();
	}

	public void execute(PythonScript script) {
		PythonExecutor.execute(this.source, script.namespace, script.path, script.content);
	}
}
