package com.revolvingmadness.pythonmc.pythonmclibrary.server.gamemode;

import net.minecraft.world.GameMode;

public class PyGameMode {
	final GameMode gameMode;
	public final int id;
	public final String name;
	public static PyGameMode SURVIVAL = new PyGameMode(GameMode.SURVIVAL);
	public static PyGameMode CREATIVE = new PyGameMode(GameMode.CREATIVE);
	public static PyGameMode ADVENTURE = new PyGameMode(GameMode.ADVENTURE);
	public static PyGameMode SPECTATOR = new PyGameMode(GameMode.SPECTATOR);
	
	public PyGameMode(GameMode gameMode) {
		this.gameMode = gameMode;
		this.id = gameMode.getId();
		this.name = gameMode.getName();
	}
	
	@Override
	public String toString() {
		return this.name;
	}
}
