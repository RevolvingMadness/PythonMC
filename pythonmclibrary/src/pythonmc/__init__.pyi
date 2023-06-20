from __future__ import annotations

from numbers import Number
from typing import overload


class Arm:
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
        ...


class BlockPos:
    x: int
    y: int
    z: int

    def __init__(self, x: Number, y: Number, z: Number) -> None: ...


class Blocks:
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
    block: Block

    def __init__(self, block: Blocks) -> None: ...

    def isOf(block: Block) -> bool: ...


class CollisionRules:
    ALWAYS: object
    NEVER: object
    PUSH_OTHER_TEAMS: object
    PUSH_OWN_TEAM: object


class DamageSources:
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
    EASY: object
    HARD: object
    NORMAL: object
    PEACEFUL: object


class Difficulty:
    name: str
    id: int
    info: str


class Enchantment:
    level: int
    rarity: EnchantmentRarity


class EnchantmentRarity:
    COMMON: object
    UNCOMMON: object
    RARE: object
    VERY_RARE: object


class Enchantments:
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
    stacks: list[ItemStack]


class Entities:
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
    def __init__(self, entity: Entities, world: World) -> None: ...

    def addVelocity(self, velocity: Vec3d) -> None: ...

    def canFreeze(self) -> bool: ...

    def canUsePortals(self) -> bool: ...

    def collidesWith(self, entity: Entity) -> bool: ...

    def damage(self, damageSource: DamageSources, amount: Number) -> None: ...

    def dismountVehicle(self) -> None: ...

    def distanceTo(self, entity: Entity) -> float: ...

    def extinguish(self) -> None: ...

    def extinguishWithSound(self) -> None: ...

    def getArmorItems(self) -> list[ItemStack]: ...

    def getBlockPos(self) -> BlockPos: ...

    def getCommandTags(self) -> list[str]: ...

    def getCustomName(self) -> str: ...

    def getDisplayName(self) -> str: ...

    def getHandItems(self) -> list[ItemStack]: ...

    def getName(self) -> str: ...

    def getPosition(self) -> Vec3d: ...

    def getVehicle(self) -> Entity: ...

    def getVelocity(self) -> Vec3d: ...

    def getX(self) -> float: ...

    def getY(self) -> float: ...

    def getZ(self) -> float: ...

    def hasCustomName(self) -> bool: ...

    def hasNoGravity(self) -> bool: ...

    def hasPassenger(self, entity: Entity) -> bool: ...

    def hasPassengers(self) -> bool: ...

    def hasPermissionLevel(self, level: Number) -> bool: ...

    def hasPortalCooldown(self) -> bool: ...

    def hasVehicle(self) -> bool: ...

    def isAlive(self) -> bool: ...

    def isCollidable(self) -> bool: ...

    def isCrawling(self) -> bool: ...

    def isCustomNameVisible(self) -> bool: ...

    def isDescending(self) -> bool: ...

    def isFireImmune(self) -> bool: ...

    def isGlowing(self) -> bool: ...

    def isInLava(self) -> bool: ...

    def isInRange(self, entity: Entity, range: Number) -> bool: ...

    def isInsideWall(self) -> bool: ...

    def isInsideWaterOrBubbleColumn(self) -> bool: ...

    def isInvisible(self) -> bool: ...

    def isLiving(self) -> bool: ...

    def isOnFire(self) -> bool: ...

    def isOnGround(self) -> bool: ...

    def isPlayer(self) -> bool: ...

    def isPushable(self) -> bool: ...

    def isSilent(self) -> bool: ...

    def isSneaking(self) -> bool: ...

    def isSpectator(self) -> bool: ...

    def isSprinting(self) -> bool: ...

    def isSubmergedInWater(self) -> bool: ...

    def isSwimming(self) -> bool: ...

    def isTouchingWater(self) -> bool: ...

    def isTouchingWaterOrRain(self) -> bool: ...

    def isWet(self) -> bool: ...

    def kill(self) -> None: ...

    def remove(self, reason: RemovalReasons) -> None: ...

    def removeAllPassengers(self) -> None: ...

    @overload
    def setCustomName(self, customName: str) -> None: ...

    @overload
    def setCustomName(self, text: Text) -> None: ...

    def setCustomNameVisible(self, customNameVisible: bool) -> None: ...

    def setFireTicks(self, fireTicks: Number) -> None: ...

    def setGlowing(self, glowing: bool) -> None: ...

    def setInPowderSnow(self, inPowderSnow: bool) -> None: ...

    def setInvisible(self, invisible: bool) -> None: ...

    def setNoGravity(self, noGravity: bool) -> None: ...

    def setOnFire(self, onFire: bool) -> None: ...

    def setOnFireFor(self, seconds: Number) -> None: ...

    def setOnFireFromLava(self) -> None: ...

    def setOnGround(self, onGround: bool) -> None: ...

    def setPosition(self, position: Vec3d) -> None: ...

    def setSilent(self, silent: bool) -> None: ...

    def setSneaking(self, sneaking: bool) -> None: ...

    def setSprinting(self, sprinting: bool) -> None: ...

    def setVelocity(self, velocity: Vec3d) -> None: ...

    def shouldDismountUnderwater(self) -> bool: ...

    def shouldRenderName(self) -> bool: ...

    def startRiding(self, entity: Entity) -> None: ...

    def stopRiding(self) -> None: ...

    def teleport(self, position: Vec3d) -> None: ...


class Executor:
    name: str
    displayName: str
    position: Vec3d
    player: PlayerEntity
    world: World
    entity: Entity
    isExecutedByPlayer: bool
    rotation: Vec2f

    @overload
    def sendMessage(message) -> None: ...

    @overload
    def sendMessage(text: Text) -> None: ...

    @overload
    def sendError(error) -> None: ...

    @overload
    def sendError(text: Text) -> None: ...


class GameMode:
    id: int
    name: str
    SURVIVAL: GameMode
    CREATIVE: GameMode
    ADVENTURE: GameMode
    SPECTATOR: GameMode


class GameModes:
    SURVIVAL: object
    CREATIVE: object
    ADVENTURE: object
    SPECTATOR: object


class Hand:
    MAIN_HAND: object
    OFF_HAND: object


class HideFlags:
    ENCHANTMENTS: object
    MODIFIERS: object
    UNBREAKABLE: object
    CAN_DESTROY: object
    CAN_PLACE: object
    ADDITIONAL: object
    DYE: object
    UPGRADES: object


class HungerManager:
    exhaustion: float
    foodLevel: int
    saturationLevel: float


class Item:
    name: str

    def __init__(self, item: Items) -> None: ...


class ItemRarity:
    COMMON: object
    UNCOMMON: object
    RARE: object
    EPIC: object


class Items:
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
    @overload
    def __init__(self, item: Items, count: Number, nbt: dict[str, object]) -> None: ...

    @overload
    def __init__(self, item: Items, nbt: dict[str, object]) -> None: ...

    @overload
    def __init__(self, item: Items, count: Number) -> None: ...

    @overload
    def __init__(self, item: Items) -> None: ...

    def addEnchantment(self, enchantment: Enchantments, level: Number) -> None: ...

    def addHideFlag(self, hideFlag: HideFlags) -> None: ...

    def decrement(self, amount: Number) -> None: ...

    def getCount(self) -> int: ...

    def getDamage(self) -> int: ...

    def getEnchantments(self) -> list[Enchantment]: ...

    def getMaxCount(self) -> int: ...

    def getMaxDamage(self) -> int: ...

    def getName(self) -> str: ...

    def getNbt(self) -> dict[str, object]: ...

    def getRarity(self) -> ItemRarity: ...

    def getRepairCost(self) -> int: ...

    def hasCustomName(self) -> bool: ...

    def hasEnchantments(self) -> bool: ...

    def hasGlint(self) -> bool: ...

    def hasNbt(self) -> bool: ...

    def increment(self, amount: Number) -> None: ...

    def isDamageable(self) -> bool: ...

    def isDamaged(self) -> bool: ...

    def isEnchantable(self) -> bool: ...

    def isFood(self) -> bool: ...

    def isItemBarVisible(self) -> bool: ...

    def isStackable(self) -> bool: ...

    def removeCustomName(self) -> None: ...

    def setCount(self, count: Number) -> None: ...

    @overload
    def setCustomName(self, customName: str) -> None: ...

    @overload
    def setCustomName(self, text: Text) -> None: ...

    def setDamage(self, damage: Number) -> None: ...

    def setRepairCost(self, repairCost: Number) -> None: ...


class LivingEntity(Entity):
    def addStatusEffect(
            self, effect: StatusEffects, duration: Number, amplifier: Number, visible: bool
    ) -> None: ...

    def canBreatheInWater(self) -> bool: ...

    def canHaveStatusEffect(self, effect: StatusEffects) -> bool: ...

    def canSee(self, entity: Entity) -> bool: ...

    def canTakeDamage(self) -> bool: ...

    def clearStatusEffects(self) -> None: ...

    def damageArmor(self, damageSource: DamageSources, amount: Number) -> None: ...

    def damageHelmet(self, damageSource: DamageSources, amount: Number) -> None: ...

    def damageShield(self, amount: Number) -> None: ...

    def eatFood(self, stack: ItemStack) -> None: ...

    def getAbsorptionAmount(self) -> float: ...

    def getActiveHand(self) -> Hand: ...

    def getActiveItem(self) -> ItemStack: ...

    def getArmor(self) -> float: ...

    def getAttacker(self) -> LivingEntity: ...

    def getAttacking(self) -> LivingEntity: ...

    def getMainArm(self) -> Arm: ...

    def getMainHandStack(self) -> ItemStack: ...

    def getMaxHealth(self) -> float: ...

    def getMovementSpeed(self) -> float: ...

    def getScaleFactor(self) -> float: ...

    def getStackInHand(self, hand: Hand) -> ItemStack: ...

    def getStatusEffect(self, effect: StatusEffects) -> StatusEffectInstance: ...

    def getStatusEffects(self) -> list[StatusEffectInstance]: ...

    def getStuckArrowCount(self) -> float: ...

    def hasStatusEffect(self, effect: StatusEffects) -> bool: ...

    def heal(self, amount: Number) -> None: ...

    def getHealth(self) -> float: ...

    def isAffectedBySplashPotions(self) -> bool: ...

    def isBaby(self) -> bool: ...

    def isBlocking(self) -> bool: ...

    def isClimbing(self) -> bool: ...

    def isDead(self) -> bool: ...

    def isFallFlying(self) -> bool: ...

    def isHolding(self, item: Item) -> bool: ...

    def isHoldingOntoLadder(self) -> bool: ...

    def isHurtByWater(self) -> bool: ...

    def isMobOrPlayer(self) -> bool: ...

    def isSleeping(self) -> bool: ...

    def isUndead(self) -> bool: ...

    def isUsingItem(self) -> bool: ...

    def isUsingRiptide(self) -> bool: ...

    def removeStatusEffect(self, effect: StatusEffects) -> None: ...

    def setAbsorptionAmount(self, amount: Number) -> None: ...

    def setAttacker(self, entity: LivingEntity) -> None: ...

    def setAttacking(self, entity: LivingEntity) -> None: ...

    def setCurrentHand(self, hand: Hand) -> None: ...

    def setHealth(self, amount: Number) -> None: ...

    def setJumping(self, jumping: bool) -> None: ...

    def setMovementSpeed(self, movementSpeed: Number) -> None: ...

    def setStackInHand(self, hand: Hand, stack: ItemStack) -> None: ...

    def setStingerCount(self, stingerCount: Number) -> None: ...

    def setStuckArrowCount(self, stuckArrowCount: Number) -> None: ...

    def shouldDisplaySoulSpeedEffects(self) -> bool: ...

    def shouldDropXp(self) -> bool: ...

    def swingHand(self, hand: Hand) -> None: ...

    def takeKnockback(self, strength: Number, x: Number, z: Number) -> None: ...

    def teleport(self, position: Vec3d) -> None: ...

    def tiltScreen(self, deltaX: Number, deltaY: Number) -> None: ...


class PlayerEntity(LivingEntity):
    def addExhaustion(self, exhaustion: Number) -> None: ...

    def addExperience(self, experience: Number) -> None: ...

    def addExperienceLevels(self, levels: Number) -> None: ...

    def addScore(self, score: Number) -> None: ...

    def addShoulderEntity(self, entityNbt: dict[str, object]) -> None: ...

    def attack(self, entity: Entity) -> None: ...

    def canConsume(self, ignoreHunger: bool) -> bool: ...

    def canFoodHeal(self) -> bool: ...

    @overload
    def canHarvest(self, block: Blocks) -> bool: ...

    @overload
    def canHarvest(self, block: BlockState) -> bool: ...

    def checkFallFlying(self) -> bool: ...

    def disableShield(self, sprinting: bool) -> None: ...

    def getAttackCooldownProgress(self, baseTime: Number) -> float: ...

    def getEnderChestInventory(self) -> EnderChestInventory: ...

    def getHungerManager(self) -> HungerManager: ...

    def getInventory(self) -> PlayerInventory: ...

    def getShoulderEntityLeft(self) -> dict[str, object]: ...

    def getShoulderEntityRight(self) -> dict[str, object]: ...

    def isCreative(self) -> bool: ...

    def isMainPlayer(self) -> bool: ...

    def isUsingSglass(self) -> bool: ...

    def requestRespawn(self) -> None: ...

    @overload
    def sendMessage(self, message) -> None: ...

    @overload
    def sendMessage(self, text: Text) -> None: ...

    def setMainArm(self, arm: Arm) -> None: ...


class PlayerInventory:
    main: list[ItemStack]
    armor: list[ItemStack]
    offHand: list[ItemStack]
    selectedSlot: int

    def clear(self) -> None: ...

    def contains(self, stack: ItemStack) -> bool: ...

    def dropAll(self) -> None: ...

    def dropSelectedItem(self, entireStack: bool) -> None: ...

    def getArmorStack(self, slot: Number) -> ItemStack: ...

    def getEmptySlot(self) -> int: ...

    def getMainHandStack(self) -> ItemStack: ...

    def getSlotWithStack(self, stack: ItemStack) -> int: ...

    def getStack(self, slot: Number) -> ItemStack: ...

    def indexOf(self, stack: ItemStack) -> ItemStack: ...

    @overload
    def insertStack(self, slot: Number, stack: ItemStack) -> None: ...

    @overload
    def insertStack(self, stack: ItemStack) -> None: ...

    def isEmpty(self) -> bool: ...

    def removeOne(self, stack: ItemStack) -> None: ...

    @overload
    def removeStack(self, slot: Number, amount: Number) -> None: ...

    @overload
    def removeStack(self, slot: Number) -> None: ...

    def setStack(self, slot: Number, stack: ItemStack) -> None: ...


class RemovalReasons:
    KILLED: object
    DISCARDED: object
    UNLOADED_TO_CHUNK: object
    UNLOADED_WITH_PLAYER: object
    CHANGED_DIMENSION: object


class RenderTypes:
    INTEGER: object
    HEARTS: object


class Scoreboard:
    scoreboard: Scoreboard

    def __init__(self, scoreboard: Scoreboard):
        self.scoreboard: object

    def getTeams(self) -> list[Team]: ...

    def resetPlayerScore(
            self, playerName: str, objective: ScoreboardObjective
    ) -> None: ...

    def getAllPlayerScores(
            self, objective: ScoreboardObjective
    ) -> list[ScoreboardPlayerScore]: ...

    def removeTeam(self, team: Team) -> None: ...

    def containsObjective(self, name: str) -> bool: ...

    def addObjective(
            self,
            name: str,
            criterion: ScoreboardCriterions,
            displayName: Text,
            renderType: RenderTypes,
    ) -> None: ...

    def removePlayerFromTeam(self, playerName: str, team: Team) -> None: ...

    def getObjectives(self) -> list[ScoreboardObjective]: ...

    def addPlayerToTeam(self, playerName: str, team: Team) -> None: ...

    def clearPlayerTeam(self, playerName: str) -> None: ...

    def getObjectiveNames(self) -> list[str]: ...

    def getTeam(self, name: str) -> Team: ...

    def resetEntityScore(self, entity: Entity) -> None: ...

    def getObjective(self, name: str) -> ScoreboardObjective: ...

    def addTeam(self, name: str) -> None: ...

    def getTeamNames(self) -> list[str]: ...

    def removeObjective(self, objective: ScoreboardObjective) -> None: ...

    def getPlayerScore(
            self, name: str, objective: ScoreboardObjective
    ) -> ScoreboardPlayerScore: ...

    def getPlayerTeam(self, name: str) -> Team: ...


class ScoreboardCriterions:
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
    def getCriterion(self) -> ScoreboardCriterions: ...

    def getDisplayName(self) -> Text: ...

    def getName(self) -> str: ...

    def getRenderType(self) -> RenderTypes: ...

    def setDisplayName(self, displayName: Text) -> None: ...

    def setRenderType(self, renderType: RenderTypes) -> None: ...


class ScoreboardPlayerScore:
    def clearScore(self) -> None: ...

    def getPlayerName(self) -> str: ...

    def getScore(self) -> int: ...

    def getScoreboard(self) -> Scoreboard: ...

    def incrementScore(self) -> None: ...

    def incrementScore(self, amount: Number) -> None: ...

    def setScore(self, score: Number) -> None: ...


class Server:
    def getPlayerManager(self) -> PlayerManager: ...

    def getDefaultGameMode(self) -> GameMode: ...

    def getForcedGameMode(self) -> GameMode: ...

    def getScoreboard(self) -> Scoreboard: ...

    def getMaxWorldBorderRadius(self) -> int: ...

    def getServerIP(self) -> str: ...

    def getWorld(self, world: Worlds) -> World: ...

    def getServerMOTD(self) -> str: ...

    def getServerPort(self) -> int: ...

    def getSpawnProtectionRadius(self) -> int: ...

    def getSpawnRadius(self, world: Worlds) -> int: ...

    def getVersion(self) -> str: ...

    def isFlightEnabled(self) -> bool: ...

    def isHardcore(self) -> bool: ...

    def isMonsterSpawningEnabled(self) -> bool: ...

    def isNetherAllowed(self) -> bool: ...

    def isPVPEnabled(self) -> bool: ...

    def isSingleplayer(self) -> bool: ...

    def openToLAN(
            self, gameMode: GameModes, cheatsAllowed: bool, port: Number
    ) -> None: ...

    def setDefaultGameMode(self, defaultGameMode: GameModes) -> None: ...

    def setDifficulty(self, difficulty: Difficulties) -> None: ...

    def setDifficultyLocked(self, difficultyLocked: bool) -> None: ...


class StatusEffectInstance:
    duration: int
    amplifier: int


class StatusEffects:
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
    def setSuffix(self, suffix: Text) -> None: ...

    def setShowFriendlyInvisibles(self, showFriendlyInvisibles: bool) -> None: ...

    def setPrefix(self, prefix: Text) -> None: ...

    def shouldShowFriendlyInvisibles(self) -> bool: ...

    def setNameTagVisibilityRule(
            self, nameTagVisibilityRule: VisibilityRules
    ) -> None: ...

    def setFriendlyFireAllowed(self, friendlyFireAllowed: bool) -> None: ...

    def setDisplayName(self, displayName: Text) -> None: ...

    def setDeathMessageVisibilityRule(
            self, deathMessageVisibilityRule: VisibilityRules
    ) -> None: ...

    def setColor(self, formatting: Formatting) -> None: ...

    def setCollisionRule(self, collisionRule: CollisionRules) -> None: ...

    def isFriendlyFireAllowed(self) -> bool: ...

    def getSuffix(self) -> Text: ...

    def getPlayerList(self) -> list[str]: ...

    def getPrefix(self) -> Text: ...

    def getNameTagVisibilityRule(self) -> VisibilityRules: ...

    def getName(self) -> str: ...

    def getDisplayName(self) -> Text: ...

    def getDeathMessageVisibilityRule(self) -> VisibilityRules: ...

    def getColor(self) -> Formatting: ...

    def getCollisionRule(self) -> CollisionRules: ...


class Time:
    DAY: object
    MIDNIGHT: object
    NIGHT: object
    NOON: object


class Vec2f:
    x: float
    y: float

    def __init__(self, x: Number, y: Number) -> None: ...


class Vec3d:
    x: float
    y: float
    z: float

    def __init__(self, x: Number, y: Number, z: Number) -> None: ...


class VisibilityRules:
    ALWAYS: object
    NEVER: object
    HIDE_FOR_OTHER_TEAMS: object
    HIDE_FOR_OWN_TEAM: object


class Weather:
    CLEAR: object
    RAIN: object
    THUNDER: object


class World:
    @overload
    def getBlock(self, x: Number, y: Number, z: Number) -> BlockState: ...

    @overload
    def getBlock(self, blockPos: BlockPos) -> BlockState: ...

    def getDifficulty(self) -> Difficulty: ...

    def getSeed(self) -> int: ...

    @overload
    def setBlock(self, x: Number, y: Number, z: Number, block: Blocks) -> None: ...

    @overload
    def setBlock(self, x: Number, y: Number, z: Number, block: BlockState) -> None: ...

    @overload
    def setBlock(self, blockPos: BlockPos, block: Blocks) -> None: ...

    @overload
    def setBlock(self, blockPos: BlockPos, block: BlockState) -> None: ...

    @overload
    def setSpawnPos(self, x: Number, y: Number, z: Number) -> None: ...

    @overload
    def setSpawnPos(self, x: Number, y: Number, z: Number, angle: Number) -> None: ...

    @overload
    def setSpawnPos(self, blockPos: BlockPos) -> None: ...

    @overload
    def setSpawnPos(self, blockPos: BlockPos, angle: Number) -> None: ...

    def setTime(self, time: Time) -> None: ...

    @overload
    def setWeather(self, weather: Weather) -> None: ...

    @overload
    def setWeather(self, weather: Weather, duration: Number) -> None: ...

    @overload
    def spawnEntity(
            self, entity: Entities, x: Number, y: Number, z: Number, nbt: dict[str, object]
    ) -> None: ...

    @overload
    def spawnEntity(
            self, entity: Entities, blockPos: BlockPos, nbt: dict[str, object]
    ) -> None: ...


class Worlds:
    OVERWORLD: object
    NETHER: object
    END: object


class PlayerManager:
    def areCheatsAllowed(self) -> bool: ...

    @overload
    def broadcast(self, message: str) -> None: ...

    @overload
    def broadcast(self, text: Text) -> None: ...

    def disconnectAllPlayers(self) -> None: ...

    def getCurrentPlayerCount(self) -> int: ...

    def getMaxPlayerCount(self) -> int: ...

    def getOpNames(self) -> list[str]: ...

    def getPlayer(self, name: str) -> PlayerEntity: ...

    def getPlayerList(self) -> list[PlayerEntity]: ...

    def getPlayerNames(self) -> list[str]: ...

    def getViewDistance(self) -> int: ...

    def getWhitelistedNames(self) -> list[str]: ...

    def isWhitelistEnabled(self) -> bool: ...

    def reloadWhitelist(self) -> None: ...

    def setCheatsAllowed(self, cheatsAllowed: bool) -> None: ...

    def setSimulationDistance(self, simulationDistance: int) -> None: ...

    def setViewDistance(self, viewDistance: int) -> None: ...

    def setWhitelistEnabled(self, whitelistEnabled: bool) -> None: ...


class Formatting:
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
thonMCVersion: str
thonMCMajor: int
thonMCMinor: int
thonMCPatch: int
namespace: str
path: str
