from .advancement_frame import AdvancementFrame
from ..item import ItemStack
from ..server_ import Text


class AdvancementDisplay:
    title: Text
    description: Text
    hidden: bool
    frame: AdvancementFrame
    showToast: bool
    icon: ItemStack
