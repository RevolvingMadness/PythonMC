package com.revolvingmadness.pythonmc.pythonmclibrary.advancement;

import com.revolvingmadness.pythonmc.pythonmclibrary.item.PyItemStack;
import com.revolvingmadness.pythonmc.pythonmclibrary.server.text.PyText;
import net.minecraft.advancement.AdvancementDisplay;

public class PyAdvancementDisplay {
    public PyText title;
    public PyText description;
    public boolean hidden;
    public PyAdvancementFrame frame;
    public boolean showToast;
    public PyItemStack icon;
    AdvancementDisplay display;

    public PyAdvancementDisplay(AdvancementDisplay display) {
        this.title = new PyText(display.getTitle());
        this.description = new PyText(display.getDescription());
        this.hidden = display.isHidden();
        this.frame = PyAdvancementFrame.fromFrame(display.getFrame());
        this.showToast = display.shouldShowToast();
        this.icon = new PyItemStack(display.getIcon());
        this.display = display;
    }
}
