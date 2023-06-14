package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.server.command.ServerCommandSource;
import net.minecraft.text.Text;
import net.minecraft.util.math.Vec2f;

public class PyExecutor {
	final ServerCommandSource source;
	public final String name;
	public final String displayName;
	public final PyVec3d position;
	public final PyPlayerEntity player;
	public final PyWorld world;
	public final PyEntity entity;
	public final boolean isExecutedByPlayer;
	public final Vec2f rotation;

	public PyExecutor(ServerCommandSource source) {
		this.source = source;
		this.name = source.getName();
		this.player = new PyPlayerEntity(source.getPlayer());
		this.displayName = source.getDisplayName().getString();
		this.position = new PyVec3d(source.getPosition());
		this.world = new PyWorld(source.getWorld());
		this.entity = new PyEntity(source.getEntity());
		this.isExecutedByPlayer = source.isExecutedByPlayer();
		this.rotation = source.getRotation();
	}

	public void sendMessage(Object message) {
		this.source.sendMessage(Text.of(String.valueOf(message)));
	}

	public void sendMessage(PyText text) {
		this.source.sendMessage(text.text);
	}

	public void sendError(Object error) {
		this.source.sendError(Text.of(String.valueOf(error)));
	}

	public void sendError(PyText text) {
		this.source.sendError(text.text);
	}

	@Override
	public String toString() {
		return this.name;
	}
}
