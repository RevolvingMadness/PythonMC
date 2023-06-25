package com.revolvingmadness.pythonmc.pythonmclibrary.world;

import com.revolvingmadness.pythonmc.pythonmclibrary.block.PyBlockPos;
import com.revolvingmadness.pythonmc.pythonmclibrary.block.PyBlockState;
import com.revolvingmadness.pythonmc.pythonmclibrary.block.PyBlocks;
import com.revolvingmadness.pythonmc.pythonmclibrary.entity.PyEntities;
import com.revolvingmadness.pythonmc.pythonmclibrary.server.difficulty.PyDifficulty;
import com.revolvingmadness.pythonmc.util.NbtCompoundUtil;
import net.minecraft.entity.Entity;
import net.minecraft.entity.EntityType;
import net.minecraft.nbt.NbtCompound;
import net.minecraft.registry.Registries;
import net.minecraft.server.world.ServerWorld;
import net.minecraft.util.math.intprovider.IntProvider;

import java.util.Map;

public class PyWorld {
	public final ServerWorld world;
	
	public PyWorld(ServerWorld world) {
		this.world = world;
	}
	
	public long getSeed() {
		return this.world.getSeed();
	}
	
	public PyDifficulty getDifficulty() {
		return new PyDifficulty(this.world.getDifficulty());
	}
	
	public PyBlockState getBlock(PyBlockPos blockPos) {
		return new PyBlockState(this.world.getBlockState(blockPos.blockPos));
	}
	
	public PyBlockState getBlock(Number x, Number y, Number z) {
		return this.getBlock(new PyBlockPos(x, y, z));
	}
	
	public void setBlock(PyBlockPos blockPos, PyBlockState block) {
		this.world.setBlockState(blockPos.blockPos, block.blockState);
	}
	
	public void setBlock(Number x, Number y, Number z, PyBlockState block) {
		this.setBlock(new PyBlockPos(x, y, z), block);
	}
	
	public void setBlock(PyBlockPos blockPos, PyBlocks block) {
		this.world.setBlockState(blockPos.blockPos, block.toBlock().getDefaultState());
	}
	
	public void setBlock(Number x, Number y, Number z, PyBlocks block) {
		this.setBlock(new PyBlockPos(x, y, z), block);
	}
	
	public void spawnEntity(PyEntities entity, PyBlockPos pos, Map<String, Object> nbtMap) {
		NbtCompound nbt = NbtCompoundUtil.fromMap(nbtMap);
		nbt.putString("id", Registries.ENTITY_TYPE.getId(entity.toEntityType()).toString());
		Entity entity2 = EntityType.loadEntityWithPassengers(nbt, this.world, entity1 -> {
			entity1.setPosition(pos.x, pos.y, pos.z);
			return entity1;
		});
		this.world.spawnEntity(entity2);
	}
	
	public void spawnEntity(PyEntities entity, Number x, Number y, Number z, Map<String, Object> nbtMap) {
		this.spawnEntity(entity, new PyBlockPos(x, y, z), nbtMap);
	}
	
	public void spawnParticle(PyParticles particle, Number x, Number y, Number z, Number count, Number deltaX, Number deltaY, Number deltaZ, Number speed) {
		this.world.spawnParticles(particle.toParticle(), x.doubleValue(), y.doubleValue(), z.doubleValue(), count.intValue(), deltaX.doubleValue(), deltaY.doubleValue(), deltaZ.doubleValue(), speed.doubleValue());
	}
	
	public void setTime(PyTime time) {
		this.world.setTimeOfDay(time.toTimeLong());
	}
	
	public void setSpawnPos(PyBlockPos pos, Number angle) {
		this.world.setSpawnPos(pos.blockPos, angle.floatValue());
	}
	
	public void setSpawnPos(PyBlockPos pos) {
		this.setSpawnPos(pos, 0.0);
	}
	
	public void setSpawnPos(Number x, Number y, Number z, Number angle) {
		this.setSpawnPos(new PyBlockPos(x, y, z), angle);
	}
	
	public void setSpawnPos(Number x, Number y, Number z) {
		this.setSpawnPos(new PyBlockPos(x, y, z), 0.0);
	}
	
	private int processDuration(Number duration, IntProvider provider) {
		if (duration.intValue() == -1) {
			return provider.get(this.world.getRandom());
		}
		return duration.intValue();
	}
	
	public void setWeather(PyWeather weather, Number duration) {
		int intDuration = duration.intValue();
		switch (weather) {
			case CLEAR ->
					this.world.setWeather(this.processDuration(intDuration, ServerWorld.CLEAR_WEATHER_DURATION_PROVIDER), 0, false, false);
			case RAIN ->
					this.world.setWeather(0, this.processDuration(intDuration, ServerWorld.RAIN_WEATHER_DURATION_PROVIDER), true, false);
			case THUNDER ->
					this.world.setWeather(0, this.processDuration(intDuration, ServerWorld.THUNDER_WEATHER_DURATION_PROVIDER), true, true);
		}
	}
	
	public void setWeather(PyWeather weather) {
		this.setWeather(weather, -1);
	}
}
