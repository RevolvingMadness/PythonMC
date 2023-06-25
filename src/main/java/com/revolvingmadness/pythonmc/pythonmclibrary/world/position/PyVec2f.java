package com.revolvingmadness.pythonmc.pythonmclibrary.world.position;

import net.minecraft.util.math.Vec2f;

public class PyVec2f {
    public final float x;
    public final float y;
    final Vec2f vec;

    public PyVec2f(Number x, Number y) {
        this(new Vec2f(x.floatValue(), y.floatValue()));
    }

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
