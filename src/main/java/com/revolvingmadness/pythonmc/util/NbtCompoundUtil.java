package com.revolvingmadness.pythonmc.util;

import net.minecraft.nbt.NbtCompound;

import java.util.Map;

public class NbtCompoundUtil {
    public static NbtCompound fromMap(Map<String, Object> map) {
        return (NbtCompound) NbtElementUtil.toNbtElement(map);
    }
}
