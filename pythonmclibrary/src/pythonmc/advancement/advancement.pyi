from .advancement_display import AdvancementDisplay
from ..other import Identifier
from ..server_ import Text


class Advancement:
    """
    Represents an advancement.

    Attributes:
        id (Identifier): The unique identifier of the advancement.
        requirements (list[list[str]]): The requirements needed to unlock the advancement.
        text (Text): The text description or details of the advancement.
        parent (Advancement): The parent advancement, if any, that must be completed before unlocking this advancement.
        display (AdvancementDisplay): The display settings and visuals for the advancement.
        rewards (AdvancementRewards): The rewards associated with completing the advancement.
    """
    id: Identifier
    requirements: list[list[str]]
    text: Text
    parent: Advancement
    display: AdvancementDisplay
    rewards: AdvancementRewards
