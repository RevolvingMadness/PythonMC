from ..other import Identifier


class AdvancementRewards:
    """
    Represents the rewards associated with completing an advancement.

    Attributes:
        experience (int): The amount of experience rewarded for completing the advancement.
        loot (list[Identifier]): The list of identifiers for loot rewarded upon completion.
        recipes (list[Identifier]): The list of identifiers for recipes unlocked upon completion.
    """
    experience: int
    loot: list[Identifier]
    recipes: list[Identifier]
