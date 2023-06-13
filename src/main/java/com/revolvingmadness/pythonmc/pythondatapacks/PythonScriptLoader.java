package com.revolvingmadness.pythonmc.pythondatapacks;

import com.google.common.collect.ImmutableMap;
import com.revolvingmadness.pythonmc.Mod;
import net.minecraft.registry.tag.TagGroupLoader;
import net.minecraft.resource.Resource;
import net.minecraft.resource.ResourceFinder;
import net.minecraft.resource.ResourceManager;
import net.minecraft.resource.ResourceReloader;
import net.minecraft.util.Identifier;
import net.minecraft.util.profiler.Profiler;

import java.util.*;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.CompletionStage;
import java.util.concurrent.Executor;

public class PythonScriptLoader implements ResourceReloader {
	private static final ResourceFinder FINDER = new ResourceFinder("python", ".py");

	private Map<Identifier, PythonScript> scripts = ImmutableMap.of();

	private final TagGroupLoader<PythonScript> tagLoader = new TagGroupLoader<>(this::get, "tags/python");

	private Map<Identifier, Collection<PythonScript>> tags = Map.of();

	public Optional<PythonScript> get(Identifier id) {
		return Optional.ofNullable(this.scripts.get(id));
	}

	public Map<Identifier, PythonScript> getScripts() {
		return this.scripts;
	}

	public Collection<PythonScript> getTagOrEmpty(Identifier id) {
		return this.tags.getOrDefault(id, List.of());
	}

	public Iterable<Identifier> getTags() {
		return this.tags.keySet();
	}

	@Override
	public CompletableFuture<Void> reload(Synchronizer synchronizer, ResourceManager manager, Profiler prepareProfiler, Profiler applyProfiler, Executor prepareExecutor, Executor applyExecutor) {
		CompletableFuture<Map<Identifier, List<TagGroupLoader.TrackedEntry>>> completableFuture = CompletableFuture.supplyAsync(() -> this.tagLoader.loadTags(manager), prepareExecutor);
		CompletionStage<Map<Identifier, CompletableFuture<PythonScript>>> completableFuture2 = CompletableFuture.supplyAsync(() -> FINDER.findResources(manager), prepareExecutor).thenComposeAsync(scripts -> {
			HashMap<Identifier, CompletableFuture<PythonScript>> map = new HashMap<>();
			for (Map.Entry<Identifier, Resource> entry : scripts.entrySet()) {
				Identifier identifier = entry.getKey();
				Identifier identifier2 = FINDER.toResourceId(identifier);
				map.put(identifier2, CompletableFuture.supplyAsync(() -> {
					String content = PythonScript.readFromResource(entry.getValue());
					return new PythonScript(identifier2, content);
				}, prepareExecutor));
			}
			CompletableFuture<Void> allFutures = CompletableFuture.allOf(map.values().toArray(new CompletableFuture[0]));
			return allFutures.thenApply((unused) -> map);
		});
		return completableFuture.thenCombine(completableFuture2, (tags, scripts) -> {
			ImmutableMap.Builder<Identifier, PythonScript> builder = ImmutableMap.builder();
			scripts.forEach((id, scriptFuture) -> scriptFuture.handle((script, ex) -> {
				if (ex != null) {
					Mod.LOGGER.error("Failed to load script '" + id + "'. Reason:");
					Mod.LOGGER.error(String.valueOf(ex));
				} else {
					builder.put(id, script);
					Mod.LOGGER.info("Loaded script '" + id + "'");
				}
				return null;
			}).join());
			this.scripts = builder.build();
			this.tags = this.tagLoader.buildGroup(tags);
			return CompletableFuture.completedFuture(null);
		}).thenComposeAsync(synchronizer::whenPrepared, applyExecutor).thenAcceptAsync(intermediate -> {
			// Handle the intermediate result as needed
		}, applyExecutor);
	}
}
