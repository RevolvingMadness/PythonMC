package com.revolvingmadness.pythonmc.pythonmclibrary.advancement;

import com.revolvingmadness.pythonmc.pythonmclibrary.other.PyIdentifier;
import com.revolvingmadness.pythonmc.pythonmclibrary.server.text.PyText;
import net.minecraft.advancement.Advancement;

import java.util.List;

public class PyAdvancement {
    public PyIdentifier id;
    public List<List<String>> requirements;
    public PyText text;
    public PyAdvancement parent;
    public PyAdvancementDisplay display;
    public PyAdvancementRewards rewards;
    Advancement advancement;

    public PyAdvancement(Advancement advancement) {
        this.advancement = advancement;
    }
}
