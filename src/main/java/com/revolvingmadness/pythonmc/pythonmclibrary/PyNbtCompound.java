package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.nbt.*;

import java.util.List;
import java.util.Map;

public class PyNbtCompound {
	NbtCompound compound;
	
	public PyNbtCompound(NbtCompound compound) {
		this.compound = compound;
	}
	
	public static NbtCompound fromMap(Map<String, Object> map) {
		return (NbtCompound) toNbtElement(map);
	}
	
	public static NbtElement toNbtElement(Object input) {
		NbtElement result = null;
		
		if (input instanceof String) {
			result = NbtString.of((String) input);
		} else if (input instanceof Integer) {
			result = NbtInt.of((Integer) input);
		} else if (input instanceof Float) {
			result = NbtFloat.of((Float) input);
		} else if (input instanceof Long) {
			result = NbtLong.of((Long) input);
		} else if (input instanceof Boolean) {
			result = NbtByte.of((Boolean) input);
		} else if (input instanceof List<?>) {
			NbtList list = new NbtList();
			for (Object element : (List) input) {
				list.add(toNbtElement(element));
			}
			result = list;
		} else if (input instanceof Map<?, ?>) {
			NbtCompound list = new NbtCompound();
			((Map<String, Object>) input).forEach((key, value) -> list.put(key, toNbtElement(value)));
			result = list;
		}
		
		return result;
	}
}
