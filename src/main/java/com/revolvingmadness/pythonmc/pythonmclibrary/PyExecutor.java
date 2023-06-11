package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.server.command.ServerCommandSource;
import net.minecraft.text.Text;
import net.minecraft.util.math.Vec2f;

public class PyExecutor {
	ServerCommandSource source;
	public String name;
	public String displayName;
	public PyVec3d position;
	public PyPlayerEntity player;
	public PyWorld world;
	public PyEntity entity;
	public Boolean isExecutedByPlayer;
	public Vec2f rotation;
	
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
	
	public void sendError(Object error) {
		this.source.sendError(Text.of(String.valueOf(error)));
	}
	
	@Override
	public String toString() {
		return this.name;
	}
}
