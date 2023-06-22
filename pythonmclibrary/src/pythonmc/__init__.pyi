from __future__ import annotations

from numbers import Number
from typing import overload

class Arm:
    """
    Represents the arm of a player.
    """

    LEFT: object
    RIGHT: object

class Block:
    item: Item
    name: str
    blastResistance: float
    velocityMultiplier: float
    jumpVelocityMultiplier: float
    slipperiness: float

    def __init__(self, block: Blocks) -> None:
        """
        Initializes a new Block object.

        Args:
            block (Blocks): The block object representing the block.

        Returns:
            None
        """

class BlockPos:
    """
    Represents a position in the world.

    Attributes:
        x (int): The x-coordinate of the position.
        y (int): The y-coordinate of the position.
        z (int): The z-coordinate of the position.
    """

    x: int
    y: int
    z: int

    def __init__(self, x: Number, y: Number, z: Number) -> None:
        """
        Initializes a new BlockPos object.

        Args:
            x (Number): The x-coordinate of the position.
            y (Number): The y-coordinate of the position.
            z (Number): The z-coordinate of the position.

        Returns:
            None
        """

class Blocks:
    """
    The Blocks class represents a collection of block objects in Minecraft game.
    """

    AIR: object
    STONE: object
    GRANITE: object
    POLISHED_GRANITE: object
    DIORITE: object
    POLISHED_DIORITE: object
    ANDESITE: object
    POLISHED_ANDESITE: object
    GRASS_BLOCK: object
    DIRT: object
    COARSE_DIRT: object
    PODZOL: object
    COBBLESTONE: object
    OAK_PLANKS: object
    SPRUCE_PLANKS: object
    BIRCH_PLANKS: object
    JUNGLE_PLANKS: object
    ACACIA_PLANKS: object
    CHERRY_PLANKS: object
    DARK_OAK_PLANKS: object
    MANGROVE_PLANKS: object
    BAMBOO_PLANKS: object
    BAMBOO_MOSAIC: object
    OAK_SAPLING: object
    SPRUCE_SAPLING: object
    BIRCH_SAPLING: object
    JUNGLE_SAPLING: object
    ACACIA_SAPLING: object
    CHERRY_SAPLING: object
    DARK_OAK_SAPLING: object
    MANGROVE_PROPAGULE: object
    BEDROCK: object
    WATER: object
    LAVA: object
    SAND: object
    SUSPICIOUS_SAND: object
    RED_SAND: object
    GRAVEL: object
    SUSPICIOUS_GRAVEL: object
    GOLD_ORE: object
    DEEPSLATE_GOLD_ORE: object
    IRON_ORE: object
    DEEPSLATE_IRON_ORE: object
    COAL_ORE: object
    DEEPSLATE_COAL_ORE: object
    NETHER_GOLD_ORE: object
    OAK_LOG: object
    SPRUCE_LOG: object
    BIRCH_LOG: object
    JUNGLE_LOG: object
    ACACIA_LOG: object
    CHERRY_LOG: object
    DARK_OAK_LOG: object
    MANGROVE_LOG: object
    MANGROVE_ROOTS: object
    MUDDY_MANGROVE_ROOTS: object
    BAMBOO_BLOCK: object
    STRIPPED_SPRUCE_LOG: object
    STRIPPED_BIRCH_LOG: object
    STRIPPED_JUNGLE_LOG: object
    STRIPPED_ACACIA_LOG: object
    STRIPPED_CHERRY_LOG: object
    STRIPPED_DARK_OAK_LOG: object
    STRIPPED_OAK_LOG: object
    STRIPPED_MANGROVE_LOG: object
    STRIPPED_BAMBOO_BLOCK: object
    OAK_WOOD: object
    SPRUCE_WOOD: object
    BIRCH_WOOD: object
    JUNGLE_WOOD: object
    ACACIA_WOOD: object
    CHERRY_WOOD: object
    DARK_OAK_WOOD: object
    MANGROVE_WOOD: object
    STRIPPED_OAK_WOOD: object
    STRIPPED_SPRUCE_WOOD: object
    STRIPPED_BIRCH_WOOD: object
    STRIPPED_JUNGLE_WOOD: object
    STRIPPED_ACACIA_WOOD: object
    STRIPPED_CHERRY_WOOD: object
    STRIPPED_DARK_OAK_WOOD: object
    STRIPPED_MANGROVE_WOOD: object
    OAK_LEAVES: object
    SPRUCE_LEAVES: object
    BIRCH_LEAVES: object
    JUNGLE_LEAVES: object
    ACACIA_LEAVES: object
    CHERRY_LEAVES: object
    DARK_OAK_LEAVES: object
    MANGROVE_LEAVES: object
    AZALEA_LEAVES: object
    FLOWERING_AZALEA_LEAVES: object
    SPONGE: object
    WET_SPONGE: object
    GLASS: object
    LAPIS_ORE: object
    DEEPSLATE_LAPIS_ORE: object
    LAPIS_BLOCK: object
    DISPENSER: object
    SANDSTONE: object
    CHISELED_SANDSTONE: object
    CUT_SANDSTONE: object
    NOTE_BLOCK: object
    WHITE_BED: object
    ORANGE_BED: object
    MAGENTA_BED: object
    LIGHT_BLUE_BED: object
    YELLOW_BED: object
    LIME_BED: object
    PINK_BED: object
    GRAY_BED: object
    LIGHT_GRAY_BED: object
    CYAN_BED: object
    PURPLE_BED: object
    BLUE_BED: object
    BROWN_BED: object
    GREEN_BED: object
    RED_BED: object
    BLACK_BED: object
    POWERED_RAIL: object
    DETECTOR_RAIL: object
    STICKY_PISTON: object
    COBWEB: object
    GRASS: object
    FERN: object
    DEAD_BUSH: object
    SEAGRASS: object
    TALL_SEAGRASS: object
    PISTON: object
    PISTON_HEAD: object
    WHITE_WOOL: object
    ORANGE_WOOL: object
    MAGENTA_WOOL: object
    LIGHT_BLUE_WOOL: object
    YELLOW_WOOL: object
    LIME_WOOL: object
    PINK_WOOL: object
    GRAY_WOOL: object
    LIGHT_GRAY_WOOL: object
    CYAN_WOOL: object
    PURPLE_WOOL: object
    BLUE_WOOL: object
    BROWN_WOOL: object
    GREEN_WOOL: object
    RED_WOOL: object
    BLACK_WOOL: object
    MOVING_PISTON: object
    DANDELION: object
    TORCHFLOWER: object
    POPPY: object
    BLUE_ORCHID: object
    ALLIUM: object
    AZURE_BLUET: object
    RED_TULIP: object
    ORANGE_TULIP: object
    WHITE_TULIP: object
    PINK_TULIP: object
    OXEYE_DAISY: object
    CORNFLOWER: object
    WITHER_ROSE: object
    LILY_OF_THE_VALLEY: object
    BROWN_MUSHROOM: object
    RED_MUSHROOM: object
    GOLD_BLOCK: object
    IRON_BLOCK: object
    BRICKS: object
    TNT: object
    BOOKSHELF: object
    CHISELED_BOOKSHELF: object
    MOSSY_COBBLESTONE: object
    OBSIDIAN: object
    TORCH: object
    WALL_TORCH: object
    FIRE: object
    SOUL_FIRE: object
    SPAWNER: object
    OAK_STAIRS: object
    CHEST: object
    REDSTONE_WIRE: object
    DIAMOND_ORE: object
    DEEPSLATE_DIAMOND_ORE: object
    DIAMOND_BLOCK: object
    CRAFTING_TABLE: object
    WHEAT: object
    FARMLAND: object
    FURNACE: object
    OAK_SIGN: object
    SPRUCE_SIGN: object
    BIRCH_SIGN: object
    ACACIA_SIGN: object
    CHERRY_SIGN: object
    JUNGLE_SIGN: object
    DARK_OAK_SIGN: object
    MANGROVE_SIGN: object
    BAMBOO_SIGN: object
    OAK_DOOR: object
    LADDER: object
    RAIL: object
    COBBLESTONE_STAIRS: object
    OAK_WALL_SIGN: object
    SPRUCE_WALL_SIGN: object
    BIRCH_WALL_SIGN: object
    ACACIA_WALL_SIGN: object
    CHERRY_WALL_SIGN: object
    JUNGLE_WALL_SIGN: object
    DARK_OAK_WALL_SIGN: object
    MANGROVE_WALL_SIGN: object
    BAMBOO_WALL_SIGN: object
    OAK_HANGING_SIGN: object
    SPRUCE_HANGING_SIGN: object
    BIRCH_HANGING_SIGN: object
    ACACIA_HANGING_SIGN: object
    CHERRY_HANGING_SIGN: object
    JUNGLE_HANGING_SIGN: object
    DARK_OAK_HANGING_SIGN: object
    CRIMSON_HANGING_SIGN: object
    WARPED_HANGING_SIGN: object
    MANGROVE_HANGING_SIGN: object
    BAMBOO_HANGING_SIGN: object
    OAK_WALL_HANGING_SIGN: object
    SPRUCE_WALL_HANGING_SIGN: object
    BIRCH_WALL_HANGING_SIGN: object
    ACACIA_WALL_HANGING_SIGN: object
    CHERRY_WALL_HANGING_SIGN: object
    JUNGLE_WALL_HANGING_SIGN: object
    DARK_OAK_WALL_HANGING_SIGN: object
    MANGROVE_WALL_HANGING_SIGN: object
    CRIMSON_WALL_HANGING_SIGN: object
    WARPED_WALL_HANGING_SIGN: object
    BAMBOO_WALL_HANGING_SIGN: object
    LEVER: object
    STONE_PRESSURE_PLATE: object
    IRON_DOOR: object
    OAK_PRESSURE_PLATE: object
    SPRUCE_PRESSURE_PLATE: object
    BIRCH_PRESSURE_PLATE: object
    JUNGLE_PRESSURE_PLATE: object
    ACACIA_PRESSURE_PLATE: object
    CHERRY_PRESSURE_PLATE: object
    DARK_OAK_PRESSURE_PLATE: object
    MANGROVE_PRESSURE_PLATE: object
    BAMBOO_PRESSURE_PLATE: object
    REDSTONE_ORE: object
    DEEPSLATE_REDSTONE_ORE: object
    REDSTONE_TORCH: object
    REDSTONE_WALL_TORCH: object
    STONE_BUTTON: object
    SNOW: object
    ICE: object
    SNOW_BLOCK: object
    CACTUS: object
    CLAY: object
    SUGAR_CANE: object
    JUKEBOX: object
    OAK_FENCE: object
    PUMPKIN: object
    NETHERRACK: object
    SOUL_SAND: object
    SOUL_SOIL: object
    BASALT: object
    POLISHED_BASALT: object
    SOUL_TORCH: object
    SOUL_WALL_TORCH: object
    GLOWSTONE: object
    NETHER_PORTAL: object
    CARVED_PUMPKIN: object
    JACK_O_LANTERN: object
    CAKE: object
    REPEATER: object
    WHITE_STAINED_GLASS: object
    ORANGE_STAINED_GLASS: object
    MAGENTA_STAINED_GLASS: object
    LIGHT_BLUE_STAINED_GLASS: object
    YELLOW_STAINED_GLASS: object
    LIME_STAINED_GLASS: object
    PINK_STAINED_GLASS: object
    GRAY_STAINED_GLASS: object
    LIGHT_GRAY_STAINED_GLASS: object
    CYAN_STAINED_GLASS: object
    PURPLE_STAINED_GLASS: object
    BLUE_STAINED_GLASS: object
    BROWN_STAINED_GLASS: object
    GREEN_STAINED_GLASS: object
    RED_STAINED_GLASS: object
    BLACK_STAINED_GLASS: object
    OAK_TRAPDOOR: object
    SPRUCE_TRAPDOOR: object
    BIRCH_TRAPDOOR: object
    JUNGLE_TRAPDOOR: object
    ACACIA_TRAPDOOR: object
    CHERRY_TRAPDOOR: object
    DARK_OAK_TRAPDOOR: object
    MANGROVE_TRAPDOOR: object
    BAMBOO_TRAPDOOR: object
    STONE_BRICKS: object
    MOSSY_STONE_BRICKS: object
    CRACKED_STONE_BRICKS: object
    CHISELED_STONE_BRICKS: object
    PACKED_MUD: object
    MUD_BRICKS: object
    INFESTED_STONE: object
    INFESTED_COBBLESTONE: object
    INFESTED_STONE_BRICKS: object
    INFESTED_MOSSY_STONE_BRICKS: object
    INFESTED_CRACKED_STONE_BRICKS: object
    INFESTED_CHISELED_STONE_BRICKS: object
    BROWN_MUSHROOM_BLOCK: object
    RED_MUSHROOM_BLOCK: object
    MUSHROOM_STEM: object
    IRON_BARS: object
    CHAIN: object
    GLASS_PANE: object
    MELON: object
    ATTACHED_PUMPKIN_STEM: object
    ATTACHED_MELON_STEM: object
    PUMPKIN_STEM: object
    MELON_STEM: object
    VINE: object
    GLOW_LICHEN: object
    OAK_FENCE_GATE: object
    BRICK_STAIRS: object
    STONE_BRICK_STAIRS: object
    MUD_BRICK_STAIRS: object
    MYCELIUM: object
    LILY_PAD: object
    NETHER_BRICKS: object
    NETHER_BRICK_FENCE: object
    NETHER_BRICK_STAIRS: object
    NETHER_WART: object
    ENCHANTING_TABLE: object
    BREWING_STAND: object
    CAULDRON: object
    WATER_CAULDRON: object
    LAVA_CAULDRON: object
    POWDER_SNOW_CAULDRON: object
    END_PORTAL: object
    END_PORTAL_FRAME: object
    END_STONE: object
    DRAGON_EGG: object
    REDSTONE_LAMP: object
    COCOA: object
    SANDSTONE_STAIRS: object
    EMERALD_ORE: object
    DEEPSLATE_EMERALD_ORE: object
    ENDER_CHEST: object
    TRIPWIRE_HOOK: object
    TRIPWIRE: object
    EMERALD_BLOCK: object
    SPRUCE_STAIRS: object
    BIRCH_STAIRS: object
    JUNGLE_STAIRS: object
    COMMAND_BLOCK: object
    BEACON: object
    COBBLESTONE_WALL: object
    MOSSY_COBBLESTONE_WALL: object
    FLOWER_POT: object
    POTTED_TORCHFLOWER: object
    POTTED_OAK_SAPLING: object
    POTTED_SPRUCE_SAPLING: object
    POTTED_BIRCH_SAPLING: object
    POTTED_JUNGLE_SAPLING: object
    POTTED_ACACIA_SAPLING: object
    POTTED_CHERRY_SAPLING: object
    POTTED_DARK_OAK_SAPLING: object
    POTTED_MANGROVE_PROPAGULE: object
    POTTED_FERN: object
    POTTED_DANDELION: object
    POTTED_POPPY: object
    POTTED_BLUE_ORCHID: object
    POTTED_ALLIUM: object
    POTTED_AZURE_BLUET: object
    POTTED_RED_TULIP: object
    POTTED_ORANGE_TULIP: object
    POTTED_WHITE_TULIP: object
    POTTED_PINK_TULIP: object
    POTTED_OXEYE_DAISY: object
    POTTED_CORNFLOWER: object
    POTTED_LILY_OF_THE_VALLEY: object
    POTTED_WITHER_ROSE: object
    POTTED_RED_MUSHROOM: object
    POTTED_BROWN_MUSHROOM: object
    POTTED_DEAD_BUSH: object
    POTTED_CACTUS: object
    CARROTS: object
    POTATOES: object
    OAK_BUTTON: object
    SPRUCE_BUTTON: object
    BIRCH_BUTTON: object
    JUNGLE_BUTTON: object
    ACACIA_BUTTON: object
    CHERRY_BUTTON: object
    DARK_OAK_BUTTON: object
    MANGROVE_BUTTON: object
    BAMBOO_BUTTON: object
    SKELETON_SKULL: object
    SKELETON_WALL_SKULL: object
    WITHER_SKELETON_SKULL: object
    WITHER_SKELETON_WALL_SKULL: object
    ZOMBIE_HEAD: object
    ZOMBIE_WALL_HEAD: object
    PLAYER_HEAD: object
    PLAYER_WALL_HEAD: object
    CREEPER_HEAD: object
    CREEPER_WALL_HEAD: object
    DRAGON_HEAD: object
    DRAGON_WALL_HEAD: object
    PIGLIN_HEAD: object
    PIGLIN_WALL_HEAD: object
    ANVIL: object
    CHIPPED_ANVIL: object
    DAMAGED_ANVIL: object
    TRAPPED_CHEST: object
    LIGHT_WEIGHTED_PRESSURE_PLATE: object
    HEAVY_WEIGHTED_PRESSURE_PLATE: object
    COMPARATOR: object
    DAYLIGHT_DETECTOR: object
    REDSTONE_BLOCK: object
    NETHER_QUARTZ_ORE: object
    HOPPER: object
    QUARTZ_BLOCK: object
    CHISELED_QUARTZ_BLOCK: object
    QUARTZ_PILLAR: object
    QUARTZ_STAIRS: object
    ACTIVATOR_RAIL: object
    DROPPER: object
    WHITE_TERRACOTTA: object
    ORANGE_TERRACOTTA: object
    MAGENTA_TERRACOTTA: object
    LIGHT_BLUE_TERRACOTTA: object
    YELLOW_TERRACOTTA: object
    LIME_TERRACOTTA: object
    PINK_TERRACOTTA: object
    GRAY_TERRACOTTA: object
    LIGHT_GRAY_TERRACOTTA: object
    CYAN_TERRACOTTA: object
    PURPLE_TERRACOTTA: object
    BLUE_TERRACOTTA: object
    BROWN_TERRACOTTA: object
    GREEN_TERRACOTTA: object
    RED_TERRACOTTA: object
    BLACK_TERRACOTTA: object
    WHITE_STAINED_GLASS_PANE: object
    ORANGE_STAINED_GLASS_PANE: object
    MAGENTA_STAINED_GLASS_PANE: object
    LIGHT_BLUE_STAINED_GLASS_PANE: object
    YELLOW_STAINED_GLASS_PANE: object
    LIME_STAINED_GLASS_PANE: object
    PINK_STAINED_GLASS_PANE: object
    GRAY_STAINED_GLASS_PANE: object
    LIGHT_GRAY_STAINED_GLASS_PANE: object
    CYAN_STAINED_GLASS_PANE: object
    PURPLE_STAINED_GLASS_PANE: object
    BLUE_STAINED_GLASS_PANE: object
    BROWN_STAINED_GLASS_PANE: object
    GREEN_STAINED_GLASS_PANE: object
    RED_STAINED_GLASS_PANE: object
    BLACK_STAINED_GLASS_PANE: object
    ACACIA_STAIRS: object
    CHERRY_STAIRS: object
    DARK_OAK_STAIRS: object
    MANGROVE_STAIRS: object
    BAMBOO_STAIRS: object
    BAMBOO_MOSAIC_STAIRS: object
    SLIME_BLOCK: object
    BARRIER: object
    LIGHT: object
    IRON_TRAPDOOR: object
    PRISMARINE: object
    PRISMARINE_BRICKS: object
    DARK_PRISMARINE: object
    PRISMARINE_STAIRS: object
    PRISMARINE_BRICK_STAIRS: object
    DARK_PRISMARINE_STAIRS: object
    PRISMARINE_SLAB: object
    PRISMARINE_BRICK_SLAB: object
    DARK_PRISMARINE_SLAB: object
    SEA_LANTERN: object
    HAY_BLOCK: object
    WHITE_CARPET: object
    ORANGE_CARPET: object
    MAGENTA_CARPET: object
    LIGHT_BLUE_CARPET: object
    YELLOW_CARPET: object
    LIME_CARPET: object
    PINK_CARPET: object
    GRAY_CARPET: object
    LIGHT_GRAY_CARPET: object
    CYAN_CARPET: object
    PURPLE_CARPET: object
    BLUE_CARPET: object
    BROWN_CARPET: object
    GREEN_CARPET: object
    RED_CARPET: object
    BLACK_CARPET: object
    TERRACOTTA: object
    COAL_BLOCK: object
    PACKED_ICE: object
    SUNFLOWER: object
    LILAC: object
    ROSE_BUSH: object
    PEONY: object
    TALL_GRASS: object
    LARGE_FERN: object
    WHITE_BANNER: object
    ORANGE_BANNER: object
    MAGENTA_BANNER: object
    LIGHT_BLUE_BANNER: object
    YELLOW_BANNER: object
    LIME_BANNER: object
    PINK_BANNER: object
    GRAY_BANNER: object
    LIGHT_GRAY_BANNER: object
    CYAN_BANNER: object
    PURPLE_BANNER: object
    BLUE_BANNER: object
    BROWN_BANNER: object
    GREEN_BANNER: object
    RED_BANNER: object
    BLACK_BANNER: object
    WHITE_WALL_BANNER: object
    ORANGE_WALL_BANNER: object
    MAGENTA_WALL_BANNER: object
    LIGHT_BLUE_WALL_BANNER: object
    YELLOW_WALL_BANNER: object
    LIME_WALL_BANNER: object
    PINK_WALL_BANNER: object
    GRAY_WALL_BANNER: object
    LIGHT_GRAY_WALL_BANNER: object
    CYAN_WALL_BANNER: object
    PURPLE_WALL_BANNER: object
    BLUE_WALL_BANNER: object
    BROWN_WALL_BANNER: object
    GREEN_WALL_BANNER: object
    RED_WALL_BANNER: object
    BLACK_WALL_BANNER: object
    RED_SANDSTONE: object
    CHISELED_RED_SANDSTONE: object
    CUT_RED_SANDSTONE: object
    RED_SANDSTONE_STAIRS: object
    OAK_SLAB: object
    SPRUCE_SLAB: object
    BIRCH_SLAB: object
    JUNGLE_SLAB: object
    ACACIA_SLAB: object
    CHERRY_SLAB: object
    DARK_OAK_SLAB: object
    MANGROVE_SLAB: object
    BAMBOO_SLAB: object
    BAMBOO_MOSAIC_SLAB: object
    STONE_SLAB: object
    SMOOTH_STONE_SLAB: object
    SANDSTONE_SLAB: object
    CUT_SANDSTONE_SLAB: object
    PETRIFIED_OAK_SLAB: object
    COBBLESTONE_SLAB: object
    BRICK_SLAB: object
    STONE_BRICK_SLAB: object
    MUD_BRICK_SLAB: object
    NETHER_BRICK_SLAB: object
    QUARTZ_SLAB: object
    RED_SANDSTONE_SLAB: object
    CUT_RED_SANDSTONE_SLAB: object
    PURPUR_SLAB: object
    SMOOTH_STONE: object
    SMOOTH_SANDSTONE: object
    SMOOTH_QUARTZ: object
    SMOOTH_RED_SANDSTONE: object
    SPRUCE_FENCE_GATE: object
    BIRCH_FENCE_GATE: object
    JUNGLE_FENCE_GATE: object
    ACACIA_FENCE_GATE: object
    CHERRY_FENCE_GATE: object
    DARK_OAK_FENCE_GATE: object
    MANGROVE_FENCE_GATE: object
    BAMBOO_FENCE_GATE: object
    SPRUCE_FENCE: object
    BIRCH_FENCE: object
    JUNGLE_FENCE: object
    ACACIA_FENCE: object
    CHERRY_FENCE: object
    DARK_OAK_FENCE: object
    MANGROVE_FENCE: object
    BAMBOO_FENCE: object
    SPRUCE_DOOR: object
    BIRCH_DOOR: object
    JUNGLE_DOOR: object
    ACACIA_DOOR: object
    CHERRY_DOOR: object
    DARK_OAK_DOOR: object
    MANGROVE_DOOR: object
    BAMBOO_DOOR: object
    END_ROD: object
    CHORUS_PLANT: object
    CHORUS_FLOWER: object
    PURPUR_BLOCK: object
    PURPUR_PILLAR: object
    PURPUR_STAIRS: object
    END_STONE_BRICKS: object
    TORCHFLOWER_CROP: object
    PITCHER_CROP: object
    PITCHER_PLANT: object
    BEETROOTS: object
    DIRT_PATH: object
    END_GATEWAY: object
    REPEATING_COMMAND_BLOCK: object
    CHAIN_COMMAND_BLOCK: object
    FROSTED_ICE: object
    MAGMA_BLOCK: object
    NETHER_WART_BLOCK: object
    RED_NETHER_BRICKS: object
    BONE_BLOCK: object
    STRUCTURE_VOID: object
    OBSERVER: object
    SHULKER_BOX: object
    WHITE_SHULKER_BOX: object
    ORANGE_SHULKER_BOX: object
    MAGENTA_SHULKER_BOX: object
    LIGHT_BLUE_SHULKER_BOX: object
    YELLOW_SHULKER_BOX: object
    LIME_SHULKER_BOX: object
    PINK_SHULKER_BOX: object
    GRAY_SHULKER_BOX: object
    LIGHT_GRAY_SHULKER_BOX: object
    CYAN_SHULKER_BOX: object
    PURPLE_SHULKER_BOX: object
    BLUE_SHULKER_BOX: object
    BROWN_SHULKER_BOX: object
    GREEN_SHULKER_BOX: object
    RED_SHULKER_BOX: object
    BLACK_SHULKER_BOX: object
    WHITE_GLAZED_TERRACOTTA: object
    ORANGE_GLAZED_TERRACOTTA: object
    MAGENTA_GLAZED_TERRACOTTA: object
    LIGHT_BLUE_GLAZED_TERRACOTTA: object
    YELLOW_GLAZED_TERRACOTTA: object
    LIME_GLAZED_TERRACOTTA: object
    PINK_GLAZED_TERRACOTTA: object
    GRAY_GLAZED_TERRACOTTA: object
    LIGHT_GRAY_GLAZED_TERRACOTTA: object
    CYAN_GLAZED_TERRACOTTA: object
    PURPLE_GLAZED_TERRACOTTA: object
    BLUE_GLAZED_TERRACOTTA: object
    BROWN_GLAZED_TERRACOTTA: object
    GREEN_GLAZED_TERRACOTTA: object
    RED_GLAZED_TERRACOTTA: object
    BLACK_GLAZED_TERRACOTTA: object
    WHITE_CONCRETE: object
    ORANGE_CONCRETE: object
    MAGENTA_CONCRETE: object
    LIGHT_BLUE_CONCRETE: object
    YELLOW_CONCRETE: object
    LIME_CONCRETE: object
    PINK_CONCRETE: object
    GRAY_CONCRETE: object
    LIGHT_GRAY_CONCRETE: object
    CYAN_CONCRETE: object
    PURPLE_CONCRETE: object
    BLUE_CONCRETE: object
    BROWN_CONCRETE: object
    GREEN_CONCRETE: object
    RED_CONCRETE: object
    BLACK_CONCRETE: object
    WHITE_CONCRETE_POWDER: object
    ORANGE_CONCRETE_POWDER: object
    MAGENTA_CONCRETE_POWDER: object
    LIGHT_BLUE_CONCRETE_POWDER: object
    YELLOW_CONCRETE_POWDER: object
    LIME_CONCRETE_POWDER: object
    PINK_CONCRETE_POWDER: object
    GRAY_CONCRETE_POWDER: object
    LIGHT_GRAY_CONCRETE_POWDER: object
    CYAN_CONCRETE_POWDER: object
    PURPLE_CONCRETE_POWDER: object
    BLUE_CONCRETE_POWDER: object
    BROWN_CONCRETE_POWDER: object
    GREEN_CONCRETE_POWDER: object
    RED_CONCRETE_POWDER: object
    BLACK_CONCRETE_POWDER: object
    KELP: object
    KELP_PLANT: object
    DRIED_KELP_BLOCK: object
    TURTLE_EGG: object
    SNIFFER_EGG: object
    DEAD_TUBE_CORAL_BLOCK: object
    DEAD_BRAIN_CORAL_BLOCK: object
    DEAD_BUBBLE_CORAL_BLOCK: object
    DEAD_FIRE_CORAL_BLOCK: object
    DEAD_HORN_CORAL_BLOCK: object
    TUBE_CORAL_BLOCK: object
    BRAIN_CORAL_BLOCK: object
    BUBBLE_CORAL_BLOCK: object
    FIRE_CORAL_BLOCK: object
    HORN_CORAL_BLOCK: object
    DEAD_TUBE_CORAL: object
    DEAD_BRAIN_CORAL: object
    DEAD_BUBBLE_CORAL: object
    DEAD_FIRE_CORAL: object
    DEAD_HORN_CORAL: object
    TUBE_CORAL: object
    BRAIN_CORAL: object
    BUBBLE_CORAL: object
    FIRE_CORAL: object
    HORN_CORAL: object
    DEAD_TUBE_CORAL_FAN: object
    DEAD_BRAIN_CORAL_FAN: object
    DEAD_BUBBLE_CORAL_FAN: object
    DEAD_FIRE_CORAL_FAN: object
    DEAD_HORN_CORAL_FAN: object
    TUBE_CORAL_FAN: object
    BRAIN_CORAL_FAN: object
    BUBBLE_CORAL_FAN: object
    FIRE_CORAL_FAN: object
    HORN_CORAL_FAN: object
    DEAD_TUBE_CORAL_WALL_FAN: object
    DEAD_BRAIN_CORAL_WALL_FAN: object
    DEAD_BUBBLE_CORAL_WALL_FAN: object
    DEAD_FIRE_CORAL_WALL_FAN: object
    DEAD_HORN_CORAL_WALL_FAN: object
    TUBE_CORAL_WALL_FAN: object
    BRAIN_CORAL_WALL_FAN: object
    BUBBLE_CORAL_WALL_FAN: object
    FIRE_CORAL_WALL_FAN: object
    HORN_CORAL_WALL_FAN: object
    SEA_PICKLE: object
    BLUE_ICE: object
    CONDUIT: object
    BAMBOO_SAPLING: object
    BAMBOO: object
    POTTED_BAMBOO: object
    VOID_AIR: object
    CAVE_AIR: object
    BUBBLE_COLUMN: object
    POLISHED_GRANITE_STAIRS: object
    SMOOTH_RED_SANDSTONE_STAIRS: object
    MOSSY_STONE_BRICK_STAIRS: object
    POLISHED_DIORITE_STAIRS: object
    MOSSY_COBBLESTONE_STAIRS: object
    END_STONE_BRICK_STAIRS: object
    STONE_STAIRS: object
    SMOOTH_SANDSTONE_STAIRS: object
    SMOOTH_QUARTZ_STAIRS: object
    GRANITE_STAIRS: object
    ANDESITE_STAIRS: object
    RED_NETHER_BRICK_STAIRS: object
    POLISHED_ANDESITE_STAIRS: object
    DIORITE_STAIRS: object
    POLISHED_GRANITE_SLAB: object
    SMOOTH_RED_SANDSTONE_SLAB: object
    MOSSY_STONE_BRICK_SLAB: object
    POLISHED_DIORITE_SLAB: object
    MOSSY_COBBLESTONE_SLAB: object
    END_STONE_BRICK_SLAB: object
    SMOOTH_SANDSTONE_SLAB: object
    SMOOTH_QUARTZ_SLAB: object
    GRANITE_SLAB: object
    ANDESITE_SLAB: object
    RED_NETHER_BRICK_SLAB: object
    POLISHED_ANDESITE_SLAB: object
    DIORITE_SLAB: object
    BRICK_WALL: object
    PRISMARINE_WALL: object
    RED_SANDSTONE_WALL: object
    MOSSY_STONE_BRICK_WALL: object
    GRANITE_WALL: object
    STONE_BRICK_WALL: object
    MUD_BRICK_WALL: object
    NETHER_BRICK_WALL: object
    ANDESITE_WALL: object
    RED_NETHER_BRICK_WALL: object
    SANDSTONE_WALL: object
    END_STONE_BRICK_WALL: object
    DIORITE_WALL: object
    SCAFFOLDING: object
    LOOM: object
    BARREL: object
    SMOKER: object
    BLAST_FURNACE: object
    CARTOGRAPHY_TABLE: object
    FLETCHING_TABLE: object
    GRINDSTONE: object
    LECTERN: object
    SMITHING_TABLE: object
    STONECUTTER: object
    BELL: object
    LANTERN: object
    SOUL_LANTERN: object
    CAMPFIRE: object
    SOUL_CAMPFIRE: object
    SWEET_BERRY_BUSH: object
    WARPED_STEM: object
    STRIPPED_WARPED_STEM: object
    WARPED_HYPHAE: object
    STRIPPED_WARPED_HYPHAE: object
    WARPED_NYLIUM: object
    WARPED_FUNGUS: object
    WARPED_WART_BLOCK: object
    WARPED_ROOTS: object
    NETHER_SPROUTS: object
    CRIMSON_STEM: object
    STRIPPED_CRIMSON_STEM: object
    CRIMSON_HYPHAE: object
    STRIPPED_CRIMSON_HYPHAE: object
    CRIMSON_NYLIUM: object
    CRIMSON_FUNGUS: object
    SHROOMLIGHT: object
    WEEPING_VINES: object
    WEEPING_VINES_PLANT: object
    TWISTING_VINES: object
    TWISTING_VINES_PLANT: object
    CRIMSON_ROOTS: object
    CRIMSON_PLANKS: object
    WARPED_PLANKS: object
    CRIMSON_SLAB: object
    WARPED_SLAB: object
    CRIMSON_PRESSURE_PLATE: object
    WARPED_PRESSURE_PLATE: object
    CRIMSON_FENCE: object
    WARPED_FENCE: object
    CRIMSON_TRAPDOOR: object
    WARPED_TRAPDOOR: object
    CRIMSON_FENCE_GATE: object
    WARPED_FENCE_GATE: object
    CRIMSON_STAIRS: object
    WARPED_STAIRS: object
    CRIMSON_BUTTON: object
    WARPED_BUTTON: object
    CRIMSON_DOOR: object
    WARPED_DOOR: object
    CRIMSON_SIGN: object
    WARPED_SIGN: object
    CRIMSON_WALL_SIGN: object
    WARPED_WALL_SIGN: object
    STRUCTURE_BLOCK: object
    JIGSAW: object
    COMPOSTER: object
    TARGET: object
    BEE_NEST: object
    BEEHIVE: object
    HONEY_BLOCK: object
    HONEYCOMB_BLOCK: object
    NETHERITE_BLOCK: object
    ANCIENT_DEBRIS: object
    CRYING_OBSIDIAN: object
    RESPAWN_ANCHOR: object
    POTTED_CRIMSON_FUNGUS: object
    POTTED_WARPED_FUNGUS: object
    POTTED_CRIMSON_ROOTS: object
    POTTED_WARPED_ROOTS: object
    LODESTONE: object
    BLACKSTONE: object
    BLACKSTONE_STAIRS: object
    BLACKSTONE_WALL: object
    BLACKSTONE_SLAB: object
    POLISHED_BLACKSTONE: object
    POLISHED_BLACKSTONE_BRICKS: object
    CRACKED_POLISHED_BLACKSTONE_BRICKS: object
    CHISELED_POLISHED_BLACKSTONE: object
    POLISHED_BLACKSTONE_BRICK_SLAB: object
    POLISHED_BLACKSTONE_BRICK_STAIRS: object
    POLISHED_BLACKSTONE_BRICK_WALL: object
    GILDED_BLACKSTONE: object
    POLISHED_BLACKSTONE_STAIRS: object
    POLISHED_BLACKSTONE_SLAB: object
    POLISHED_BLACKSTONE_PRESSURE_PLATE: object
    POLISHED_BLACKSTONE_BUTTON: object
    POLISHED_BLACKSTONE_WALL: object
    CHISELED_NETHER_BRICKS: object
    CRACKED_NETHER_BRICKS: object
    QUARTZ_BRICKS: object
    CANDLE: object
    WHITE_CANDLE: object
    ORANGE_CANDLE: object
    MAGENTA_CANDLE: object
    LIGHT_BLUE_CANDLE: object
    YELLOW_CANDLE: object
    LIME_CANDLE: object
    PINK_CANDLE: object
    GRAY_CANDLE: object
    LIGHT_GRAY_CANDLE: object
    CYAN_CANDLE: object
    PURPLE_CANDLE: object
    BLUE_CANDLE: object
    BROWN_CANDLE: object
    GREEN_CANDLE: object
    RED_CANDLE: object
    BLACK_CANDLE: object
    CANDLE_CAKE: object
    WHITE_CANDLE_CAKE: object
    ORANGE_CANDLE_CAKE: object
    MAGENTA_CANDLE_CAKE: object
    LIGHT_BLUE_CANDLE_CAKE: object
    YELLOW_CANDLE_CAKE: object
    LIME_CANDLE_CAKE: object
    PINK_CANDLE_CAKE: object
    GRAY_CANDLE_CAKE: object
    LIGHT_GRAY_CANDLE_CAKE: object
    CYAN_CANDLE_CAKE: object
    PURPLE_CANDLE_CAKE: object
    BLUE_CANDLE_CAKE: object
    BROWN_CANDLE_CAKE: object
    GREEN_CANDLE_CAKE: object
    RED_CANDLE_CAKE: object
    BLACK_CANDLE_CAKE: object
    AMETHYST_BLOCK: object
    BUDDING_AMETHYST: object
    AMETHYST_CLUSTER: object
    LARGE_AMETHYST_BUD: object
    MEDIUM_AMETHYST_BUD: object
    SMALL_AMETHYST_BUD: object
    TUFF: object
    CALCITE: object
    TINTED_GLASS: object
    POWDER_SNOW: object
    SCULK_SENSOR: object
    CALIBRATED_SCULK_SENSOR: object
    SCULK: object
    SCULK_VEIN: object
    SCULK_CATALYST: object
    SCULK_SHRIEKER: object
    OXIDIZED_COPPER: object
    WEATHERED_COPPER: object
    EXPOSED_COPPER: object
    COPPER_BLOCK: object
    COPPER_ORE: object
    DEEPSLATE_COPPER_ORE: object
    OXIDIZED_CUT_COPPER: object
    WEATHERED_CUT_COPPER: object
    EXPOSED_CUT_COPPER: object
    CUT_COPPER: object
    OXIDIZED_CUT_COPPER_STAIRS: object
    WEATHERED_CUT_COPPER_STAIRS: object
    EXPOSED_CUT_COPPER_STAIRS: object
    CUT_COPPER_STAIRS: object
    OXIDIZED_CUT_COPPER_SLAB: object
    WEATHERED_CUT_COPPER_SLAB: object
    EXPOSED_CUT_COPPER_SLAB: object
    CUT_COPPER_SLAB: object
    WAXED_COPPER_BLOCK: object
    WAXED_WEATHERED_COPPER: object
    WAXED_EXPOSED_COPPER: object
    WAXED_OXIDIZED_COPPER: object
    WAXED_OXIDIZED_CUT_COPPER: object
    WAXED_WEATHERED_CUT_COPPER: object
    WAXED_EXPOSED_CUT_COPPER: object
    WAXED_CUT_COPPER: object
    WAXED_OXIDIZED_CUT_COPPER_STAIRS: object
    WAXED_WEATHERED_CUT_COPPER_STAIRS: object
    WAXED_EXPOSED_CUT_COPPER_STAIRS: object
    WAXED_CUT_COPPER_STAIRS: object
    WAXED_OXIDIZED_CUT_COPPER_SLAB: object
    WAXED_WEATHERED_CUT_COPPER_SLAB: object
    WAXED_EXPOSED_CUT_COPPER_SLAB: object
    WAXED_CUT_COPPER_SLAB: object
    LIGHTNING_ROD: object
    POINTED_DRIPSTONE: object
    DRIPSTONE_BLOCK: object
    CAVE_VINES: object
    CAVE_VINES_PLANT: object
    SPORE_BLOSSOM: object
    AZALEA: object
    FLOWERING_AZALEA: object
    MOSS_CARPET: object
    PINK_PETALS: object
    MOSS_BLOCK: object
    BIG_DRIPLEAF: object
    BIG_DRIPLEAF_STEM: object
    SMALL_DRIPLEAF: object
    HANGING_ROOTS: object
    ROOTED_DIRT: object
    MUD: object
    DEEPSLATE: object
    COBBLED_DEEPSLATE: object
    COBBLED_DEEPSLATE_STAIRS: object
    COBBLED_DEEPSLATE_SLAB: object
    COBBLED_DEEPSLATE_WALL: object
    POLISHED_DEEPSLATE: object
    POLISHED_DEEPSLATE_STAIRS: object
    POLISHED_DEEPSLATE_SLAB: object
    POLISHED_DEEPSLATE_WALL: object
    DEEPSLATE_TILES: object
    DEEPSLATE_TILE_STAIRS: object
    DEEPSLATE_TILE_SLAB: object
    DEEPSLATE_TILE_WALL: object
    DEEPSLATE_BRICKS: object
    DEEPSLATE_BRICK_STAIRS: object
    DEEPSLATE_BRICK_SLAB: object
    DEEPSLATE_BRICK_WALL: object
    CHISELED_DEEPSLATE: object
    CRACKED_DEEPSLATE_BRICKS: object
    CRACKED_DEEPSLATE_TILES: object
    INFESTED_DEEPSLATE: object
    SMOOTH_BASALT: object
    RAW_IRON_BLOCK: object
    RAW_COPPER_BLOCK: object
    RAW_GOLD_BLOCK: object
    POTTED_AZALEA_BUSH: object
    POTTED_FLOWERING_AZALEA_BUSH: object
    OCHRE_FROGLIGHT: object
    VERDANT_FROGLIGHT: object
    PEARLESCENT_FROGLIGHT: object
    FROGSPAWN: object
    REINFORCED_DEEPSLATE: object
    DECORATED_POT: object

class BlockState:
    """
    The BlockState class represents the state of a block in Minecraft.

    Attributes:
        block (Block): The block associated with this state.
    """

    block: Block

    def __init__(self, block: Blocks) -> None: ...
    @staticmethod
    def isOf(block: Block) -> bool: ...

class CollisionRules:
    """
    The CollisionRules class represents the collision rules for entities in Minecraft.
    """

    ALWAYS: object
    NEVER: object
    PUSH_OTHER_TEAMS: object
    PUSH_OWN_TEAM: object

class DamageSources:
    """
    The DamageSources class represents the various sources of damage in Minecraft.
    """

    IN_FIRE: object
    LIGHTNING_BOLT: object
    ON_FIRE: object
    LAVA: object
    HOT_FLOOR: object
    IN_WALL: object
    CRAMMING: object
    DROWN: object
    STARVE: object
    CACTUS: object
    FALL: object
    FLY_INTO_WALL: object
    OUT_OF_WORLD: object
    GENERIC: object
    MAGIC: object
    WITHER: object
    DRAGON_BREATH: object
    DRY_OUT: object
    SWEET_BERRY_BUSH: object
    FREEZE: object
    STALAGMITE: object
    OUTSIDE_BORDER: object
    GENERIC_KILL: object

class Difficulties:
    """
    The Difficulties class represents the difficulty levels in Minecraft.
    """

    EASY: object
    HARD: object
    NORMAL: object
    PEACEFUL: object

class Difficulty:
    """
    The Difficulty class represents a difficulty level in Minecraft.

    Attributes:
        name (str): The name of the difficulty level.
        id (int): The unique identifier of the difficulty level.
        info (str): Additional information or description about the difficulty level.
    """

    name: str
    id: int
    info: str

class Enchantment:
    """
    The Enchantment class represents an enchantment applied to an item in Minecraft.

    Attributes:
        level (int): The level or magnitude of the enchantment.
        rarity (EnchantmentRarity): The rarity level of the enchantment.
    """

    level: int
    rarity: EnchantmentRarity

class EnchantmentRarity:
    """
    The EnchantmentRarity class represents the rarity levels of enchantments in Minecraft.
    """

    COMMON: object
    UNCOMMON: object
    RARE: object
    VERY_RARE: object

class Enchantments:
    """
    The Enchantments class represents a collection of available enchantments in Minecraft.
    """

    PROTECTION: object
    FIRE_PROTECTION: object
    FEATHER_FALLING: object
    BLAST_PROTECTION: object
    PROJECTILE_PROTECTION: object
    RESPIRATION: object
    AQUA_AFFINITY: object
    THORNS: object
    DEPTH_STRIDER: object
    FROST_WALKER: object
    BINDING_CURSE: object
    SOUL_SPEED: object
    SWIFT_SNEAK: object
    SHARPNESS: object
    SMITE: object
    BANE_OF_ARTHROPODS: object
    KNOCKBACK: object
    FIRE_ASPECT: object
    LOOTING: object
    SWEEPING: object
    EFFICIENCY: object
    SILK_TOUCH: object
    UNBREAKING: object
    FORTUNE: object
    POWER: object
    PUNCH: object
    FLAME: object
    INFINITY: object
    LUCK_OF_THE_SEA: object
    LURE: object
    LOYALTY: object
    IMPALING: object
    RIPTIDE: object
    CHANNELING: object
    MULTISHOT: object
    QUICK_CHARGE: object
    PIERCING: object
    MENDING: object
    VANISHING_CURSE: object

class EnderChestInventory:
    """
    The EnderChestInventory class represents the inventory of an Ender Chest in Minecraft.

    Attributes:
        stacks (list[ItemStack]): A list of ItemStack objects representing the items stored in the Ender Chest.
    """

    stacks: list[ItemStack]

class Entities:
    """
    The Entities class represents different types of entities in Minecraft.
    """

    ALLAY: object
    AREA_EFFECT_CLOUD: object
    ARMOR_STAND: object
    ARROW: object
    AXOLOTL: object
    BAT: object
    BEE: object
    BLAZE: object
    BLOCK_DISPLAY: object
    BOAT: object
    CAMEL: object
    CAT: object
    CAVE_SPIDER: object
    CHEST_BOAT: object
    CHEST_MINECART: object
    CHICKEN: object
    COD: object
    COMMAND_BLOCK_MINECART: object
    COW: object
    CREEPER: object
    DOLPHIN: object
    DONKEY: object
    DRAGON_FIREBALL: object
    DROWNED: object
    EGG: object
    ELDER_GUARDIAN: object
    END_CRYSTAL: object
    ENDER_DRAGON: object
    ENDER_PEARL: object
    ENDERMAN: object
    ENDERMITE: object
    EVOKER: object
    EVOKER_FANGS: object
    EXPERIENCE_BOTTLE: object
    EXPERIENCE_ORB: object
    EYE_OF_ENDER: object
    FALLING_BLOCK: object
    FIREWORK_ROCKET: object
    FOX: object
    FROG: object
    FURNACE_MINECART: object
    GHAST: object
    GIANT: object
    GLOW_ITEM_FRAME: object
    GLOW_SQUID: object
    GOAT: object
    GUARDIAN: object
    HOGLIN: object
    HOPPER_MINECART: object
    HORSE: object
    HUSK: object
    ILLUSIONER: object
    INTERACTION: object
    IRON_GOLEM: object
    ITEM: object
    ITEM_DISPLAY: object
    ITEM_FRAME: object
    FIREBALL: object
    LEASH_KNOT: object
    LIGHTNING_BOLT: object
    LLAMA: object
    LLAMA_SPIT: object
    MAGMA_CUBE: object
    MARKER: object
    MINECART: object
    MOOSHROOM: object
    MULE: object
    OCELOT: object
    PAINTING: object
    PANDA: object
    PARROT: object
    PHANTOM: object
    PIG: object
    PIGLIN: object
    PIGLIN_BRUTE: object
    PILLAGER: object
    POLAR_BEAR: object
    POTION: object
    PUFFERFISH: object
    RABBIT: object
    RAVAGER: object
    SALMON: object
    SHEEP: object
    SHULKER: object
    SHULKER_BULLET: object
    SILVERFISH: object
    SKELETON: object
    SKELETON_HORSE: object
    SLIME: object
    SMALL_FIREBALL: object
    SNIFFER: object
    SNOW_GOLEM: object
    SNOWBALL: object
    SPAWNER_MINECART: object
    SPECTRAL_ARROW: object
    SPIDER: object
    SQUID: object
    STRAY: object
    STRIDER: object
    TADPOLE: object
    TEXT_DISPLAY: object
    TNT: object
    TNT_MINECART: object
    TRADER_LLAMA: object
    TRIDENT: object
    TROPICAL_FISH: object
    TURTLE: object
    VEX: object
    VILLAGER: object
    VINDICATOR: object
    WANDERING_TRADER: object
    WARDEN: object
    WITCH: object
    WITHER: object
    WITHER_SKELETON: object
    WITHER_SKULL: object
    WOLF: object
    ZOGLIN: object
    ZOMBIE: object
    ZOMBIE_HORSE: object
    ZOMBIE_VILLAGER: object
    ZOMBIFIED_PIGLIN: object
    PLAYER: object
    FISHING_BOBBER: object

class Entity:
    def __init__(self, entity: Entities, world: World) -> None:
        """
        Initializes a new entity with the specified entity type and world.

        Args:
            entity: The type of entity.
            world: The world the entity belongs to.
        """
    def addVelocity(self, velocity: Vec3d) -> None:
        """
        Adds velocity to the entity.

        Args:
            velocity: The velocity to add to the entity.
        """
    def canFreeze(self) -> bool:
        """
        Checks if the entity can freeze.

        Returns:
            True if the entity can freeze, False otherwise.
        """
    def canUsePortals(self) -> bool:
        """
        Checks if the entity can use portals.

        Returns:
            True if the entity can use portals, False otherwise.
        """
    def collidesWith(self, entity: Entity) -> bool:
        """
        Checks if the entity collides with another entity.

        Args:
            entity: The entity to check collision with.

        Returns:
            True if the entity collides with the specified entity, False otherwise.
        """
    def damage(self, damageSource: DamageSources, amount: Number) -> None:
        """
        Damages the entity by the specified amount using the given damage source.

        Args:
            damageSource: The source of the damage.
            amount: The amount of damage to inflict.
        """
    def dismountVehicle(self) -> None:
        """
        Dismounts the entity from its current vehicle.
        """
    def distanceTo(self, entity: Entity) -> float:
        """
        Calculates the distance to another entity.

        Args:
            entity: The entity to calculate the distance to.

        Returns:
            The distance to the specified entity.
        """
    def extinguish(self) -> None:
        """
        Extinguishes the entity.
        """
    def extinguishWithSound(self) -> None:
        """
        Extinguishes the entity with a sound effect.
        """
    def getArmorItems(self) -> list[ItemStack]:
        """
        Returns a list of armor items worn by the entity.

        Returns:
            A list of ItemStack objects representing the armor items.
        """
    def getBlockPos(self) -> BlockPos:
        """
        Returns the block position of the entity.

        Returns:
            The BlockPos object representing the block position.
        """
    def getCommandTags(self) -> list[str]:
        """
        Returns a list of command tags associated with the entity.

        Returns:
            A list of strings representing the command tags.
        """
    def getCustomName(self) -> str:
        """
        Returns the custom name of the entity.

        Returns:
            The custom name of the entity as a string.
        """
    def getDisplayName(self) -> str:
        """
        Returns the display name of the entity.

        Returns:
            The display name of the entity as a string.
        """
    def getHandItems(self) -> list[ItemStack]:
        """
        Returns a list of items held in the entity's hands.

        Returns:
            A list of ItemStack objects representing the held items.
        """
    def getName(self) -> str:
        """
        Returns the name of the entity.

        Returns:
            The name of the entity as a string.
        """
    def getPosition(self) -> Vec3d:
        """
        Returns the position of the entity.

        Returns:
            The position of the entity as a Vec3d object.
        """
    def getVehicle(self) -> Entity:
        """
        Returns the vehicle that the entity is riding.

        Returns:
            The vehicle entity that the entity is riding, or None if not riding any vehicle.
        """
    def getVelocity(self) -> Vec3d:
        """
        Returns the velocity of the entity.

        Returns:
            The velocity of the entity as a Vec3d object.
        """
    def getX(self) -> float:
        """
        Returns the X-coordinate of the entity's position.

        Returns:
            The X-coordinate of the entity's position as a float.
        """
    def getY(self) -> float:
        """
        Returns the Y-coordinate of the entity's position.

        Returns:
            The Y-coordinate of the entity's position as a float.
        """
    def getZ(self) -> float:
        """
        Returns the Z-coordinate of the entity's position.

        Returns:
            The Z-coordinate of the entity's position as a float.
        """
    def hasCustomName(self) -> bool:
        """
        Checks if the entity has a custom name.

        Returns:
            True if the entity has a custom name, False otherwise.
        """
    def hasNoGravity(self) -> bool:
        """
        Checks if the entity has no gravity.

        Returns:
            True if the entity has no gravity, False otherwise.
        """
    def hasPassenger(self, entity: Entity) -> bool:
        """
        Checks if the entity has the specified entity as a passenger.

        Args:
            entity: The entity to check for as a passenger.

        Returns:
            True if the entity has the specified entity as a passenger, False otherwise.
        """
    def hasPassengers(self) -> bool:
        """
        Checks if the entity has any passengers.

        Returns:
            True if the entity has passengers, False otherwise.
        """
    def hasPermissionLevel(self, level: Number) -> bool:
        """
        Checks if the entity has the specified permission level.

        Args:
            level: The permission level to check.

        Returns:
            True if the entity has the specified permission level, False otherwise.
        """
    def hasPortalCooldown(self) -> bool:
        """
        Checks if the entity has a portal cooldown.

        Returns:
            True if the entity has a portal cooldown, False otherwise.
        """
    def hasVehicle(self) -> bool:
        """
        Checks if the entity is riding a vehicle.

        Returns:
            True if the entity is riding a vehicle, False otherwise.
        """
    def isAlive(self) -> bool:
        """
        Checks if the entity is alive.

        Returns:
            True if the entity is alive, False otherwise.
        """
    def isCollidable(self) -> bool:
        """
        Checks if the entity is collidable.

        Returns:
            True if the entity is collidable, False otherwise.
        """
    def isCrawling(self) -> bool:
        """
        Checks if the entity is crawling.

        Returns:
            True if the entity is crawling, False otherwise.
        """
    def isCustomNameVisible(self) -> bool:
        """
        Checks if the entity's custom name is visible.

        Returns:
            True if the entity's custom name is visible, False otherwise.
        """
    def isDead(self) -> bool:
        """
        Checks if the entity is dead.

        Returns:
            True if the entity is dead, False otherwise.
        """
    def isInLava(self) -> bool:
        """
        Checks if the entity is in lava.

        Returns:
            True if the entity is in lava, False otherwise.
        """
    def isInRain(self) -> bool:
        """
        Checks if the entity is in rain.

        Returns:
            True if the entity is in rain, False otherwise.
        """
    def isInsidePortal(self) -> bool:
        """
        Checks if the entity is inside a portal.

        Returns:
            True if the entity is inside a portal, False otherwise.
        """
    def isInsideWater(self) -> bool:
        """
        Checks if the entity is inside water.

        Returns:
            True if the entity is inside water, False otherwise.
        """
    def isOnGround(self) -> bool:
        """
        Checks if the entity is on the ground.

        Returns:
            True if the entity is on the ground, False otherwise.
        """
    def isSpectator(self) -> bool:
        """
        Checks if the entity is a spectator.

        Returns:
            True if the entity is a spectator, False otherwise.
        """
    def isSubmergedInWater(self) -> bool:
        """
        Checks if the entity is submerged in water.

        Returns:
            True if the entity is submerged in water, False otherwise.
        """
    def isVisible(self) -> bool:
        """
        Checks if the entity is visible.

        Returns:
            True if the entity is visible, False otherwise.
        """
    def lookAt(self, x: float, y: float, z: float) -> None:
        """
        Sets the entity's rotation to face the specified position.

        Args:
            x: The X-coordinate of the target position.
            y: The Y-coordinate of the target position.
            z: The Z-coordinate of the target position.
        """
    def removeAllPassengers(self) -> None:
        """
        Removes all passengers from the entity.
        """
    def removePassenger(self, entity: Entity) -> None:
        """
        Removes the specified entity from the entity's passengers.

        Args:
            entity: The entity to remove as a passenger.
        """
    def removePermissionLevel(self, level: Number) -> None:
        """
        Removes the specified permission level from the entity.

        Args:
            level: The permission level to remove.
        """
    def ride(self, entity: Entity) -> None:
        """
        Rides the specified entity.

        Args:
            entity: The entity to ride.
        """
    def setPosition(self, x: float, y: float, z: float) -> None:
        """
        Sets the position of the entity.

        Args:
            x: The X-coordinate of the new position.
            y: The Y-coordinate of the new position.
            z: The Z-coordinate of the new position.
        """
    def setCustomName(self, customName: str) -> None:
        """
        Sets the custom name of the entity using a string.

        Args:
            customName: The custom name to set.
        """
    def setCustomNameVisible(self, visible: bool) -> None:
        """
        Sets whether the custom name of the entity is visible.

        Args:
            visible: True to make the custom name visible, False to hide it.
        """
    def setGlowing(self, glowing: bool) -> None:
        """
        Sets whether the entity is glowing.

        Args:
            glowing: True to make the entity glow, False otherwise.
        """
    def setInvisible(self, invisible: bool) -> None:
        """
        Sets whether the entity is invisible.

        Args:
            invisible: True to make the entity invisible, False otherwise.
        """
    def setInvulnerable(self, invulnerable: bool) -> None:
        """
        Sets whether the entity is invulnerable.

        Args:
            invulnerable: True to make the entity invulnerable, False otherwise.
        """
    def setMotion(self, motion: Vec3d) -> None:
        """
        Sets the motion of the entity.

        Args:
            motion: The new motion to set for the entity.
        """
    def setNoGravity(self, noGravity: bool) -> None:
        """
        Sets whether the entity has gravity.

        Args:
            noGravity: True to disable gravity for the entity, False otherwise.
        """
    def setSilent(self, silent: bool) -> None:
        """
        Sets whether the entity is silent.

        Args:
            silent: True to make the entity silent, False otherwise.
        """
    def setSneaking(self, sneaking: bool) -> None:
        """
        Sets whether the entity is sneaking.

        Args:
            sneaking: True to make the entity sneak, False otherwise.
        """
    def setSprinting(self, sprinting: bool) -> None:
        """
        Sets whether the entity is sprinting.

        Args:
            sprinting: True to make the entity sprint, False otherwise.
        """
    def startRiding(self, entity: Entity) -> None:
        """
        Starts riding the specified entity.

        Args:
            entity: The entity to start riding.
        """
    def stopRiding(self) -> None:
        """
        Stops riding any entity the entity is currently riding.
        """
    def teleport(self, position: Vec3d) -> None:
        """
        Teleports the entity to the specified position.

        Args:
            position: The position to teleport the entity to.
        """

class Executor:
    """
    Attributes:
        name (str): The name of the executor.
        displayName (str): The display name of the executor.
        position (Vec3d): The position of the executor.
        player (PlayerEntity): The player entity associated with the executor.
        world (World): The world in which the executor exists.
        entity (Entity): The entity associated with the executor.
        isExecutedByPlayer (bool): Indicates if the executor is executed by a player.
        rotation (Vec2f): The rotation of the executor.
    """

    name: str
    displayName: str
    position: Vec3d
    player: PlayerEntity
    world: World
    entity: Entity
    isExecutedByPlayer: bool
    rotation: Vec2f

    def sendMessage(self, message) -> None:
        """
        Sends a message to the executor.

        Args:
            message: The message to send.
        """
    def sendError(self, error) -> None:
        """
        Sends an error message to the executor.

        Args:
            error: The error message to send.
        """
    def sendMessage(self, text: Text) -> None:
        """
        Sends a text message to the executor.

        Args:
            text (Text): The text message to send.
        """
    def sendError(self, text: Text) -> None:
        """
        Sends an error text message to the executor.

        Args:
            text (Text): The error text message to send.
        """

class GameMode:
    """
    Represents Minecraft mode.
    """

    id: int
    name: str
    SURVIVAL: GameMode
    CREATIVE: GameMode
    ADVENTURE: GameMode
    SPECTATOR: GameMode

class GameModes:
    """
    Represents a collection of game modes.
    """

    SURVIVAL: object
    CREATIVE: object
    ADVENTURE: object
    SPECTATOR: object

class Hand:
    """
    Represents the hand used by a player.
    """

    MAIN_HAND: object
    OFF_HAND: object

class HideFlags:
    """
    Represents various hide flags for an item.
    """

    ENCHANTMENTS: object
    MODIFIERS: object
    UNBREAKABLE: object
    CAN_DESTROY: object
    CAN_PLACE: object
    ADDITIONAL: object
    DYE: object
    UPGRADES: object

class HungerManager:
    """
    Represents the hunger manager for a player.

    Attributes:
        exhaustion (float): The exhaustion level of the player.
        foodLevel (int): The current food level of the player.
        saturationLevel (float): The saturation level of the player.
    """

    exhaustion: float
    foodLevel: int
    saturationLevel: float

class Item:
    """
    Represents an item in the game.

    Attributes:
        name (str): The name of the item.
    """

    name: str

    def __init__(self, item: Items) -> None: ...

class ItemRarity:
    """
    Represents the rarity of an item.
    """

    COMMON: object
    UNCOMMON: object
    RARE: object
    EPIC: object

class Items:
    """
    Represents various items in the game.
    """

    AIR: object
    STONE: object
    GRANITE: object
    POLISHED_GRANITE: object
    DIORITE: object
    POLISHED_DIORITE: object
    ANDESITE: object
    POLISHED_ANDESITE: object
    DEEPSLATE: object
    COBBLED_DEEPSLATE: object
    POLISHED_DEEPSLATE: object
    CALCITE: object
    TUFF: object
    DRIPSTONE_BLOCK: object
    GRASS_BLOCK: object
    DIRT: object
    COARSE_DIRT: object
    PODZOL: object
    ROOTED_DIRT: object
    MUD: object
    CRIMSON_NYLIUM: object
    WARPED_NYLIUM: object
    COBBLESTONE: object
    OAK_PLANKS: object
    SPRUCE_PLANKS: object
    BIRCH_PLANKS: object
    JUNGLE_PLANKS: object
    ACACIA_PLANKS: object
    CHERRY_PLANKS: object
    DARK_OAK_PLANKS: object
    MANGROVE_PLANKS: object
    BAMBOO_PLANKS: object
    CRIMSON_PLANKS: object
    WARPED_PLANKS: object
    BAMBOO_MOSAIC: object
    OAK_SAPLING: object
    SPRUCE_SAPLING: object
    BIRCH_SAPLING: object
    JUNGLE_SAPLING: object
    ACACIA_SAPLING: object
    CHERRY_SAPLING: object
    DARK_OAK_SAPLING: object
    MANGROVE_PROPAGULE: object
    BEDROCK: object
    SAND: object
    SUSPICIOUS_SAND: object
    SUSPICIOUS_GRAVEL: object
    RED_SAND: object
    GRAVEL: object
    COAL_ORE: object
    DEEPSLATE_COAL_ORE: object
    IRON_ORE: object
    DEEPSLATE_IRON_ORE: object
    COPPER_ORE: object
    DEEPSLATE_COPPER_ORE: object
    GOLD_ORE: object
    DEEPSLATE_GOLD_ORE: object
    REDSTONE_ORE: object
    DEEPSLATE_REDSTONE_ORE: object
    EMERALD_ORE: object
    DEEPSLATE_EMERALD_ORE: object
    LAPIS_ORE: object
    DEEPSLATE_LAPIS_ORE: object
    DIAMOND_ORE: object
    DEEPSLATE_DIAMOND_ORE: object
    NETHER_GOLD_ORE: object
    NETHER_QUARTZ_ORE: object
    ANCIENT_DEBRIS: object
    COAL_BLOCK: object
    RAW_IRON_BLOCK: object
    RAW_COPPER_BLOCK: object
    RAW_GOLD_BLOCK: object
    AMETHYST_BLOCK: object
    BUDDING_AMETHYST: object
    IRON_BLOCK: object
    COPPER_BLOCK: object
    GOLD_BLOCK: object
    DIAMOND_BLOCK: object
    NETHERITE_BLOCK: object
    EXPOSED_COPPER: object
    WEATHERED_COPPER: object
    OXIDIZED_COPPER: object
    CUT_COPPER: object
    EXPOSED_CUT_COPPER: object
    WEATHERED_CUT_COPPER: object
    OXIDIZED_CUT_COPPER: object
    CUT_COPPER_STAIRS: object
    EXPOSED_CUT_COPPER_STAIRS: object
    WEATHERED_CUT_COPPER_STAIRS: object
    OXIDIZED_CUT_COPPER_STAIRS: object
    CUT_COPPER_SLAB: object
    EXPOSED_CUT_COPPER_SLAB: object
    WEATHERED_CUT_COPPER_SLAB: object
    OXIDIZED_CUT_COPPER_SLAB: object
    WAXED_COPPER_BLOCK: object
    WAXED_EXPOSED_COPPER: object
    WAXED_WEATHERED_COPPER: object
    WAXED_OXIDIZED_COPPER: object
    WAXED_CUT_COPPER: object
    WAXED_EXPOSED_CUT_COPPER: object
    WAXED_WEATHERED_CUT_COPPER: object
    WAXED_OXIDIZED_CUT_COPPER: object
    WAXED_CUT_COPPER_STAIRS: object
    WAXED_EXPOSED_CUT_COPPER_STAIRS: object
    WAXED_WEATHERED_CUT_COPPER_STAIRS: object
    WAXED_OXIDIZED_CUT_COPPER_STAIRS: object
    WAXED_CUT_COPPER_SLAB: object
    WAXED_EXPOSED_CUT_COPPER_SLAB: object
    WAXED_WEATHERED_CUT_COPPER_SLAB: object
    WAXED_OXIDIZED_CUT_COPPER_SLAB: object
    OAK_LOG: object
    SPRUCE_LOG: object
    BIRCH_LOG: object
    JUNGLE_LOG: object
    ACACIA_LOG: object
    CHERRY_LOG: object
    DARK_OAK_LOG: object
    MANGROVE_LOG: object
    MANGROVE_ROOTS: object
    MUDDY_MANGROVE_ROOTS: object
    CRIMSON_STEM: object
    WARPED_STEM: object
    BAMBOO_BLOCK: object
    STRIPPED_OAK_LOG: object
    STRIPPED_SPRUCE_LOG: object
    STRIPPED_BIRCH_LOG: object
    STRIPPED_JUNGLE_LOG: object
    STRIPPED_ACACIA_LOG: object
    STRIPPED_CHERRY_LOG: object
    STRIPPED_DARK_OAK_LOG: object
    STRIPPED_MANGROVE_LOG: object
    STRIPPED_CRIMSON_STEM: object
    STRIPPED_WARPED_STEM: object
    STRIPPED_OAK_WOOD: object
    STRIPPED_SPRUCE_WOOD: object
    STRIPPED_BIRCH_WOOD: object
    STRIPPED_JUNGLE_WOOD: object
    STRIPPED_ACACIA_WOOD: object
    STRIPPED_CHERRY_WOOD: object
    STRIPPED_DARK_OAK_WOOD: object
    STRIPPED_MANGROVE_WOOD: object
    STRIPPED_CRIMSON_HYPHAE: object
    STRIPPED_WARPED_HYPHAE: object
    STRIPPED_BAMBOO_BLOCK: object
    OAK_WOOD: object
    SPRUCE_WOOD: object
    BIRCH_WOOD: object
    JUNGLE_WOOD: object
    ACACIA_WOOD: object
    CHERRY_WOOD: object
    DARK_OAK_WOOD: object
    MANGROVE_WOOD: object
    CRIMSON_HYPHAE: object
    WARPED_HYPHAE: object
    OAK_LEAVES: object
    SPRUCE_LEAVES: object
    BIRCH_LEAVES: object
    JUNGLE_LEAVES: object
    ACACIA_LEAVES: object
    CHERRY_LEAVES: object
    DARK_OAK_LEAVES: object
    MANGROVE_LEAVES: object
    AZALEA_LEAVES: object
    FLOWERING_AZALEA_LEAVES: object
    SPONGE: object
    WET_SPONGE: object
    GLASS: object
    TINTED_GLASS: object
    LAPIS_BLOCK: object
    SANDSTONE: object
    CHISELED_SANDSTONE: object
    CUT_SANDSTONE: object
    COBWEB: object
    GRASS: object
    FERN: object
    AZALEA: object
    FLOWERING_AZALEA: object
    DEAD_BUSH: object
    SEAGRASS: object
    SEA_PICKLE: object
    WHITE_WOOL: object
    ORANGE_WOOL: object
    MAGENTA_WOOL: object
    LIGHT_BLUE_WOOL: object
    YELLOW_WOOL: object
    LIME_WOOL: object
    PINK_WOOL: object
    GRAY_WOOL: object
    LIGHT_GRAY_WOOL: object
    CYAN_WOOL: object
    PURPLE_WOOL: object
    BLUE_WOOL: object
    BROWN_WOOL: object
    GREEN_WOOL: object
    RED_WOOL: object
    BLACK_WOOL: object
    DANDELION: object
    POPPY: object
    BLUE_ORCHID: object
    ALLIUM: object
    AZURE_BLUET: object
    RED_TULIP: object
    ORANGE_TULIP: object
    WHITE_TULIP: object
    PINK_TULIP: object
    OXEYE_DAISY: object
    CORNFLOWER: object
    LILY_OF_THE_VALLEY: object
    WITHER_ROSE: object
    TORCHFLOWER: object
    PITCHER_PLANT: object
    SPORE_BLOSSOM: object
    BROWN_MUSHROOM: object
    RED_MUSHROOM: object
    CRIMSON_FUNGUS: object
    WARPED_FUNGUS: object
    CRIMSON_ROOTS: object
    WARPED_ROOTS: object
    NETHER_SPROUTS: object
    WEEPING_VINES: object
    TWISTING_VINES: object
    SUGAR_CANE: object
    KELP: object
    MOSS_CARPET: object
    PINK_PETALS: object
    MOSS_BLOCK: object
    HANGING_ROOTS: object
    BIG_DRIPLEAF: object
    SMALL_DRIPLEAF: object
    BAMBOO: object
    OAK_SLAB: object
    SPRUCE_SLAB: object
    BIRCH_SLAB: object
    JUNGLE_SLAB: object
    ACACIA_SLAB: object
    CHERRY_SLAB: object
    DARK_OAK_SLAB: object
    MANGROVE_SLAB: object
    BAMBOO_SLAB: object
    BAMBOO_MOSAIC_SLAB: object
    CRIMSON_SLAB: object
    WARPED_SLAB: object
    STONE_SLAB: object
    SMOOTH_STONE_SLAB: object
    SANDSTONE_SLAB: object
    CUT_SANDSTONE_SLAB: object
    PETRIFIED_OAK_SLAB: object
    COBBLESTONE_SLAB: object
    BRICK_SLAB: object
    STONE_BRICK_SLAB: object
    MUD_BRICK_SLAB: object
    NETHER_BRICK_SLAB: object
    QUARTZ_SLAB: object
    RED_SANDSTONE_SLAB: object
    CUT_RED_SANDSTONE_SLAB: object
    PURPUR_SLAB: object
    PRISMARINE_SLAB: object
    PRISMARINE_BRICK_SLAB: object
    DARK_PRISMARINE_SLAB: object
    SMOOTH_QUARTZ: object
    SMOOTH_RED_SANDSTONE: object
    SMOOTH_SANDSTONE: object
    SMOOTH_STONE: object
    BRICKS: object
    BOOKSHELF: object
    CHISELED_BOOKSHELF: object
    DECORATED_POT: object
    MOSSY_COBBLESTONE: object
    OBSIDIAN: object
    TORCH: object
    END_ROD: object
    CHORUS_PLANT: object
    CHORUS_FLOWER: object
    PURPUR_BLOCK: object
    PURPUR_PILLAR: object
    PURPUR_STAIRS: object
    SPAWNER: object
    CHEST: object
    CRAFTING_TABLE: object
    FARMLAND: object
    FURNACE: object
    LADDER: object
    COBBLESTONE_STAIRS: object
    SNOW: object
    ICE: object
    SNOW_BLOCK: object
    CACTUS: object
    CLAY: object
    JUKEBOX: object
    OAK_FENCE: object
    SPRUCE_FENCE: object
    BIRCH_FENCE: object
    JUNGLE_FENCE: object
    ACACIA_FENCE: object
    CHERRY_FENCE: object
    DARK_OAK_FENCE: object
    MANGROVE_FENCE: object
    BAMBOO_FENCE: object
    CRIMSON_FENCE: object
    WARPED_FENCE: object
    PUMPKIN: object
    CARVED_PUMPKIN: object
    JACK_O_LANTERN: object
    NETHERRACK: object
    SOUL_SAND: object
    SOUL_SOIL: object
    BASALT: object
    POLISHED_BASALT: object
    SMOOTH_BASALT: object
    SOUL_TORCH: object
    GLOWSTONE: object
    INFESTED_STONE: object
    INFESTED_COBBLESTONE: object
    INFESTED_STONE_BRICKS: object
    INFESTED_MOSSY_STONE_BRICKS: object
    INFESTED_CRACKED_STONE_BRICKS: object
    INFESTED_CHISELED_STONE_BRICKS: object
    INFESTED_DEEPSLATE: object
    STONE_BRICKS: object
    MOSSY_STONE_BRICKS: object
    CRACKED_STONE_BRICKS: object
    CHISELED_STONE_BRICKS: object
    PACKED_MUD: object
    MUD_BRICKS: object
    DEEPSLATE_BRICKS: object
    CRACKED_DEEPSLATE_BRICKS: object
    DEEPSLATE_TILES: object
    CRACKED_DEEPSLATE_TILES: object
    CHISELED_DEEPSLATE: object
    REINFORCED_DEEPSLATE: object
    BROWN_MUSHROOM_BLOCK: object
    RED_MUSHROOM_BLOCK: object
    MUSHROOM_STEM: object
    IRON_BARS: object
    CHAIN: object
    GLASS_PANE: object
    MELON: object
    VINE: object
    GLOW_LICHEN: object
    BRICK_STAIRS: object
    STONE_BRICK_STAIRS: object
    MUD_BRICK_STAIRS: object
    MYCELIUM: object
    LILY_PAD: object
    NETHER_BRICKS: object
    CRACKED_NETHER_BRICKS: object
    CHISELED_NETHER_BRICKS: object
    NETHER_BRICK_FENCE: object
    NETHER_BRICK_STAIRS: object
    SCULK: object
    SCULK_VEIN: object
    SCULK_CATALYST: object
    SCULK_SHRIEKER: object
    ENCHANTING_TABLE: object
    END_PORTAL_FRAME: object
    END_STONE: object
    END_STONE_BRICKS: object
    DRAGON_EGG: object
    SANDSTONE_STAIRS: object
    ENDER_CHEST: object
    EMERALD_BLOCK: object
    OAK_STAIRS: object
    SPRUCE_STAIRS: object
    BIRCH_STAIRS: object
    JUNGLE_STAIRS: object
    ACACIA_STAIRS: object
    CHERRY_STAIRS: object
    DARK_OAK_STAIRS: object
    MANGROVE_STAIRS: object
    BAMBOO_STAIRS: object
    BAMBOO_MOSAIC_STAIRS: object
    CRIMSON_STAIRS: object
    WARPED_STAIRS: object
    COMMAND_BLOCK: object
    BEACON: object
    COBBLESTONE_WALL: object
    MOSSY_COBBLESTONE_WALL: object
    BRICK_WALL: object
    PRISMARINE_WALL: object
    RED_SANDSTONE_WALL: object
    MOSSY_STONE_BRICK_WALL: object
    GRANITE_WALL: object
    STONE_BRICK_WALL: object
    MUD_BRICK_WALL: object
    NETHER_BRICK_WALL: object
    ANDESITE_WALL: object
    RED_NETHER_BRICK_WALL: object
    SANDSTONE_WALL: object
    END_STONE_BRICK_WALL: object
    DIORITE_WALL: object
    BLACKSTONE_WALL: object
    POLISHED_BLACKSTONE_WALL: object
    POLISHED_BLACKSTONE_BRICK_WALL: object
    COBBLED_DEEPSLATE_WALL: object
    POLISHED_DEEPSLATE_WALL: object
    DEEPSLATE_BRICK_WALL: object
    DEEPSLATE_TILE_WALL: object
    ANVIL: object
    CHIPPED_ANVIL: object
    DAMAGED_ANVIL: object
    CHISELED_QUARTZ_BLOCK: object
    QUARTZ_BLOCK: object
    QUARTZ_BRICKS: object
    QUARTZ_PILLAR: object
    QUARTZ_STAIRS: object
    WHITE_TERRACOTTA: object
    ORANGE_TERRACOTTA: object
    MAGENTA_TERRACOTTA: object
    LIGHT_BLUE_TERRACOTTA: object
    YELLOW_TERRACOTTA: object
    LIME_TERRACOTTA: object
    PINK_TERRACOTTA: object
    GRAY_TERRACOTTA: object
    LIGHT_GRAY_TERRACOTTA: object
    CYAN_TERRACOTTA: object
    PURPLE_TERRACOTTA: object
    BLUE_TERRACOTTA: object
    BROWN_TERRACOTTA: object
    GREEN_TERRACOTTA: object
    RED_TERRACOTTA: object
    BLACK_TERRACOTTA: object
    BARRIER: object
    LIGHT: object
    HAY_BLOCK: object
    WHITE_CARPET: object
    ORANGE_CARPET: object
    MAGENTA_CARPET: object
    LIGHT_BLUE_CARPET: object
    YELLOW_CARPET: object
    LIME_CARPET: object
    PINK_CARPET: object
    GRAY_CARPET: object
    LIGHT_GRAY_CARPET: object
    CYAN_CARPET: object
    PURPLE_CARPET: object
    BLUE_CARPET: object
    BROWN_CARPET: object
    GREEN_CARPET: object
    RED_CARPET: object
    BLACK_CARPET: object
    TERRACOTTA: object
    PACKED_ICE: object
    DIRT_PATH: object
    SUNFLOWER: object
    LILAC: object
    ROSE_BUSH: object
    PEONY: object
    TALL_GRASS: object
    LARGE_FERN: object
    WHITE_STAINED_GLASS: object
    ORANGE_STAINED_GLASS: object
    MAGENTA_STAINED_GLASS: object
    LIGHT_BLUE_STAINED_GLASS: object
    YELLOW_STAINED_GLASS: object
    LIME_STAINED_GLASS: object
    PINK_STAINED_GLASS: object
    GRAY_STAINED_GLASS: object
    LIGHT_GRAY_STAINED_GLASS: object
    CYAN_STAINED_GLASS: object
    PURPLE_STAINED_GLASS: object
    BLUE_STAINED_GLASS: object
    BROWN_STAINED_GLASS: object
    GREEN_STAINED_GLASS: object
    RED_STAINED_GLASS: object
    BLACK_STAINED_GLASS: object
    WHITE_STAINED_GLASS_PANE: object
    ORANGE_STAINED_GLASS_PANE: object
    MAGENTA_STAINED_GLASS_PANE: object
    LIGHT_BLUE_STAINED_GLASS_PANE: object
    YELLOW_STAINED_GLASS_PANE: object
    LIME_STAINED_GLASS_PANE: object
    PINK_STAINED_GLASS_PANE: object
    GRAY_STAINED_GLASS_PANE: object
    LIGHT_GRAY_STAINED_GLASS_PANE: object
    CYAN_STAINED_GLASS_PANE: object
    PURPLE_STAINED_GLASS_PANE: object
    BLUE_STAINED_GLASS_PANE: object
    BROWN_STAINED_GLASS_PANE: object
    GREEN_STAINED_GLASS_PANE: object
    RED_STAINED_GLASS_PANE: object
    BLACK_STAINED_GLASS_PANE: object
    PRISMARINE: object
    PRISMARINE_BRICKS: object
    DARK_PRISMARINE: object
    PRISMARINE_STAIRS: object
    PRISMARINE_BRICK_STAIRS: object
    DARK_PRISMARINE_STAIRS: object
    SEA_LANTERN: object
    RED_SANDSTONE: object
    CHISELED_RED_SANDSTONE: object
    CUT_RED_SANDSTONE: object
    RED_SANDSTONE_STAIRS: object
    REPEATING_COMMAND_BLOCK: object
    CHAIN_COMMAND_BLOCK: object
    MAGMA_BLOCK: object
    NETHER_WART_BLOCK: object
    WARPED_WART_BLOCK: object
    RED_NETHER_BRICKS: object
    BONE_BLOCK: object
    STRUCTURE_VOID: object
    SHULKER_BOX: object
    WHITE_SHULKER_BOX: object
    ORANGE_SHULKER_BOX: object
    MAGENTA_SHULKER_BOX: object
    LIGHT_BLUE_SHULKER_BOX: object
    YELLOW_SHULKER_BOX: object
    LIME_SHULKER_BOX: object
    PINK_SHULKER_BOX: object
    GRAY_SHULKER_BOX: object
    LIGHT_GRAY_SHULKER_BOX: object
    CYAN_SHULKER_BOX: object
    PURPLE_SHULKER_BOX: object
    BLUE_SHULKER_BOX: object
    BROWN_SHULKER_BOX: object
    GREEN_SHULKER_BOX: object
    RED_SHULKER_BOX: object
    BLACK_SHULKER_BOX: object
    WHITE_GLAZED_TERRACOTTA: object
    ORANGE_GLAZED_TERRACOTTA: object
    MAGENTA_GLAZED_TERRACOTTA: object
    LIGHT_BLUE_GLAZED_TERRACOTTA: object
    YELLOW_GLAZED_TERRACOTTA: object
    LIME_GLAZED_TERRACOTTA: object
    PINK_GLAZED_TERRACOTTA: object
    GRAY_GLAZED_TERRACOTTA: object
    LIGHT_GRAY_GLAZED_TERRACOTTA: object
    CYAN_GLAZED_TERRACOTTA: object
    PURPLE_GLAZED_TERRACOTTA: object
    BLUE_GLAZED_TERRACOTTA: object
    BROWN_GLAZED_TERRACOTTA: object
    GREEN_GLAZED_TERRACOTTA: object
    RED_GLAZED_TERRACOTTA: object
    BLACK_GLAZED_TERRACOTTA: object
    WHITE_CONCRETE: object
    ORANGE_CONCRETE: object
    MAGENTA_CONCRETE: object
    LIGHT_BLUE_CONCRETE: object
    YELLOW_CONCRETE: object
    LIME_CONCRETE: object
    PINK_CONCRETE: object
    GRAY_CONCRETE: object
    LIGHT_GRAY_CONCRETE: object
    CYAN_CONCRETE: object
    PURPLE_CONCRETE: object
    BLUE_CONCRETE: object
    BROWN_CONCRETE: object
    GREEN_CONCRETE: object
    RED_CONCRETE: object
    BLACK_CONCRETE: object
    WHITE_CONCRETE_POWDER: object
    ORANGE_CONCRETE_POWDER: object
    MAGENTA_CONCRETE_POWDER: object
    LIGHT_BLUE_CONCRETE_POWDER: object
    YELLOW_CONCRETE_POWDER: object
    LIME_CONCRETE_POWDER: object
    PINK_CONCRETE_POWDER: object
    GRAY_CONCRETE_POWDER: object
    LIGHT_GRAY_CONCRETE_POWDER: object
    CYAN_CONCRETE_POWDER: object
    PURPLE_CONCRETE_POWDER: object
    BLUE_CONCRETE_POWDER: object
    BROWN_CONCRETE_POWDER: object
    GREEN_CONCRETE_POWDER: object
    RED_CONCRETE_POWDER: object
    BLACK_CONCRETE_POWDER: object
    TURTLE_EGG: object
    SNIFFER_EGG: object
    DEAD_TUBE_CORAL_BLOCK: object
    DEAD_BRAIN_CORAL_BLOCK: object
    DEAD_BUBBLE_CORAL_BLOCK: object
    DEAD_FIRE_CORAL_BLOCK: object
    DEAD_HORN_CORAL_BLOCK: object
    TUBE_CORAL_BLOCK: object
    BRAIN_CORAL_BLOCK: object
    BUBBLE_CORAL_BLOCK: object
    FIRE_CORAL_BLOCK: object
    HORN_CORAL_BLOCK: object
    TUBE_CORAL: object
    BRAIN_CORAL: object
    BUBBLE_CORAL: object
    FIRE_CORAL: object
    HORN_CORAL: object
    DEAD_BRAIN_CORAL: object
    DEAD_BUBBLE_CORAL: object
    DEAD_FIRE_CORAL: object
    DEAD_HORN_CORAL: object
    DEAD_TUBE_CORAL: object
    TUBE_CORAL_FAN: object
    BRAIN_CORAL_FAN: object
    BUBBLE_CORAL_FAN: object
    FIRE_CORAL_FAN: object
    HORN_CORAL_FAN: object
    DEAD_TUBE_CORAL_FAN: object
    DEAD_BRAIN_CORAL_FAN: object
    DEAD_BUBBLE_CORAL_FAN: object
    DEAD_FIRE_CORAL_FAN: object
    DEAD_HORN_CORAL_FAN: object
    BLUE_ICE: object
    CONDUIT: object
    POLISHED_GRANITE_STAIRS: object
    SMOOTH_RED_SANDSTONE_STAIRS: object
    MOSSY_STONE_BRICK_STAIRS: object
    POLISHED_DIORITE_STAIRS: object
    MOSSY_COBBLESTONE_STAIRS: object
    END_STONE_BRICK_STAIRS: object
    STONE_STAIRS: object
    SMOOTH_SANDSTONE_STAIRS: object
    SMOOTH_QUARTZ_STAIRS: object
    GRANITE_STAIRS: object
    ANDESITE_STAIRS: object
    RED_NETHER_BRICK_STAIRS: object
    POLISHED_ANDESITE_STAIRS: object
    DIORITE_STAIRS: object
    COBBLED_DEEPSLATE_STAIRS: object
    POLISHED_DEEPSLATE_STAIRS: object
    DEEPSLATE_BRICK_STAIRS: object
    DEEPSLATE_TILE_STAIRS: object
    POLISHED_GRANITE_SLAB: object
    SMOOTH_RED_SANDSTONE_SLAB: object
    MOSSY_STONE_BRICK_SLAB: object
    POLISHED_DIORITE_SLAB: object
    MOSSY_COBBLESTONE_SLAB: object
    END_STONE_BRICK_SLAB: object
    SMOOTH_SANDSTONE_SLAB: object
    SMOOTH_QUARTZ_SLAB: object
    GRANITE_SLAB: object
    ANDESITE_SLAB: object
    RED_NETHER_BRICK_SLAB: object
    POLISHED_ANDESITE_SLAB: object
    DIORITE_SLAB: object
    COBBLED_DEEPSLATE_SLAB: object
    POLISHED_DEEPSLATE_SLAB: object
    DEEPSLATE_BRICK_SLAB: object
    DEEPSLATE_TILE_SLAB: object
    SCAFFOLDING: object
    REDSTONE: object
    REDSTONE_TORCH: object
    REDSTONE_BLOCK: object
    REPEATER: object
    COMPARATOR: object
    PISTON: object
    STICKY_PISTON: object
    SLIME_BLOCK: object
    HONEY_BLOCK: object
    OBSERVER: object
    HOPPER: object
    DISPENSER: object
    DROPPER: object
    LECTERN: object
    TARGET: object
    LEVER: object
    LIGHTNING_ROD: object
    DAYLIGHT_DETECTOR: object
    SCULK_SENSOR: object
    CALIBRATED_SCULK_SENSOR: object
    TRIPWIRE_HOOK: object
    TRAPPED_CHEST: object
    TNT: object
    REDSTONE_LAMP: object
    NOTE_BLOCK: object
    STONE_BUTTON: object
    POLISHED_BLACKSTONE_BUTTON: object
    OAK_BUTTON: object
    SPRUCE_BUTTON: object
    BIRCH_BUTTON: object
    JUNGLE_BUTTON: object
    ACACIA_BUTTON: object
    CHERRY_BUTTON: object
    DARK_OAK_BUTTON: object
    MANGROVE_BUTTON: object
    BAMBOO_BUTTON: object
    CRIMSON_BUTTON: object
    WARPED_BUTTON: object
    STONE_PRESSURE_PLATE: object
    POLISHED_BLACKSTONE_PRESSURE_PLATE: object
    LIGHT_WEIGHTED_PRESSURE_PLATE: object
    HEAVY_WEIGHTED_PRESSURE_PLATE: object
    OAK_PRESSURE_PLATE: object
    SPRUCE_PRESSURE_PLATE: object
    BIRCH_PRESSURE_PLATE: object
    JUNGLE_PRESSURE_PLATE: object
    ACACIA_PRESSURE_PLATE: object
    CHERRY_PRESSURE_PLATE: object
    DARK_OAK_PRESSURE_PLATE: object
    MANGROVE_PRESSURE_PLATE: object
    BAMBOO_PRESSURE_PLATE: object
    CRIMSON_PRESSURE_PLATE: object
    WARPED_PRESSURE_PLATE: object
    IRON_DOOR: object
    OAK_DOOR: object
    SPRUCE_DOOR: object
    BIRCH_DOOR: object
    JUNGLE_DOOR: object
    ACACIA_DOOR: object
    CHERRY_DOOR: object
    DARK_OAK_DOOR: object
    MANGROVE_DOOR: object
    BAMBOO_DOOR: object
    CRIMSON_DOOR: object
    WARPED_DOOR: object
    IRON_TRAPDOOR: object
    OAK_TRAPDOOR: object
    SPRUCE_TRAPDOOR: object
    BIRCH_TRAPDOOR: object
    JUNGLE_TRAPDOOR: object
    ACACIA_TRAPDOOR: object
    CHERRY_TRAPDOOR: object
    DARK_OAK_TRAPDOOR: object
    MANGROVE_TRAPDOOR: object
    BAMBOO_TRAPDOOR: object
    CRIMSON_TRAPDOOR: object
    WARPED_TRAPDOOR: object
    OAK_FENCE_GATE: object
    SPRUCE_FENCE_GATE: object
    BIRCH_FENCE_GATE: object
    JUNGLE_FENCE_GATE: object
    ACACIA_FENCE_GATE: object
    CHERRY_FENCE_GATE: object
    DARK_OAK_FENCE_GATE: object
    MANGROVE_FENCE_GATE: object
    BAMBOO_FENCE_GATE: object
    CRIMSON_FENCE_GATE: object
    WARPED_FENCE_GATE: object
    POWERED_RAIL: object
    DETECTOR_RAIL: object
    RAIL: object
    ACTIVATOR_RAIL: object
    SADDLE: object
    MINECART: object
    CHEST_MINECART: object
    FURNACE_MINECART: object
    TNT_MINECART: object
    HOPPER_MINECART: object
    CARROT_ON_A_STICK: object
    WARPED_FUNGUS_ON_A_STICK: object
    ELYTRA: object
    OAK_BOAT: object
    OAK_CHEST_BOAT: object
    SPRUCE_BOAT: object
    SPRUCE_CHEST_BOAT: object
    BIRCH_BOAT: object
    BIRCH_CHEST_BOAT: object
    JUNGLE_BOAT: object
    JUNGLE_CHEST_BOAT: object
    ACACIA_BOAT: object
    ACACIA_CHEST_BOAT: object
    CHERRY_BOAT: object
    CHERRY_CHEST_BOAT: object
    DARK_OAK_BOAT: object
    DARK_OAK_CHEST_BOAT: object
    MANGROVE_BOAT: object
    MANGROVE_CHEST_BOAT: object
    BAMBOO_RAFT: object
    BAMBOO_CHEST_RAFT: object
    STRUCTURE_BLOCK: object
    JIGSAW: object
    TURTLE_HELMET: object
    SCUTE: object
    FLINT_AND_STEEL: object
    APPLE: object
    BOW: object
    ARROW: object
    COAL: object
    CHARCOAL: object
    DIAMOND: object
    EMERALD: object
    LAPIS_LAZULI: object
    QUARTZ: object
    AMETHYST_SHARD: object
    RAW_IRON: object
    IRON_INGOT: object
    RAW_COPPER: object
    COPPER_INGOT: object
    RAW_GOLD: object
    GOLD_INGOT: object
    NETHERITE_INGOT: object
    NETHERITE_SCRAP: object
    WOODEN_SWORD: object
    WOODEN_SHOVEL: object
    WOODEN_PICKAXE: object
    WOODEN_AXE: object
    WOODEN_HOE: object
    STONE_SWORD: object
    STONE_SHOVEL: object
    STONE_PICKAXE: object
    STONE_AXE: object
    STONE_HOE: object
    GOLDEN_SWORD: object
    GOLDEN_SHOVEL: object
    GOLDEN_PICKAXE: object
    GOLDEN_AXE: object
    GOLDEN_HOE: object
    IRON_SWORD: object
    IRON_SHOVEL: object
    IRON_PICKAXE: object
    IRON_AXE: object
    IRON_HOE: object
    DIAMOND_SWORD: object
    DIAMOND_SHOVEL: object
    DIAMOND_PICKAXE: object
    DIAMOND_AXE: object
    DIAMOND_HOE: object
    NETHERITE_SWORD: object
    NETHERITE_SHOVEL: object
    NETHERITE_PICKAXE: object
    NETHERITE_AXE: object
    NETHERITE_HOE: object
    STICK: object
    BOWL: object
    MUSHROOM_STEW: object
    STRING: object
    FEATHER: object
    GUNPOWDER: object
    WHEAT_SEEDS: object
    WHEAT: object
    BREAD: object
    LEATHER_HELMET: object
    LEATHER_CHESTPLATE: object
    LEATHER_LEGGINGS: object
    LEATHER_BOOTS: object
    CHAINMAIL_HELMET: object
    CHAINMAIL_CHESTPLATE: object
    CHAINMAIL_LEGGINGS: object
    CHAINMAIL_BOOTS: object
    IRON_HELMET: object
    IRON_CHESTPLATE: object
    IRON_LEGGINGS: object
    IRON_BOOTS: object
    DIAMOND_HELMET: object
    DIAMOND_CHESTPLATE: object
    DIAMOND_LEGGINGS: object
    DIAMOND_BOOTS: object
    GOLDEN_HELMET: object
    GOLDEN_CHESTPLATE: object
    GOLDEN_LEGGINGS: object
    GOLDEN_BOOTS: object
    NETHERITE_HELMET: object
    NETHERITE_CHESTPLATE: object
    NETHERITE_LEGGINGS: object
    NETHERITE_BOOTS: object
    FLINT: object
    PORKCHOP: object
    COOKED_PORKCHOP: object
    PAINTING: object
    GOLDEN_APPLE: object
    ENCHANTED_GOLDEN_APPLE: object
    OAK_SIGN: object
    SPRUCE_SIGN: object
    BIRCH_SIGN: object
    JUNGLE_SIGN: object
    ACACIA_SIGN: object
    CHERRY_SIGN: object
    DARK_OAK_SIGN: object
    MANGROVE_SIGN: object
    BAMBOO_SIGN: object
    CRIMSON_SIGN: object
    WARPED_SIGN: object
    OAK_HANGING_SIGN: object
    SPRUCE_HANGING_SIGN: object
    BIRCH_HANGING_SIGN: object
    JUNGLE_HANGING_SIGN: object
    ACACIA_HANGING_SIGN: object
    CHERRY_HANGING_SIGN: object
    DARK_OAK_HANGING_SIGN: object
    MANGROVE_HANGING_SIGN: object
    BAMBOO_HANGING_SIGN: object
    CRIMSON_HANGING_SIGN: object
    WARPED_HANGING_SIGN: object
    BUCKET: object
    WATER_BUCKET: object
    LAVA_BUCKET: object
    POWDER_SNOW_BUCKET: object
    SNOWBALL: object
    LEATHER: object
    MILK_BUCKET: object
    PUFFERFISH_BUCKET: object
    SALMON_BUCKET: object
    COD_BUCKET: object
    TROPICAL_FISH_BUCKET: object
    AXOLOTL_BUCKET: object
    TADPOLE_BUCKET: object
    BRICK: object
    CLAY_BALL: object
    DRIED_KELP_BLOCK: object
    PAPER: object
    BOOK: object
    SLIME_BALL: object
    EGG: object
    COMPASS: object
    RECOVERY_COMPASS: object
    BUNDLE: object
    FISHING_ROD: object
    CLOCK: object
    SPYGLASS: object
    GLOWSTONE_DUST: object
    COD: object
    SALMON: object
    TROPICAL_FISH: object
    PUFFERFISH: object
    COOKED_COD: object
    COOKED_SALMON: object
    INK_SAC: object
    GLOW_INK_SAC: object
    COCOA_BEANS: object
    WHITE_DYE: object
    ORANGE_DYE: object
    MAGENTA_DYE: object
    LIGHT_BLUE_DYE: object
    YELLOW_DYE: object
    LIME_DYE: object
    PINK_DYE: object
    GRAY_DYE: object
    LIGHT_GRAY_DYE: object
    CYAN_DYE: object
    PURPLE_DYE: object
    BLUE_DYE: object
    BROWN_DYE: object
    GREEN_DYE: object
    RED_DYE: object
    BLACK_DYE: object
    BONE_MEAL: object
    BONE: object
    SUGAR: object
    CAKE: object
    WHITE_BED: object
    ORANGE_BED: object
    MAGENTA_BED: object
    LIGHT_BLUE_BED: object
    YELLOW_BED: object
    LIME_BED: object
    PINK_BED: object
    GRAY_BED: object
    LIGHT_GRAY_BED: object
    CYAN_BED: object
    PURPLE_BED: object
    BLUE_BED: object
    BROWN_BED: object
    GREEN_BED: object
    RED_BED: object
    BLACK_BED: object
    COOKIE: object
    FILLED_MAP: object
    SHEARS: object
    MELON_SLICE: object
    DRIED_KELP: object
    PUMPKIN_SEEDS: object
    MELON_SEEDS: object
    BEEF: object
    COOKED_BEEF: object
    CHICKEN: object
    COOKED_CHICKEN: object
    ROTTEN_FLESH: object
    ENDER_PEARL: object
    BLAZE_ROD: object
    GHAST_TEAR: object
    GOLD_NUGGET: object
    NETHER_WART: object
    POTION: object
    GLASS_BOTTLE: object
    SPIDER_EYE: object
    FERMENTED_SPIDER_EYE: object
    BLAZE_POWDER: object
    MAGMA_CREAM: object
    BREWING_STAND: object
    CAULDRON: object
    ENDER_EYE: object
    GLISTERING_MELON_SLICE: object
    ALLAY_SPAWN_EGG: object
    AXOLOTL_SPAWN_EGG: object
    BAT_SPAWN_EGG: object
    BEE_SPAWN_EGG: object
    BLAZE_SPAWN_EGG: object
    CAT_SPAWN_EGG: object
    CAMEL_SPAWN_EGG: object
    CAVE_SPIDER_SPAWN_EGG: object
    CHICKEN_SPAWN_EGG: object
    COD_SPAWN_EGG: object
    COW_SPAWN_EGG: object
    CREEPER_SPAWN_EGG: object
    DOLPHIN_SPAWN_EGG: object
    DONKEY_SPAWN_EGG: object
    DROWNED_SPAWN_EGG: object
    ELDER_GUARDIAN_SPAWN_EGG: object
    ENDER_DRAGON_SPAWN_EGG: object
    ENDERMAN_SPAWN_EGG: object
    ENDERMITE_SPAWN_EGG: object
    EVOKER_SPAWN_EGG: object
    FOX_SPAWN_EGG: object
    FROG_SPAWN_EGG: object
    GHAST_SPAWN_EGG: object
    GLOW_SQUID_SPAWN_EGG: object
    GOAT_SPAWN_EGG: object
    GUARDIAN_SPAWN_EGG: object
    HOGLIN_SPAWN_EGG: object
    HORSE_SPAWN_EGG: object
    HUSK_SPAWN_EGG: object
    IRON_GOLEM_SPAWN_EGG: object
    LLAMA_SPAWN_EGG: object
    MAGMA_CUBE_SPAWN_EGG: object
    MOOSHROOM_SPAWN_EGG: object
    MULE_SPAWN_EGG: object
    OCELOT_SPAWN_EGG: object
    PANDA_SPAWN_EGG: object
    PARROT_SPAWN_EGG: object
    PHANTOM_SPAWN_EGG: object
    PIG_SPAWN_EGG: object
    PIGLIN_SPAWN_EGG: object
    PIGLIN_BRUTE_SPAWN_EGG: object
    PILLAGER_SPAWN_EGG: object
    POLAR_BEAR_SPAWN_EGG: object
    PUFFERFISH_SPAWN_EGG: object
    RABBIT_SPAWN_EGG: object
    RAVAGER_SPAWN_EGG: object
    SALMON_SPAWN_EGG: object
    SHEEP_SPAWN_EGG: object
    SHULKER_SPAWN_EGG: object
    SILVERFISH_SPAWN_EGG: object
    SKELETON_SPAWN_EGG: object
    SKELETON_HORSE_SPAWN_EGG: object
    SLIME_SPAWN_EGG: object
    SNIFFER_SPAWN_EGG: object
    SNOW_GOLEM_SPAWN_EGG: object
    SPIDER_SPAWN_EGG: object
    SQUID_SPAWN_EGG: object
    STRAY_SPAWN_EGG: object
    STRIDER_SPAWN_EGG: object
    TADPOLE_SPAWN_EGG: object
    TRADER_LLAMA_SPAWN_EGG: object
    TROPICAL_FISH_SPAWN_EGG: object
    TURTLE_SPAWN_EGG: object
    VEX_SPAWN_EGG: object
    VILLAGER_SPAWN_EGG: object
    VINDICATOR_SPAWN_EGG: object
    WANDERING_TRADER_SPAWN_EGG: object
    WARDEN_SPAWN_EGG: object
    WITCH_SPAWN_EGG: object
    WITHER_SPAWN_EGG: object
    WITHER_SKELETON_SPAWN_EGG: object
    WOLF_SPAWN_EGG: object
    ZOGLIN_SPAWN_EGG: object
    ZOMBIE_SPAWN_EGG: object
    ZOMBIE_HORSE_SPAWN_EGG: object
    ZOMBIE_VILLAGER_SPAWN_EGG: object
    ZOMBIFIED_PIGLIN_SPAWN_EGG: object
    EXPERIENCE_BOTTLE: object
    FIRE_CHARGE: object
    WRITABLE_BOOK: object
    WRITTEN_BOOK: object
    ITEM_FRAME: object
    GLOW_ITEM_FRAME: object
    FLOWER_POT: object
    CARROT: object
    POTATO: object
    BAKED_POTATO: object
    POISONOUS_POTATO: object
    MAP: object
    GOLDEN_CARROT: object
    SKELETON_SKULL: object
    WITHER_SKELETON_SKULL: object
    PLAYER_HEAD: object
    ZOMBIE_HEAD: object
    CREEPER_HEAD: object
    DRAGON_HEAD: object
    PIGLIN_HEAD: object
    NETHER_STAR: object
    PUMPKIN_PIE: object
    FIREWORK_ROCKET: object
    FIREWORK_STAR: object
    ENCHANTED_BOOK: object
    NETHER_BRICK: object
    PRISMARINE_SHARD: object
    PRISMARINE_CRYSTALS: object
    RABBIT: object
    COOKED_RABBIT: object
    RABBIT_STEW: object
    RABBIT_FOOT: object
    RABBIT_HIDE: object
    ARMOR_STAND: object
    IRON_HORSE_ARMOR: object
    GOLDEN_HORSE_ARMOR: object
    DIAMOND_HORSE_ARMOR: object
    LEATHER_HORSE_ARMOR: object
    LEAD: object
    NAME_TAG: object
    COMMAND_BLOCK_MINECART: object
    MUTTON: object
    COOKED_MUTTON: object
    WHITE_BANNER: object
    ORANGE_BANNER: object
    MAGENTA_BANNER: object
    LIGHT_BLUE_BANNER: object
    YELLOW_BANNER: object
    LIME_BANNER: object
    PINK_BANNER: object
    GRAY_BANNER: object
    LIGHT_GRAY_BANNER: object
    CYAN_BANNER: object
    PURPLE_BANNER: object
    BLUE_BANNER: object
    BROWN_BANNER: object
    GREEN_BANNER: object
    RED_BANNER: object
    BLACK_BANNER: object
    END_CRYSTAL: object
    CHORUS_FRUIT: object
    POPPED_CHORUS_FRUIT: object
    TORCHFLOWER_SEEDS: object
    PITCHER_POD: object
    BEETROOT: object
    BEETROOT_SEEDS: object
    BEETROOT_SOUP: object
    DRAGON_BREATH: object
    SPLASH_POTION: object
    SPECTRAL_ARROW: object
    TIPPED_ARROW: object
    LINGERING_POTION: object
    SHIELD: object
    TOTEM_OF_UNDYING: object
    SHULKER_SHELL: object
    IRON_NUGGET: object
    KNOWLEDGE_BOOK: object
    DEBUG_STICK: object
    MUSIC_DISC_13: object
    MUSIC_DISC_CAT: object
    MUSIC_DISC_BLOCKS: object
    MUSIC_DISC_CHIRP: object
    MUSIC_DISC_FAR: object
    MUSIC_DISC_MALL: object
    MUSIC_DISC_MELLOHI: object
    MUSIC_DISC_STAL: object
    MUSIC_DISC_STRAD: object
    MUSIC_DISC_WARD: object
    MUSIC_DISC_11: object
    MUSIC_DISC_WAIT: object
    MUSIC_DISC_OTHERSIDE: object
    MUSIC_DISC_RELIC: object
    MUSIC_DISC_5: object
    MUSIC_DISC_PIGSTEP: object
    DISC_FRAGMENT_5: object
    TRIDENT: object
    PHANTOM_MEMBRANE: object
    NAUTILUS_SHELL: object
    HEART_OF_THE_SEA: object
    CROSSBOW: object
    SUSPICIOUS_STEW: object
    LOOM: object
    FLOWER_BANNER_PATTERN: object
    CREEPER_BANNER_PATTERN: object
    SKULL_BANNER_PATTERN: object
    MOJANG_BANNER_PATTERN: object
    GLOBE_BANNER_PATTERN: object
    PIGLIN_BANNER_PATTERN: object
    GOAT_HORN: object
    COMPOSTER: object
    BARREL: object
    SMOKER: object
    BLAST_FURNACE: object
    CARTOGRAPHY_TABLE: object
    FLETCHING_TABLE: object
    GRINDSTONE: object
    SMITHING_TABLE: object
    STONECUTTER: object
    BELL: object
    LANTERN: object
    SOUL_LANTERN: object
    SWEET_BERRIES: object
    GLOW_BERRIES: object
    CAMPFIRE: object
    SOUL_CAMPFIRE: object
    SHROOMLIGHT: object
    HONEYCOMB: object
    BEE_NEST: object
    BEEHIVE: object
    HONEY_BOTTLE: object
    HONEYCOMB_BLOCK: object
    LODESTONE: object
    CRYING_OBSIDIAN: object
    BLACKSTONE: object
    BLACKSTONE_SLAB: object
    BLACKSTONE_STAIRS: object
    GILDED_BLACKSTONE: object
    POLISHED_BLACKSTONE: object
    POLISHED_BLACKSTONE_SLAB: object
    POLISHED_BLACKSTONE_STAIRS: object
    CHISELED_POLISHED_BLACKSTONE: object
    POLISHED_BLACKSTONE_BRICKS: object
    POLISHED_BLACKSTONE_BRICK_SLAB: object
    POLISHED_BLACKSTONE_BRICK_STAIRS: object
    CRACKED_POLISHED_BLACKSTONE_BRICKS: object
    RESPAWN_ANCHOR: object
    CANDLE: object
    WHITE_CANDLE: object
    ORANGE_CANDLE: object
    MAGENTA_CANDLE: object
    LIGHT_BLUE_CANDLE: object
    YELLOW_CANDLE: object
    LIME_CANDLE: object
    PINK_CANDLE: object
    GRAY_CANDLE: object
    LIGHT_GRAY_CANDLE: object
    CYAN_CANDLE: object
    PURPLE_CANDLE: object
    BLUE_CANDLE: object
    BROWN_CANDLE: object
    GREEN_CANDLE: object
    RED_CANDLE: object
    BLACK_CANDLE: object
    SMALL_AMETHYST_BUD: object
    MEDIUM_AMETHYST_BUD: object
    LARGE_AMETHYST_BUD: object
    AMETHYST_CLUSTER: object
    POINTED_DRIPSTONE: object
    OCHRE_FROGLIGHT: object
    VERDANT_FROGLIGHT: object
    PEARLESCENT_FROGLIGHT: object
    FROGSPAWN: object
    ECHO_SHARD: object
    BRUSH: object
    NETHERITE_UPGRADE_SMITHING_TEMPLATE: object
    SENTRY_ARMOR_TRIM_SMITHING_TEMPLATE: object
    DUNE_ARMOR_TRIM_SMITHING_TEMPLATE: object
    COAST_ARMOR_TRIM_SMITHING_TEMPLATE: object
    WILD_ARMOR_TRIM_SMITHING_TEMPLATE: object
    WARD_ARMOR_TRIM_SMITHING_TEMPLATE: object
    EYE_ARMOR_TRIM_SMITHING_TEMPLATE: object
    VEX_ARMOR_TRIM_SMITHING_TEMPLATE: object
    TIDE_ARMOR_TRIM_SMITHING_TEMPLATE: object
    SNOUT_ARMOR_TRIM_SMITHING_TEMPLATE: object
    RIB_ARMOR_TRIM_SMITHING_TEMPLATE: object
    SPIRE_ARMOR_TRIM_SMITHING_TEMPLATE: object
    WAYFINDER_ARMOR_TRIM_SMITHING_TEMPLATE: object
    SHAPER_ARMOR_TRIM_SMITHING_TEMPLATE: object
    SILENCE_ARMOR_TRIM_SMITHING_TEMPLATE: object
    RAISER_ARMOR_TRIM_SMITHING_TEMPLATE: object
    HOST_ARMOR_TRIM_SMITHING_TEMPLATE: object
    ANGLER_POTTERY_SHERD: object
    ARCHER_POTTERY_SHERD: object
    ARMS_UP_POTTERY_SHERD: object
    BLADE_POTTERY_SHERD: object
    BREWER_POTTERY_SHERD: object
    BURN_POTTERY_SHERD: object
    DANGER_POTTERY_SHERD: object
    EXPLORER_POTTERY_SHERD: object
    FRIEND_POTTERY_SHERD: object
    HEART_POTTERY_SHERD: object
    HEARTBREAK_POTTERY_SHERD: object
    HOWL_POTTERY_SHERD: object
    MINER_POTTERY_SHERD: object
    MOURNER_POTTERY_SHERD: object
    PLENTY_POTTERY_SHERD: object
    PRIZE_POTTERY_SHERD: object
    SHEAF_POTTERY_SHERD: object
    SHELTER_POTTERY_SHERD: object
    SKULL_POTTERY_SHERD: object
    SNORT_POTTERY_SHERD: object

class ItemStack:
    """
    Represents an item stack in Minecraft.
    """

    @overload
    def __init__(self, item: Items, count: Number, nbt: dict[str, object]) -> None:
        """
        Initializes an ItemStack with the specified item, count, and NBT data.

        Args:
            item (Items): The item type.
            count (Number): The number of items in the stack.
            nbt (dict[str, object]): The NBT data associated with the item.

        Returns:
            None
        """
    @overload
    def __init__(self, item: Items, nbt: dict[str, object]) -> None:
        """
        Initializes an ItemStack with the specified item and NBT data.

        Args:
            item (Items): The item type.
            nbt (dict[str, object]): The NBT data associated with the item.

        Returns:
            None
        """
    @overload
    def __init__(self, item: Items, count: Number) -> None:
        """
        Initializes an ItemStack with the specified item and count.

        Args:
            item (Items): The item type.
            count (Number): The number of items in the stack.

        Returns:
            None
        """
    @overload
    def __init__(self, item: Items) -> None:
        """
        Initializes an ItemStack with the specified item.

        Args:
            item (Items): The item type.

        Returns:
            None
        """
    def addEnchantment(self, enchantment: Enchantments, level: Number) -> None:
        """
        Adds an enchantment to the item stack.

        Args:
            enchantment (Enchantments): The enchantment to add.
            level (Number): The level of enchantment.

        Returns:
            None
        """
    def addHideFlag(self, hideFlag: HideFlags) -> None:
        """
        Adds a hide flag to the item stack.

        Args:
            hideFlag (HideFlags): The hide flag to add.

        Returns:
            None
        """
    def decrement(self, amount: Number) -> None:
        """
        Decrements the count of items in the stack by the specified amount.

        Args:
            amount (Number): The amount to decrement.

        Returns:
            None
        """
    def getCount(self) -> int:
        """
        Returns the number of items in the stack.

        Returns:
            int: The count of items.
        """
    def getDamage(self) -> int:
        """
        Returns the damage value of the item stack.

        Returns:
            int: The damage value.
        """
    def getEnchantments(self) -> list[Enchantment]:
        """
        Returns a list of enchantments applied to the item stack.

        Returns:
            list[Enchantment]: The list of enchantments.
        """
    def getMaxCount(self) -> int:
        """
        Returns the maximum count of items allowed in the stack.

        Returns:
            int: The maximum count.
        """
    def getMaxDamage(self) -> int:
        """
        Returns the maximum damage value of the item stack.

        Returns:
            int: The maximum damage value.
        """
    def getName(self) -> str:
        """
        Returns the name of the item.

        Returns:
            str: The item name.
        """
    def getNbt(self) -> dict[str, object]:
        """
        Returns the NBT data associated with the item stack.

        Returns:
            dict[str, object]: The NBT data.
        """
    def getRarity(self) -> ItemRarity:
        """
        Returns the rarity of the item.

        Returns:
            ItemRarity: The item rarity.
        """
    def getRepairCost(self) -> int:
        """
        Returns the repair cost of the item.

        Returns:
            int: The repair cost.
        """
    def hasCustomName(self) -> bool:
        """
        Checks if the item has a custom name.

        Returns:
            bool: True if the item has a custom name, False otherwise.
        """
    def hasEnchantments(self) -> bool:
        """
        Checks if the item has any enchantments.

        Returns:
            bool: True if the item has enchantments, False otherwise.
        """
    def hasGlint(self) -> bool:
        """
        Checks if the item has a glint effect.

        Returns:
            bool: True if the item has a glint effect, False otherwise.
        """
    def hasNbt(self) -> bool:
        """
        Checks if the item has NBT data.

        Returns:
            bool: True if the item has NBT data, False otherwise.
        """
    def increment(self, amount: Number) -> None:
        """
        Increments the count of items in the stack by the specified amount.

        Args:
            amount (Number): The amount to increment.

        Returns:
            None
        """
    def isDamageable(self) -> bool:
        """
        Checks if the item is damageable.

        Returns:
            bool: True if the item is damageable, False otherwise.
        """
    def isDamaged(self) -> bool:
        """
        Checks if the item is damaged.

        Returns:
            bool: True if the item is damaged, False otherwise.
        """
    def isEnchantable(self) -> bool:
        """
        Checks if the item is enchantable.

        Returns:
            bool: True if the item is enchantable, False otherwise.
        """
    def isFood(self) -> bool:
        """
        Checks if the item is a food item.

        Returns:
            bool: True if the item is a food item, False otherwise.
        """
    def isItemBarVisible(self) -> bool:
        """
        Checks if the item bar is visible.

        Returns:
            bool: True if the item bar is visible, False otherwise.
        """
    def isStackable(self) -> bool:
        """
        Checks if the item is stackable.

        Returns:
            bool: True if the item is stackable, False otherwise.
        """
    def removeCustomName(self) -> None:
        """
        Removes the custom name of the item.

        Returns:
            None
        """
    def setCount(self, count: Number) -> None:
        """
        Sets the count of items in the stack.

        Args:
            count (Number): The count of items.

        Returns:
            None
        """
    @overload
    def setCustomName(self, customName: str) -> None:
        """
        Sets the custom name of the item.

        Args:
            customName (str): The custom name.

        Returns:
            None
        """
    @overload
    def setCustomName(self, text: Text) -> None:
        """
        Sets the custom name of the item using a text object.

        Args:
            text (Text): The text object representing the custom name.

        Returns:
            None
        """
    def setDamage(self, damage: Number) -> None:
        """
        Sets the damage value of the item stack.

        Args:
            damage (Number): The damage value.

        Returns:
            None
        """
    def setRepairCost(self, repairCost: Number) -> None:
        """
        Sets the repair cost of the item.

        Args:
            repairCost (Number): The repair cost.

        Returns:
            None
        """

class LivingEntity(Entity):
    """
    Represents a living entity in the game.
    Inherits from Entity.
    """

    def addStatusEffect(
        self, effect: StatusEffects, duration: Number, amplifier: Number, visible: bool
    ) -> None:
        """
        Adds a status effect to the living entity.

        Args:
            effect (StatusEffects): The status effect to add.
            duration (Number): The duration of the effect.
            amplifier (Number): The amplifier level of the effect.
            visible (bool): Whether the effect is visible.

        Returns:
            None
        """
    def canBreatheInWater(self) -> bool:
        """
        Checks if the living entity can breathe underwater.

        Returns:
            bool: True if the entity can breathe in water, False otherwise.
        """
    def canHaveStatusEffect(self, effect: StatusEffects) -> bool:
        """
        Checks if the living entity can have the specified status effect.

        Args:
            effect (StatusEffects): The status effect to check.

        Returns:
            bool: True if the entity can have the effect, False otherwise.
        """
    def canSee(self, entity: Entity) -> bool:
        """
        Checks if the living entity can see the specified entity.

        Args:
            entity (Entity): The entity to check visibility.

        Returns:
            bool: True if the entity can see the other entity, False otherwise.
        """
    def canTakeDamage(self) -> bool:
        """
        Checks if the living entity can take damage.

        Returns:
            bool: True if the entity can take damage, False otherwise.
        """
    def clearStatusEffects(self) -> None:
        """
        Clears all status effects from the living entity.

        Returns:
            None
        """
    def damageArmor(self, damageSource: DamageSources, amount: Number) -> None:
        """
        Damages the entity's armor by the specified amount.

        Args:
            damageSource (DamageSources): The source of the damage.
            amount (Number): The amount of damage to apply.

        Returns:
            None
        """
    def damageHelmet(self, damageSource: DamageSources, amount: Number) -> None:
        """
        Damages the entity's helmet by the specified amount.

        Args:
            damageSource (DamageSources): The source of the damage.
            amount (Number): The amount of damage to apply.

        Returns:
            None
        """
    def damageShield(self, amount: Number) -> None:
        """
        Damages the entity's shield by the specified amount.

        Args:
            amount (Number): The amount of damage to apply.

        Returns:
            None
        """
    def eatFood(self, stack: ItemStack) -> None:
        """
        Makes the living entity eat the specified food item stack.

        Args:
            stack (ItemStack): The food item stack to eat.

        Returns:
            None
        """
    def getAbsorptionAmount(self) -> float:
        """
        Returns the absorption amount of the living entity.

        Returns:
            float: The absorption amount.
        """
    def getActiveHand(self) -> Hand:
        """
        Returns the active hand of the living entity.

        Returns:
            Hand: The active hand.
        """
    def getActiveItem(self) -> ItemStack:
        """
        Returns the item stack in the entity's active hand.

        Returns:
            ItemStack: The active item stack.
        """
    def getArmor(self) -> float:
        """
        Returns the armor value of the living entity.

        Returns:
            float: The armor value.
        """
    def getAttacker(self) -> LivingEntity:
        """
        Returns the entity that attacked this living entity.

        Returns:
            LivingEntity: The attacking entity.
        """
    def getAttacking(self) -> LivingEntity:
        """
        Returns the entity that this living entity is currently attacking.

        Returns:
            LivingEntity: The attacking entity.
        """
    def getMainArm(self) -> Arm:
        """
        Returns the main arm of the living entity.

        Returns:
            Arm: The main arm.
        """
    def getMainHandStack(self) -> ItemStack:
        """
        Returns the item stack in the entity's main hand.

        Returns:
            ItemStack: The main hand item stack.
        """
    def getMaxHealth(self) -> float:
        """
        Returns the maximum health of the living entity.

        Returns:
            float: The maximum health.
        """
    def getMovementSpeed(self) -> float:
        """
        Returns the movement speed of the living entity.

        Returns:
            float: The movement speed.
        """
    def getScaleFactor(self) -> float:
        """
        Returns the scale factor of the living entity.

        Returns:
            float: The scale factor.
        """
    def getStackInHand(self, hand: Hand) -> ItemStack:
        """
        Returns the item stack in the specified hand.

        Args:
            hand (Hand): The hand to get the item stack from.

        Returns:
            ItemStack: The item stack in the hand.
        """
    def getStatusEffect(self, effect: StatusEffects) -> StatusEffectInstance:
        """
        Returns the status effect instance of the specified effect.

        Args:
            effect (StatusEffects): The status effect to retrieve.

        Returns:
            StatusEffectInstance: The status effect instance.
        """
    def getStatusEffects(self) -> list[StatusEffectInstance]:
        """
        Returns a list of all status effects applied to the living entity.

        Returns:
            list[StatusEffectInstance]: The list of status effect instances.
        """
    def getStuckArrowCount(self) -> float:
        """
        Returns the number of arrows stuck in the living entity.

        Returns:
            float: The stuck arrow count.
        """
    def hasStatusEffect(self, effect: StatusEffects) -> bool:
        """
        Checks if the living entity has the specified status effect.

        Args:
            effect (StatusEffects): The status effect to check.

        Returns:
            bool: True if the entity has the effect, False otherwise.
        """
    def heal(self, amount: Number) -> None:
        """
        Heals the living entity by the specified amount.

        Args:
            amount (Number): The amount to heal.

        Returns:
            None
        """
    def getHealth(self) -> float:
        """
        Returns the current health of the living entity.

        Returns:
            float: The current health.
        """
    def isAffectedBySplashPotions(self) -> bool:
        """
        Checks if the living entity is affected by splash potions.

        Returns:
            bool: True if the entity is affected, False otherwise.
        """
    def isBaby(self) -> bool:
        """
        Checks if the living entity is a baby.

        Returns:
            bool: True if the entity is a baby, False otherwise.
        """
    def isBlocking(self) -> bool:
        """
        Checks if the living entity is currently blocking.

        Returns:
            bool: True if the entity is blocking, False otherwise.
        """
    def isClimbing(self) -> bool:
        """
        Checks if the living entity is currently climbing.

        Returns:
            bool: True if the entity is climbing, False otherwise.
        """
    def isDead(self) -> bool:
        """
        Checks if the living entity is dead.

        Returns:
            bool: True if the entity is dead, False otherwise.
        """
    def isFallFlying(self) -> bool:
        """
        Checks if the living entity is currently fall flying.

        Returns:
            bool: True if the entity is fall flying, False otherwise.
        """
    def isHolding(self, item: Item) -> bool:
        """
        Checks if the living entity is holding the specified item.

        Args:
            item (Item): The item to check.

        Returns:
            bool: True if the entity is holding the item, False otherwise.
        """
    def isHoldingOntoLadder(self) -> bool:
        """
        Checks if the living entity is holding onto a ladder.

        Returns:
            bool: True if the entity is holding onto a ladder, False otherwise.
        """
    def isHurtByWater(self) -> bool:
        """
        Checks if water hurts the living entity.

        Returns:
            bool: True if water hurts the entity, False otherwise.
        """
    def isMobOrPlayer(self) -> bool:
        """
        Checks if the living entity is either a mob or a player.

        Returns:
            bool: True if the entity is a mob or a player, False otherwise.
        """
    def isSleeping(self) -> bool:
        """
        Checks if the living entity is sleeping.

        Returns:
            bool: True if the entity is sleeping, False otherwise.
        """
    def isUndead(self) -> bool:
        """
        Checks if the living entity is undead.

        Returns:
            bool: True if the entity is undead, False otherwise.
        """
    def isUsingItem(self) -> bool:
        """
        Checks if the living entity is currently using an item.

        Returns:
            bool: True if the entity is using an item, False otherwise.
        """
    def isUsingRiptide(self) -> bool:
        """
        Checks if the living entity is currently using the riptide enchantment.

        Returns:
            bool: True if the entity is using riptide, False otherwise.
        """
    def removeStatusEffect(self, effect: StatusEffects) -> None:
        """
        Removes the specified status effect from the living entity.

        Args:
            effect (StatusEffects): The status effect to remove.

        Returns:
            None
        """
    def setAbsorptionAmount(self, amount: Number) -> None:
        """
        Sets the absorption amount of the living entity.

        Args:
            amount (Number): The absorption amount to set.

        Returns:
            None
        """
    def setAttacker(self, entity: LivingEntity) -> None:
        """
        Sets the entity that attacked this living entity.

        Args:
            entity (LivingEntity): The attacking entity.

        Returns:
            None
        """
    def setAttacking(self, entity: LivingEntity) -> None:
        """
        Sets the entity that this living entity is currently attacking.

        Args:
            entity (LivingEntity): The attacking entity.

        Returns:
            None
        """
    def setCurrentHand(self, hand: Hand) -> None:
        """
        Sets the current hand of the living entity.

        Args:
            hand (Hand): The hand to set as current.

        Returns:
            None
        """
    def setHealth(self, amount: Number) -> None:
        """
        Sets the current health of the living entity.

        Args:
            amount (Number): The amount to set as health.

        Returns:
            None
        """
    def setJumping(self, jumping: bool) -> None:
        """
        Sets whether the living entity is jumping.

        Args:
            jumping (bool): True if the entity is jumping, False otherwise.

        Returns:
            None
        """
    def setMovementSpeed(self, movementSpeed: Number) -> None:
        """
        Sets the movement speed of the living entity.

        Args:
            movementSpeed (Number): The movement speed to set.

        Returns:
            None
        """
    def setStackInHand(self, hand: Hand, stack: ItemStack) -> None:
        """
        Sets the item stack in the specified hand.

        Args:
            hand (Hand): The hand to set the item stack in.
            stack (ItemStack): The item stack to set.

        Returns:
            None
        """
    def setStingerCount(self, stingerCount: Number) -> None:
        """
        Sets the stinger count of the living entity.

        Args:
            stingerCount (Number): The stinger count to set.

        Returns:
            None
        """
    def setStuckArrowCount(self, stuckArrowCount: Number) -> None:
        """
        Sets the number of arrows stuck in the living entity.

        Args:
            stuckArrowCount (Number): The stuck arrow count to set.

        Returns:
            None
        """
    def shouldDisplaySoulSpeedEffects(self) -> bool:
        """
        Checks if the living entity should display soul speed effects.

        Returns:
            bool: True if the entity should display soul speed effects, False otherwise.
        """
    def shouldDropXp(self) -> bool:
        """
        Checks if the living entity should drop experience points upon death.

        Returns:
            bool: True if the entity should drop experience points, False otherwise.
        """
    def swingHand(self, hand: Hand) -> None:
        """
        Swings the specified hand of the living entity.

        Args:
            hand (Hand): The hand to swing.

        Returns:
            None
        """
    def takeKnockback(self, strength: Number, x: Number, z: Number) -> None:
        """
        Applies knockback to the living entity.

        Args:
            strength (Number): The strength of the knockback.
            x (Number): The x-direction of the knockback.
            z (Number): The z-direction of the knockback.

        Returns:
            None
        """
    def teleport(self, position: Vec3d) -> None:
        """
        Teleports the living entity to the specified position.

        Args:
            position (Vec3d): The position to teleport to.

        Returns:
            None
        """
    def tiltScreen(self, deltaX: Number, deltaY: Number) -> None:
        """
        Tilts the screen of the living entity by the specified amount.

        Args:
            deltaX (Number): The amount to tilt the screen horizontally.
            deltaY (Number): The amount to tilt the screen vertically.

        Returns:
            None
        """

class PlayerEntity(LivingEntity):
    def addExhaustion(self, exhaustion: Number) -> None:
        """
        Increases the exhaustion level of the player.

        Args:
            exhaustion (Number): The amount of exhaustion to add.

        Returns:
            None
        """
    def addExperience(self, experience: Number) -> None:
        """
        Adds experience points to the player.

        Args:
            experience (Number): The number of experience points to add.

        Returns:
            None
        """
    def addExperienceLevels(self, levels: Number) -> None:
        """
        Adds experience levels to the player.

        Args:
            levels (Number): The number of levels to add.

        Returns:
            None
        """
    def addScore(self, score: Number) -> None:
        """
        Adds a score value to the player.

        Args:
            score (Number): The score value to add.

        Returns:
            None
        """
    def addShoulderEntity(self, entityNbt: dict[str, object]) -> None:
        """
        Adds an entity to the player's shoulder.

        Args:
            entityNbt (dict[str, object]): The NBT data of the entity to add.

        Returns:
            None
        """
    def attack(self, entity: Entity) -> None:
        """
        Attacks the specified entity.

        Args:
            entity (Entity): The entity to attack.

        Returns:
            None
        """
    def canConsume(self, ignoreHunger: bool) -> bool:
        """
        Checks if the player can consume items.

        Args:
            ignoreHunger (bool): Whether to ignore hunger level when checking.

        Returns:
            bool: True if the player can consume items, False otherwise.
        """
    def canFoodHeal(self) -> bool:
        """
        Checks if the player can heal using food.

        Returns:
            bool: True if the player can heal with food, False otherwise.
        """
    def canHarvest(self, block: Blocks | BlockState) -> bool:
        """
        Checks if the player can harvest the specified block.

        Args:
            block (Union[Blocks, BlockState]): The block to check.

        Returns:
            bool: True if the player can harvest the block, False otherwise.
        """
    def checkFallFlying(self) -> bool:
        """
        Checks if the player can use elytra to fall with reduced speed.

        Returns:
            bool: True if the player can fall flying, False otherwise.
        """
    def disableShield(self, sprinting: bool) -> None:
        """
        Disables the player's shield.

        Args:
            sprinting (bool): Whether the player is sprinting.

        Returns:
            None
        """
    def getAttackCooldownProgress(self, baseTime: Number) -> float:
        """
        Calculates the progress of the attack cooldown.

        Args:
            baseTime (Number): The base time for the attack cooldown.

        Returns:
            float: The progress of the attack cooldown as a value between 0.0 and 1.0.
        """
    def getEnderChestInventory(self) -> EnderChestInventory:
        """
        Retrieves the ender chest inventory of the player.

        Returns:
            EnderChestInventory: The ender chest inventory of the player.
        """
    def getHungerManager(self) -> HungerManager:
        """
        Retrieves the hunger manager of the player.

        Returns:
            HungerManager: The hunger manager of the player.
        """
    def getInventory(self) -> PlayerInventory:
        """
        Retrieves the inventory of the player.

        Returns:
            PlayerInventory: The inventory of the player.
        """
    def getShoulderEntityLeft(self) -> dict[str, object]:
        """
        Retrieves the entity data on the player's left shoulder.

        Returns:
            dict[str, object]: The NBT data of the entity on the left shoulder.
        """
    def getShoulderEntityRight(self) -> dict[str, object]:
        """
        Retrieves the entity data on the player's right shoulder.

        Returns:
            dict[str, object]: The NBT data of the entity on the right shoulder.
        """
    def isCreative(self) -> bool:
        """
        Checks if the player is in creative mode.

        Returns:
            bool: True if the player is in creative mode, False otherwise.
        """
    def isMainPlayer(self) -> bool:
        """
        Checks if the player is the main player.

        Returns:
            bool: True if the player is the main player, False otherwise.
        """
    def isUsingSglass(self) -> bool:
        """
        Checks if the player is using a spyglass.

        Returns:
            bool: True if the player is using a spyglass, False otherwise.
        """
    def requestRespawn(self) -> None:
        """
        Requests the player to respawn.

        Returns:
            None
        """
    def sendMessage(self, message: str) -> None:
        """
        Sends a message to the player.

        Args:
            message: The message to send.

        Returns:
            None
        """
    def setMainArm(self, arm: Arm) -> None:
        """
        Sets the player's main arm.

        Args:
            arm (Arm): The main arm to set.

        Returns:
            None
        """

class PlayerInventory:
    main: list[ItemStack]
    armor: list[ItemStack]
    offHand: list[ItemStack]
    selectedSlot: int

    def clear(self) -> None:
        """
        Clears the player's inventory.

        Returns:
            None
        """
    def contains(self, stack: ItemStack) -> bool:
        """
        Checks if the inventory contains the specified item stack.

        Args:
            stack (ItemStack): The item stack to check.

        Returns:
            bool: True if the inventory contains the item stack, False otherwise.
        """
    def dropAll(self) -> None:
        """
        Drops all items from the inventory.

        Returns:
            None
        """
    def dropSelectedItem(self, entireStack: bool) -> None:
        """
        Drops the selected item from the inventory.

        Args:
            entireStack (bool): Whether to drop the entire stack or just one item.

        Returns:
            None
        """
    def getArmorStack(self, slot: Number) -> ItemStack:
        """
        Retrieves the item stack in the specified armor slot.

        Args:
            slot (Number): The armor slot.

        Returns:
            ItemStack: The item stack in the specified armor slot.
        """
    def getEmptySlot(self) -> int:
        """
        Retrieves the index of an empty slot in the inventory.

        Returns:
            int: The index of an empty slot, or -1 if no empty slot is found.
        """
    def getMainHandStack(self) -> ItemStack:
        """
        Retrieves the item stack in the player's main hand.

        Returns:
            ItemStack: The item stack in the player's main hand.
        """
    def getSlotWithStack(self, stack: ItemStack) -> int:
        """
        Retrieves the index of the slot that contains the specified item stack.

        Args:
            stack (ItemStack): The item stack to search for.

        Returns:
            int: The index of the slot that contains the item stack, or -1 if not found.
        """
    def getStack(self, slot: Number) -> ItemStack:
        """
        Retrieves the item stack in the specified slot.

        Args:
            slot (Number): The slot index.

        Returns:
            ItemStack: The item stack in the specified slot.
        """
    def indexOf(self, stack: ItemStack) -> int:
        """
        Retrieves the index of the first occurrence of the specified item stack.

        Args:
            stack (ItemStack): The item stack to search for.

        Returns:
            int: The index of the first occurrence of the item stack, or -1 if not found.
        """
    def insertStack(self, slot: Number, stack: ItemStack) -> None:
        """
        Inserts the specified item stack into the specified slot.

        Args:
            slot (Number): The slot index.
            stack (ItemStack): The item stack to insert.

        Returns:
            None
        """
    def insertStack(self, stack: ItemStack) -> None:
        """
        Inserts the specified item stack into the first available slot.

        Args:
            stack (ItemStack): The item stack to insert.

        Returns:
            None
        """
    def isEmpty(self) -> bool:
        """
        Checks if the inventory is empty.

        Returns:
            bool: True if the inventory is empty, False otherwise.
        """
    def removeOne(self, stack: ItemStack) -> None:
        """
        Removes one item from the specified item stack.

        Args:
            stack (ItemStack): The item stack to remove from.

        Returns:
            None
        """
    def removeStack(self, slot: Number, amount: Number) -> None:
        """
        Removes a specified number of items from the specified slot.

        Args:
            slot (Number): The slot index.
            amount (Number): The number of items to remove.

        Returns:
            None
        """
    def removeStack(self, slot: Number) -> None:
        """
        Removes the item stack from the specified slot.

        Args:
            slot (Number): The slot index.

        Returns:
            None
        """
    def setStack(self, slot: Number, stack: ItemStack) -> None:
        """
        Sets the item stack in the specified slot.

        Args:
            slot (Number): The slot index.
            stack (ItemStack): The item stack to set.

        Returns:
            None
        """

class RemovalReasons:
    """
    A list of reasons for an entity to be removed
    """

    KILLED: object
    DISCARDED: object
    UNLOADED_TO_CHUNK: object
    UNLOADED_WITH_PLAYER: object
    CHANGED_DIMENSION: object

class RenderTypes:
    """
    A list of render types for scoreboards
    """

    INTEGER: object
    HEARTS: object

class Scoreboard:
    def getTeams(self) -> list[Team]:
        """
        Retrieves a list of all teams on the scoreboard.

        Returns:
            list[Team]: A list of all teams on the scoreboard.
        """
    def resetPlayerScore(self, playerName: str, objective: ScoreboardObjective) -> None:
        """
        Resets the score of a player for the specified objective.

        Args:
            playerName (str): The name of the player.
            objective (ScoreboardObjective): The objective to reset the player's score for.

        Returns:
            None
        """
    def getAllPlayerScores(
        self, objective: ScoreboardObjective
    ) -> list[ScoreboardPlayerScore]:
        """
        Retrieves a list of all player scores for the specified objective.

        Args:
            objective (ScoreboardObjective): The objective to retrieve player scores for.

        Returns:
            list[ScoreboardPlayerScore]: A list of all player scores for the objective.
        """
    def removeTeam(self, team: Team) -> None:
        """
        Removes the specified team from the scoreboard.

        Args:
            team (Team): The team to remove.

        Returns:
            None
        """
    def containsObjective(self, name: str) -> bool:
        """
        Checks if an objective with the specified name exists in the scoreboard.

        Args:
            name (str): The name of the objective.

        Returns:
            bool: True if the objective exists, False otherwise.
        """
    def addObjective(
        self,
        name: str,
        criterion: ScoreboardCriterions,
        displayName: Text,
        renderType: RenderTypes,
    ) -> None:
        """
        Adds a new objective to the scoreboard.

        Args:
            name (str): The name of the objective.
            criterion (ScoreboardCriterions): The criterion type of the objective.
            displayName (Text): The display name of the objective.
            renderType (RenderTypes): The render type of the objective.

        Returns:
            None
        """
    def removePlayerFromTeam(self, playerName: str, team: Team) -> None:
        """
        Removes a player from the specified team.

        Args:
            playerName (str): The name of the player.
            team (Team): The team to remove the player from.

        Returns:
            None
        """
    def getObjectives(self) -> list[ScoreboardObjective]:
        """
        Retrieves a list of all objectives on the scoreboard.

        Returns:
            list[ScoreboardObjective]: A list of all objectives on the scoreboard.
        """
    def addPlayerToTeam(self, playerName: str, team: Team) -> None:
        """
        Adds a player to the specified team.

        Args:
            playerName (str): The name of the player.
            team (Team): The team to add the player to.

        Returns:
            None
        """
    def clearPlayerTeam(self, playerName: str) -> None:
        """
        Clears the team association of a player.

        Args:
            playerName (str): The name of the player.

        Returns:
            None
        """
    def getObjectiveNames(self) -> list[str]:
        """
        Retrieves a list of names from all the objectives on the scoreboard.

        Returns:
            list[str]: A list of names from all the objectives on the scoreboard.
        """
    def getTeam(self, name: str) -> Team:
        """
        Retrieves the team with the specified name.

        Args:
            name (str): The name of the team.

        Returns:
            Team: The team object.
        """
    def resetEntityScore(self, entity: Entity) -> None:
        """
        Resets the score of an entity on all objectives.

        Args:
            entity (Entity): The entity.

        Returns:
            None
        """
    def getObjective(self, name: str) -> ScoreboardObjective:
        """
        Retrieves the objective with the specified name.

        Args:
            name (str): The name of the objective.

        Returns:
            ScoreboardObjective: The objective object.
        """
    def addTeam(self, name: str) -> None:
        """
        Adds a new team to the scoreboard.

        Args:
            name (str): The name of the team.

        Returns:
            None
        """
    def getTeamNames(self) -> list[str]:
        """
        Retrieves a list of names from all the teams on the scoreboard.

        Returns:
            list[str]: A list of names from all the teams on the scoreboard.
        """
    def removeObjective(self, objective: ScoreboardObjective) -> None:
        """
        Removes the specified objective from the scoreboard.

        Args:
            objective (ScoreboardObjective): The objective to remove.

        Returns:
            None
        """
    def getPlayerScore(
        self, name: str, objective: ScoreboardObjective
    ) -> ScoreboardPlayerScore:
        """
        Retrieves the score of a player for the specified objective.

        Args:
            name (str): The name of the player.
            objective (ScoreboardObjective): The objective to retrieve the player's score for.

        Returns:
            ScoreboardPlayerScore: The player's score for the objective.
        """
    def getPlayerTeam(self, name: str) -> Team:
        """
        Retrieves the team associated with the specified player.

        Args:
            name (str): The name of the player.

        Returns:
            Team: The associated team object.
        """

class ScoreboardCriterions:
    """
    A list of criterions for scoreboards
    """

    DUMMY: object
    TRIGGER: object
    DEATH_COUNT: object
    PLAYER_KILL_COUNT: object
    TOTAL_KILL_COUNT: object
    HEALTH: object
    FOOD: object
    AIR: object
    ARMOR: object
    XP: object
    LEVEL: object
    TEAM_KILL_BLACK: object
    TEAM_KILL_DARK_BLUE: object
    TEAM_KILL_DARK_GREEN: object
    TEAM_KILL_DARK_AQUA: object
    TEAM_KILL_DARK_RED: object
    TEAM_KILL_DARK_PURPLE: object
    TEAM_KILL_GOLD: object
    TEAM_KILL_GRAY: object
    TEAM_KILL_DARK_GRAY: object
    TEAM_KILL_BLUE: object
    TEAM_KILL_GREEN: object
    TEAM_KILL_AQUA: object
    TEAM_KILL_RED: object
    TEAM_KILL_LIGHT_PURPLE: object
    TEAM_KILL_YELLOW: object
    TEAM_KILL_WHITE: object
    KILLED_BY_TEAM_BLACK: object
    KILLED_BY_TEAM_DARK_BLUE: object
    KILLED_BY_TEAM_DARK_GREEN: object
    KILLED_BY_TEAM_DARK_AQUA: object
    KILLED_BY_TEAM_DARK_RED: object
    KILLED_BY_TEAM_DARK_PURPLE: object
    KILLED_BY_TEAM_GOLD: object
    KILLED_BY_TEAM_GRAY: object
    KILLED_BY_TEAM_DARK_GRAY: object
    KILLED_BY_TEAM_BLUE: object
    KILLED_BY_TEAM_GREEN: object
    KILLED_BY_TEAM_AQUA: object
    KILLED_BY_TEAM_RED: object
    KILLED_BY_TEAM_LIGHT_PURPLE: object
    KILLED_BY_TEAM_YELLOW: object
    KILLED_BY_TEAM_WHITE: object

class ScoreboardObjective:
    def getCriterion(self) -> ScoreboardCriterions:
        """
        Retrieves the criterion type of the scoreboard objective.

        Returns:
            ScoreboardCriterions: The criterion type of the objective.
        """
    def getDisplayName(self) -> Text:
        """
        Retrieves the display name of the scoreboard objective.

        Returns:
            Text: The display name of the objective.
        """
    def getName(self) -> str:
        """
        Retrieves the name of the scoreboard objective.

        Returns:
            str: The name of the objective.
        """
    def getRenderType(self) -> RenderTypes:
        """
        Retrieves the render type of the scoreboard objective.

        Returns:
            RenderTypes: The render type of the objective.
        """
    def setDisplayName(self, displayName: Text) -> None:
        """
        Sets the display name of the scoreboard objective.

        Args:
            displayName (Text): The display name to set.

        Returns:
            None
        """
    def setRenderType(self, renderType: RenderTypes) -> None:
        """
        Sets the render type of the scoreboard objective.

        Args:
            renderType (RenderTypes): The render type to set.

        Returns:
            None
        """

class ScoreboardPlayerScore:
    def clearScore(self) -> None:
        """
        Clears the score of the player.

        Returns:
            None
        """
    def getPlayerName(self) -> str:
        """
        Retrieves the name of the player associated with the score.

        Returns:
            str: The name of the player.
        """
    def getScore(self) -> int:
        """
        Retrieves the score value.

        Returns:
            int: The score value.
        """
    def getScoreboard(self) -> Scoreboard:
        """
        Retrieves the scoreboard associated with the score.

        Returns:
            Scoreboard: The associated scoreboard object.
        """
    def incrementScore(self) -> None:
        """
        Increments the score value by 1.

        Returns:
            None
        """
    def incrementScore(self, amount: Number) -> None:
        """
        Increments the score value by the specified amount.

        Args:
            amount (Number): The amount to increment the score by.

        Returns:
            None
        """
    def setScore(self, score: Number) -> None:
        """
        Sets the score value.

        Args:
            score (Number): The score value to set.

        Returns:
            None
        """

class Server:
    def getPlayerManager(self) -> PlayerManager:
        """
        Retrieves the player manager for the server.

        Returns:
            PlayerManager: The player manager object.
        """
    def getDefaultGameMode(self) -> GameMode:
        """
        Retrieves the default game mode for new players.

        Returns:
            GameMode: The default game mode.
        """
    def getForcedGameMode(self) -> GameMode:
        """
        Retrieves the forced game mode for all players.

        Returns:
            GameMode: The forced game mode.
        """
    def getScoreboard(self) -> Scoreboard:
        """
        Retrieves the scoreboard for the server.

        Returns:
            Scoreboard: The scoreboard object.
        """
    def getMaxWorldBorderRadius(self) -> int:
        """
        Retrieves the maximum radius of the world border.

        Returns:
            int: The maximum world border radius.
        """
    def getServerIP(self) -> str:
        """
        Retrieves the IP address of the server.

        Returns:
            str: The server IP address.
        """
    def getWorld(self, world: Worlds) -> World:
        """
        Retrieves the world object for the specified world type.

        Args:
            world (Worlds): The type of the world to retrieve.

        Returns:
            World: The world object.
        """
    def getServerMOTD(self) -> str:
        """
        Retrieves the MOTD (Message of the Day) of the server.

        Returns:
            str: The server MOTD.
        """
    def getServerPort(self) -> int:
        """
        Retrieves the port number on which the server is running.

        Returns:
            int: The server port number.
        """
    def getSpawnProtectionRadius(self) -> int:
        """
        Retrieves the radius of spawn protection around the world spawn point.

        Returns:
            int: The spawn protection radius.
        """
    def getSpawnRadius(self, world: Worlds) -> int:
        """
        Retrieves the spawn radius for the specified world type.

        Args:
            world (Worlds): The type of the world to retrieve the spawn radius for.

        Returns:
            int: The spawn radius of the world.
        """
    def getVersion(self) -> str:
        """
        Retrieves the version of the server.

        Returns:
            str: The server version.
        """
    def isFlightEnabled(self) -> bool:
        """
        Checks if flight is enabled on the server.

        Returns:
            bool: True if flight is enabled, False otherwise.
        """
    def isHardcore(self) -> bool:
        """
        Checks if the server is in hardcore mode.

        Returns:
            bool: True if the server is in hardcore mode, False otherwise.
        """
    def isMonsterSpawningEnabled(self) -> bool:
        """
        Checks if monster spawning is enabled on the server.

        Returns:
            bool: True if monster spawning is enabled, False otherwise.
        """
    def isNetherAllowed(self) -> bool:
        """
        Checks if the Nether dimension is allowed on the server.

        Returns:
            bool: True if the Nether is allowed, False otherwise.
        """
    def isPVPEnabled(self) -> bool:
        """
        Checks if PVP (Player vs. Player) is enabled on the server.

        Returns:
            bool: True if PVP is enabled, False otherwise.
        """
    def isSingleplayer(self) -> bool:
        """
        Checks if the server is running in singleplayer mode.

        Returns:
            bool: True if the server is in singleplayer mode, False otherwise.
        """
    def openToLAN(self, gameMode: GameModes, cheatsAllowed: bool, port: Number) -> None:
        """
        Opens the server to LAN (Local Area Network) with the specified settings.

        Args:
            gameMode (GameModes): The game mode for LAN players.
            cheatsAllowed (bool): Whether cheats are allowed for LAN players.
            port (Number): The port number to use for LAN connections.

        Returns:
            None
        """
    def setDefaultGameMode(self, defaultGameMode: GameModes) -> None:
        """
        Sets the default game mode for new players.

        Args:
            defaultGameMode (GameModes): The default game mode to set.

        Returns:
            None
        """
    def setDifficulty(self, difficulty: Difficulties) -> None:
        """
        Sets the difficulty level of the server.

        Args:
            difficulty (Difficulties): The difficulty level to set.

        Returns:
            None
        """
    def setDifficultyLocked(self, difficultyLocked: bool) -> None:
        """
        Sets whether the difficulty level is locked on the server.

        Args:
            difficultyLocked (bool): True to lock the difficulty level, False otherwise.

        Returns:
            None
        """

class StatusEffectInstance:
    duration: int
    amplifier: int

class StatusEffects:
    """
    Constants representing different status effects available in the game.
    These objects can be used to identify specific status effects.
    """

    SPEED: object
    SLOWNESS: object
    HASTE: object
    MINING_FATIGUE: object
    STRENGTH: object
    INSTANT_HEALTH: object
    INSTANT_DAMAGE: object
    JUMP_BOOST: object
    NAUSEA: object
    REGENERATION: object
    RESISTANCE: object
    FIRE_RESISTANCE: object
    WATER_BREATHING: object
    INVISIBILITY: object
    BLINDNESS: object
    NIGHT_VISION: object
    HUNGER: object
    WEAKNESS: object
    POISON: object
    WITHER: object
    HEALTH_BOOST: object
    ABSORPTION: object
    SATURATION: object
    GLOWING: object
    LEVITATION: object
    LUCK: object
    UNLUCK: object
    SLOW_FALLING: object
    CONDUIT_POWER: object
    DOLPHINS_GRACE: object
    BAD_OMEN: object
    HERO_OF_THE_VILLAGE: object
    DARKNESS: object

class Team:
    def setSuffix(self, suffix: Text) -> None:
        """
        Sets the suffix of the team.

        Args:
            suffix (Text): The suffix to set for the team.

        Returns:
            None
        """
    def setShowFriendlyInvisibles(self, showFriendlyInvisibles: bool) -> None:
        """
        Sets whether to show friendly invisibles for the team.

        Args:
            showFriendlyInvisibles (bool): A boolean value indicating whether to show friendly invisibles.

        Returns:
            None
        """
    def setPrefix(self, prefix: Text) -> None:
        """
        Sets the prefix of the team.

        Args:
            prefix (Text): The prefix to set for the team.

        Returns:
            None
        """
    def shouldShowFriendlyInvisibles(self) -> bool:
        """
        Checks if friendly invisibles are shown for the team.

        Returns:
            bool: True if friendly invisibles are shown, False otherwise.
        """
    def setNameTagVisibilityRule(self, nameTagVisibilityRule: VisibilityRules) -> None:
        """
        Sets the name tag visibility rule for the team.

        Args:
            nameTagVisibilityRule (VisibilityRules): The name tag visibility rule to set for the team.

        Returns:
            None
        """
    def setFriendlyFireAllowed(self, friendlyFireAllowed: bool) -> None:
        """
        Sets whether friendly fire is allowed for the team.

        Args:
            friendlyFireAllowed (bool): A boolean value indicating whether friendly fire is allowed.

        Returns:
            None
        """
    def setDisplayName(self, displayName: Text) -> None:
        """
        Sets the display name of the team.

        Args:
            displayName (Text): The display name to set for the team.

        Returns:
            None
        """
    def setDeathMessageVisibilityRule(
        self, deathMessageVisibilityRule: VisibilityRules
    ) -> None:
        """
        Sets the death message visibility rule for the team.

        Args:
            deathMessageVisibilityRule (VisibilityRules): The death message visibility rule to set for the team.

        Returns:
            None
        """
    def setColor(self, formatting: Formatting) -> None:
        """
        Sets the color of the team.

        Args:
            formatting (Formatting): The color formatting to set for the team.

        Returns:
            None
        """
    def setCollisionRule(self, collisionRule: CollisionRules) -> None:
        """
        Sets the collision rule for the team.

        Args:
            collisionRule (CollisionRules): The collision rule to set for the team.

        Returns:
            None
        """
    def isFriendlyFireAllowed(self) -> bool:
        """
        Checks if friendly fire is allowed for the team.

        Returns:
            bool: True if friendly fire is allowed, False otherwise.
        """
    def getSuffix(self) -> Text:
        """
        Returns the suffix of the team.

        Returns:
            Text: The suffix of the team.
        """
    def getPlayerList(self) -> list[str]:
        """
        Returns the list of players in the team.

        Returns:
            list[str]: The list of players in the team.
        """
    def getPrefix(self) -> Text:
        """
        Returns the prefix of the team.

        Returns:
            Text: The prefix of the team.
        """
    def getNameTagVisibilityRule(self) -> VisibilityRules:
        """
        Returns the name tag visibility rule of the team.

        Returns:
            VisibilityRules: The name tag visibility rule of the team.
        """
    def getName(self) -> str:
        """
        Returns the name of the team.

        Returns:
            str: The name of the team.
        """
    def getDisplayName(self) -> Text:
        """
        Returns the display name of the team.

        Returns:
            Text: The display name of the team.
        """
    def getDeathMessageVisibilityRule(self) -> VisibilityRules:
        """
        Returns the death message visibility rule of the team.

        Returns:
            VisibilityRules: The death message visibility rule of the team.
        """
    def getColor(self) -> Formatting:
        """
        Returns the color of the team.

        Returns:
            Formatting: The color of the team.
        """
    def getCollisionRule(self) -> CollisionRules:
        """
        Returns the collision rule of the team.

        Returns:
            CollisionRules: The collision rule of the team.
        """

class Time:
    """
    Represents different time values.
    """

    DAY: object
    MIDNIGHT: object
    NIGHT: object
    NOON: object

class Vec2f:
    """
    Represents a two-dimensional vector.

    Attributes:
        x (float): The x-coordinate of the vector.
        y (float): The y-coordinate of the vector.
    """

    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        """
        Initializes a Vec2f instance with the given coordinates.

        Args:
            x (float): The x-coordinate of the vector.
            y (float): The y-coordinate of the vector.
        """
        self.x = x
        self.y = y

class Vec3d:
    """
    Represents a three-dimensional vector.

    Attributes:
        x (float): The x-coordinate of the vector.
        y (float): The y-coordinate of the vector.
        z (float): The z-coordinate of the vector.
    """

    x: float
    y: float
    z: float

    def __init__(self, x: float, y: float, z: float) -> None:
        """
        Initializes a Vec3d instance with the given coordinates.

        Args:
            x (float): The x-coordinate of the vector.
            y (float): The y-coordinate of the vector.
            z (float): The z-coordinate of the vector.
        """
        self.x = x
        self.y = y
        self.z = z

class VisibilityRules:
    """
    Represents different visibility rules.
    """

    ALWAYS: object
    NEVER: object
    HIDE_FOR_OTHER_TEAMS: object
    HIDE_FOR_OWN_TEAM: object

class Weather:
    """
    Represents different weather conditions.
    """

    CLEAR: object
    RAIN: object
    THUNDER: object

class World:
    """
    Represents a world.
    """

    @overload
    def getBlock(self, x: Number, y: Number, z: Number) -> BlockState:
        """
        Retrieves the block state at the given coordinates.

        Args:
            x (Number): The x-coordinate of the block.
            y (Number): The y-coordinate of the block.
            z (Number): The z-coordinate of the block.

        Returns:
            BlockState: The block state at the given coordinates.
        """
    @overload
    def getBlock(self, blockPos: BlockPos) -> BlockState:
        """
        Retrieves the block state at the given block position.

        Args:
            blockPos (BlockPos): The block position.

        Returns:
            BlockState: The block state at the given block position.
        """
    def getDifficulty(self) -> Difficulty:
        """
        Retrieves the difficulty level of the world.

        Returns:
            Difficulty: The difficulty level of the world.
        """
    def getSeed(self) -> int:
        """
        Retrieves the seed value of the world.

        Returns:
            int: The seed value of the world.
        """
    @overload
    def setBlock(self, x: Number, y: Number, z: Number, block: Blocks) -> None:
        """
        Sets the block at the given coordinates.

        Args:
            x (Number): The x-coordinate of the block.
            y (Number): The y-coordinate of the block.
            z (Number): The z-coordinate of the block.
            block (Blocks): The block to be set.
        """
    @overload
    def setBlock(self, x: Number, y: Number, z: Number, block: BlockState) -> None:
        """
        Sets the block with the specified state at the given coordinates.

        Args:
            x (Number): The x-coordinate of the block.
            y (Number): The y-coordinate of the block.
            z (Number): The z-coordinate of the block.
            block (BlockState): The block state to be set.
        """
    @overload
    def setBlock(self, blockPos: BlockPos, block: Blocks) -> None:
        """
        Sets the block at the given block position.

        Args:
            blockPos (BlockPos): The block position.
            block (Blocks): The block to be set.
        """
    @overload
    def setBlock(self, blockPos: BlockPos, block: BlockState) -> None:
        """
        Sets the block with the specified state at the given block position.

        Args:
            blockPos (BlockPos): The block position.
            block (BlockState): The block state to be set.
        """
    @overload
    def setSpawnPos(self, x: Number, y: Number, z: Number) -> None:
        """
        Sets the spawn position of the world.

        Args:
            x (Number): The x-coordinate of the spawn position.
            y (Number): The y-coordinate of the spawn position.
            z (Number): The z-coordinate of the spawn position.
        """
    @overload
    def setSpawnPos(self, x: Number, y: Number, z: Number, angle: Number) -> None:
        """
        Sets the spawn position and angle of the world.

        Args:
            x (Number): The x-coordinate of the spawn position.
            y (Number): The y-coordinate of the spawn position.
            z (Number): The z-coordinate of the spawn position.
            angle (Number): The angle of the spawn position.
        """
    @overload
    def setSpawnPos(self, blockPos: BlockPos) -> None:
        """
        Sets the spawn position of the world using block position.

        Args:
            blockPos (BlockPos): The block position of the spawn position.
        """
    @overload
    def setSpawnPos(self, blockPos: BlockPos, angle: Number) -> None:
        """
        Sets the spawn position and angle of the world using block position.

        Args:
            blockPos (BlockPos): The block position of the spawn position.
            angle (Number): The angle of the spawn position.
        """
    def setTime(self, time: Time) -> None:
        """
        Sets the current time of the world.

        Args:
            time (Time): The time value to be set.
        """
    @overload
    def setWeather(self, weather: Weather) -> None:
        """
        Sets the weather condition of the world.

        Args:
            weather (Weather): The weather condition to be set.
        """
    @overload
    def setWeather(self, weather: Weather, duration: Number) -> None:
        """
        Sets the weather condition and duration of the world.

        Args:
            weather (Weather): The weather condition to be set.
            duration (Number): The duration of the weather condition.
        """
    @overload
    def spawnEntity(
        self, entity: Entities, x: Number, y: Number, z: Number, nbt: dict[str, object]
    ) -> None:
        """
        Spawns an entity at the specified coordinates.

        Args:
            entity (Entities): The type of entity to be spawned.
            x (Number): The x-coordinate of the entity's spawn location.
            y (Number): The y-coordinate of the entity's spawn location.
            z (Number): The z-coordinate of the entity's spawn location.
            nbt (dict[str, object]): Additional data for the entity (if applicable).
        """
    @overload
    def spawnEntity(
        self, entity: Entities, blockPos: BlockPos, nbt: dict[str, object]
    ) -> None:
        """
        Spawns an entity at the specified block position.

        Args:
            entity (Entities): The type of entity to be spawned.
            blockPos (BlockPos): The block position of the entity's spawn location.
            nbt (dict[str, object]): Additional data for the entity (if applicable).
        """

class Worlds:
    """
    Represents different game worlds.
    """

    OVERWORLD: object
    NETHER: object
    END: object

class PlayerManager:
    """
    Manages players in the game.
    """

    def areCheatsAllowed(self) -> bool:
        """
        Checks if cheats are allowed in the game.

        Returns:
            bool: True if cheats are allowed, False otherwise.
        """
    @overload
    def broadcast(self, message: str) -> None:
        """
        Broadcasts a message to all players.

        Args:
            message (str): The message to broadcast.
        """
    @overload
    def broadcast(self, text: Text) -> None:
        """
        Broadcasts a text component to all players.

        Args:
            text (Text): The text component to broadcast.
        """
    def disconnectAllPlayers(self) -> None:
        """
        Disconnects all players from the game.
        """
    def getCurrentPlayerCount(self) -> int:
        """
        Retrieves the current count of players in the game.

        Returns:
            int: The current count of players.
        """
    def getMaxPlayerCount(self) -> int:
        """
        Retrieves the maximum allowed count of players in the game.

        Returns:
            int: The maximum allowed count of players.
        """
    def getOpNames(self) -> list[str]:
        """
        Retrieves the names of all operators (ops) in the game.

        Returns:
            list[str]: The names of all operators.
        """
    def getPlayer(self, name: str) -> PlayerEntity:
        """
        Retrieves the player entity with the specified name.

        Args:
            name (str): The name of the player.

        Returns:
            PlayerEntity: The player entity.
        """
    def getPlayerList(self) -> list[PlayerEntity]:
        """
        Retrieves a list of all player entities in the game.

        Returns:
            list[PlayerEntity]: A list of player entities.
        """
    def getPlayerNames(self) -> list[str]:
        """
        Retrieves the names of all players in the game.

        Returns:
            list[str]: The names of all players.
        """
    def getViewDistance(self) -> int:
        """
        Retrieves the view distance setting of the game.

        Returns:
            int: The view distance.
        """
    def getWhitelistedNames(self) -> list[str]:
        """
        Retrieves the names of all whitelisted players in the game.

        Returns:
            list[str]: The names of all whitelisted players.
        """
    def isWhitelistEnabled(self) -> bool:
        """
        Checks if the whitelist is enabled in the game.

        Returns:
            bool: True if the whitelist is enabled, False otherwise.
        """
    def reloadWhitelist(self) -> None:
        """
        Reloads the whitelist configuration.
        """
    def setCheatsAllowed(self, cheatsAllowed: bool) -> None:
        """
        Sets whether cheats are allowed in the game.

        Args:
            cheatsAllowed (bool): True to allow cheats, False to disallow cheats.
        """
    def setSimulationDistance(self, simulationDistance: int) -> None:
        """
        Sets the simulation distance of the game.

        Args:
            simulationDistance (int): The simulation distance value.
        """
    def setViewDistance(self, viewDistance: int) -> None:
        """
        Sets the view distance of the game.

        Args:
            viewDistance (int): The view distance value.
        """
    def setWhitelistEnabled(self, whitelistEnabled: bool) -> None:
        """
        Sets whether the whitelist is enabled in the game.

        Args:
            whitelistEnabled (bool): True to enable the whitelist, False to disable the whitelist.
        """

class Formatting:
    """
    Text formatting
    """

    BLACK: object
    DARK_BLUE: object
    DARK_GREEN: object
    DARK_AQUA: object
    DARK_RED: object
    DARK_PURPLE: object
    GOLD: object
    GRAY: object
    DARK_GRAY: object
    BLUE: object
    GREEN: object
    AQUA: object
    RED: object
    LIGHT_PURPLE: object
    YELLOW: object
    WHITE: object
    OBFUSCATED: object
    BOLD: object
    STRIKETHROUGH: object
    UNDERLINE: object
    ITALIC: object
    RESET: object

class Text:
    message: str

    def __init__(self, message: str) -> None: ...
    def withFormatting(self, formatting: Formatting): ...

server: Server
executor: Executor
pythonMCVersion: str
pythonMCMajor: int
pythonMCMinor: int
pythonMCPatch: int
namespace: str
path: str
