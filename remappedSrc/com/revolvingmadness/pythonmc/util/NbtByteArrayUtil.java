package com.revolvingmadness.pythonmc.util;

import net.minecraft.nbt.NbtByteArray;

import java.util.ArrayList;
import java.util.List;

public class NbtByteArrayUtil {
    public static List<Byte> toByteList(NbtByteArray byteArray) {
        List<Byte> result = new ArrayList<>();
        for (Byte byte_ : byteArray.getByteArray()) {
            result.add(byte_);
        }
        return result;
    }
}
