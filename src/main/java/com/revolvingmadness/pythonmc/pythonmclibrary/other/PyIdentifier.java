package com.revolvingmadness.pythonmc.pythonmclibrary.other;

import net.minecraft.util.Identifier;

public class PyIdentifier {
    public String namespace;
    public String path;
    public Identifier identifier;

    public PyIdentifier(String namespace, String path) {
        this(new Identifier(namespace, path));
    }

    public PyIdentifier(Identifier identifier) {
        this.namespace = identifier.getNamespace();
        this.path = identifier.getPath();
        this.identifier = identifier;
    }
}
