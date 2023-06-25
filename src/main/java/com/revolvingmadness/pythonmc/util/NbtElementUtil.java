package com.revolvingmadness.pythonmc.util;

import net.minecraft.nbt.*;

import java.util.*;

public class NbtElementUtil {
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
			for (Object element : (List<?>) input) {
				list.add(toNbtElement(element));
			}
			result = list;
		} else if (input instanceof Map<?, ?>) {
			NbtCompound list = new NbtCompound();
			// noinspection unchecked
			((Map<String, Object>) input).forEach((key, value) -> list.put(key, toNbtElement(value)));
			result = list;
		}
		
		return result;
	}
	
	public static Object toObject(NbtElement element) {
		Object result = null;
		switch (element.getType()) {
			case NbtElement.BYTE_TYPE -> result = ((NbtByte) element).byteValue();
			case NbtElement.SHORT_TYPE -> result = ((NbtShort) element).shortValue();
			case NbtElement.INT_TYPE -> result = ((NbtInt) element).intValue();
			case NbtElement.LONG_TYPE -> result = ((NbtLong) element).longValue();
			case NbtElement.FLOAT_TYPE -> result = ((NbtFloat) element).floatValue();
			case NbtElement.DOUBLE_TYPE -> result = ((NbtDouble) element).doubleValue();
			case NbtElement.BYTE_ARRAY_TYPE -> result = ((NbtByteArray) element).getByteArray();
			case NbtElement.STRING_TYPE -> result = element.asString();
			case NbtElement.LIST_TYPE -> {
				List<NbtElement> list = ((NbtList) element).stream().toList();
				result = new ArrayList<>();
				for (NbtElement element1 : list) {
					// noinspection unchecked
					((List<Object>) result).add(toObject(element1));
				}
			}
			case NbtElement.COMPOUND_TYPE -> {
				Set<String> nbtKeys = ((NbtCompound) element).getKeys();
				result = new HashMap<>();
				for (String nbtKey : nbtKeys) {
					// noinspection unchecked
					((Map<String, Object>) result).put(nbtKey, toObject(Objects.requireNonNull(((NbtCompound) element).get(nbtKey))));
				}
			}
			case NbtElement.INT_ARRAY_TYPE -> result = ((NbtIntArray) element).getIntArray();
			case NbtElement.LONG_ARRAY_TYPE -> result = ((NbtLongArray) element).getLongArray();
		}
		return result;
	}
	
}
