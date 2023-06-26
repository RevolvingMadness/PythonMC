from .advancement_frame import AdvancementFrame
from ..item import ItemStack
from ..server_ import Text


class AdvancementDisplay:
    """
    Represents the display settings and visuals for an advancement.

    Attributes:
        title: The title of the advancement display.
        description: The description of the advancement display.
        hidden: Specifies whether the advancement is hidden or not.
        frame: The frame type for the advancement display.
        showToast: Specifies whether to show a toast notification for the advancement.
        icon: The icon associated with the advancement display.
    """
    title: Text
    description: Text
    hidden: bool
    frame: AdvancementFrame
    showToast: bool
    icon: ItemStack
