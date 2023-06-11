package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.entity.Entity;
import net.minecraft.entity.EntityType;
import net.minecraft.nbt.NbtCompound;
import net.minecraft.registry.Registries;
import net.minecraft.server.world.ServerWorld;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class PyWorld {
	ServerWorld world;
	
	public PyWorld(ServerWorld world) {
		this.world = world;
	}
	
	public long getSeed() {
		return this.world.getSeed();
	}
	
	public PyDifficulty getDifficulty() {
		return new PyDifficulty(this.world.getDifficulty());
	}
	
	public List<PyPlayerEntity> getPlayers() {
		List<PyPlayerEntity> result = new ArrayList<>();
		this.world.getPlayers().forEach(player -> result.add(new PyPlayerEntity(player)));
		return result;
	}
	
	public PyBlockState getBlock(PyBlockPos blockPos) {
		return new PyBlockState(this.world.getBlockState(blockPos.blockPos));
	}
	
	public void setBlock(PyBlockPos blockPos, PyBlockState block) {
		this.world.setBlockState(blockPos.blockPos, block.blockState);
	}
	
	public void spawnEntity(PyEntities entity, PyBlockPos pos, Map<String, Object> nbtMap) {
		NbtCompound nbt = PyNbtCompound.fromMap(nbtMap);
		nbt.putString("id", Registries.ENTITY_TYPE.getId(entity.toEntityType()).toString());
		Entity entity2 = EntityType.loadEntityWithPassengers(nbt, this.world, entity1 -> {
			entity1.setPosition(pos.x, pos.y, pos.z);
			return entity1;
		});
		this.world.spawnEntity(entity2);
	}
}
