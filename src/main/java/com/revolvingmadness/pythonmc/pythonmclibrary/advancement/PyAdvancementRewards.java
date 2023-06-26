package com.revolvingmadness.pythonmc.pythonmclibrary.advancement;

import com.revolvingmadness.pythonmc.pythonmclibrary.other.PyIdentifier;
import net.minecraft.advancement.AdvancementRewards;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class PyAdvancementRewards {
    public int experience;
    public List<PyIdentifier> loot;
    public List<PyIdentifier> recipes;
    AdvancementRewards rewards;

    public PyAdvancementRewards(AdvancementRewards rewards) {
        this.experience = rewards.experience;
        this.loot = new ArrayList<>();
        Arrays.stream(rewards.loot).toList().forEach(identifier -> this.loot.add(new PyIdentifier(identifier)));
        this.recipes = new ArrayList<>();
        Arrays.stream(rewards.getRecipes()).toList().forEach(identifier -> this.recipes.add(new PyIdentifier(identifier)));
        this.rewards = rewards;
    }
}
