package com.revolvingmadness.pythonmc.pythonmclibrary;

import net.minecraft.util.math.Vec2f;

public class PyVec2f {
    final Vec2f vec;
    public final float x;
    public final float y;

    public PyVec2f(Vec2f vec) {
        this.vec = vec;
        this.x = vec.x;
        this.y = vec.y;
    }

    @Override
    public String toString() {
        return "(" + this.x + ", " + this.y + ")";
    }
}
