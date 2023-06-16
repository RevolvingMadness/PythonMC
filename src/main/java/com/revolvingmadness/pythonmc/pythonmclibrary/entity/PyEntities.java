package com.revolvingmadness.pythonmc.pythonmclibrary.entity;

import net.minecraft.entity.EntityType;

public enum PyEntities {
	ALLAY, AREA_EFFECT_CLOUD, ARMOR_STAND, ARROW, AXOLOTL, BAT, BEE, BLAZE, BLOCK_DISPLAY, BOAT, CAMEL, CAT, CAVE_SPIDER, CHEST_BOAT, CHEST_MINECART, CHICKEN, COD, COMMAND_BLOCK_MINECART, COW, CREEPER, DOLPHIN, DONKEY, DRAGON_FIREBALL, DROWNED, EGG, ELDER_GUARDIAN, END_CRYSTAL, ENDER_DRAGON, ENDER_PEARL, ENDERMAN, ENDERMITE, EVOKER, EVOKER_FANGS, EXPERIENCE_BOTTLE, EXPERIENCE_ORB, EYE_OF_ENDER, FALLING_BLOCK, FIREWORK_ROCKET, FOX, FROG, FURNACE_MINECART, GHAST, GIANT, GLOW_ITEM_FRAME, GLOW_SQUID, GOAT, GUARDIAN, HOGLIN, HOPPER_MINECART, HORSE, HUSK, ILLUSIONER, INTERACTION, IRON_GOLEM, ITEM, ITEM_DISPLAY, ITEM_FRAME, FIREBALL, LEASH_KNOT, LIGHTNING_BOLT, LLAMA, LLAMA_SPIT, MAGMA_CUBE, MARKER, MINECART, MOOSHROOM, MULE, OCELOT, PAINTING, PANDA, PARROT, PHANTOM, PIG, PIGLIN, PIGLIN_BRUTE, PILLAGER, POLAR_BEAR, POTION, PUFFERFISH, RABBIT, RAVAGER, SALMON, SHEEP, SHULKER, SHULKER_BULLET, SILVERFISH, SKELETON, SKELETON_HORSE, SLIME, SMALL_FIREBALL, SNIFFER, SNOW_GOLEM, SNOWBALL, SPAWNER_MINECART, SPECTRAL_ARROW, SPIDER, SQUID, STRAY, STRIDER, TADPOLE, TEXT_DISPLAY, TNT, TNT_MINECART, TRADER_LLAMA, TRIDENT, TROPICAL_FISH, TURTLE, VEX, VILLAGER, VINDICATOR, WANDERING_TRADER, WARDEN, WITCH, WITHER, WITHER_SKELETON, WITHER_SKULL, WOLF, ZOGLIN, ZOMBIE, ZOMBIE_HORSE, ZOMBIE_VILLAGER, ZOMBIFIED_PIGLIN, PLAYER, FISHING_BOBBER;

	public EntityType<?> toEntityType() {
		return switch (this) {
			case ALLAY -> EntityType.ALLAY;
			case AREA_EFFECT_CLOUD -> EntityType.AREA_EFFECT_CLOUD;
			case ARMOR_STAND -> EntityType.ARMOR_STAND;
			case ARROW -> EntityType.ARROW;
			case AXOLOTL -> EntityType.AXOLOTL;
			case BAT -> EntityType.BAT;
			case BEE -> EntityType.BEE;
			case BLAZE -> EntityType.BLAZE;
			case BLOCK_DISPLAY -> EntityType.BLOCK_DISPLAY;
			case BOAT -> EntityType.BOAT;
			case CAMEL -> EntityType.CAMEL;
			case CAT -> EntityType.CAT;
			case CAVE_SPIDER -> EntityType.CAVE_SPIDER;
			case CHEST_BOAT -> EntityType.CHEST_BOAT;
			case CHEST_MINECART -> EntityType.CHEST_MINECART;
			case CHICKEN -> EntityType.CHICKEN;
			case COD -> EntityType.COD;
			case COMMAND_BLOCK_MINECART -> EntityType.COMMAND_BLOCK_MINECART;
			case COW -> EntityType.COW;
			case CREEPER -> EntityType.CREEPER;
			case DOLPHIN -> EntityType.DOLPHIN;
			case DONKEY -> EntityType.DONKEY;
			case DRAGON_FIREBALL -> EntityType.DRAGON_FIREBALL;
			case DROWNED -> EntityType.DROWNED;
			case EGG -> EntityType.EGG;
			case ELDER_GUARDIAN -> EntityType.ELDER_GUARDIAN;
			case END_CRYSTAL -> EntityType.END_CRYSTAL;
			case ENDER_DRAGON -> EntityType.ENDER_DRAGON;
			case ENDER_PEARL -> EntityType.ENDER_PEARL;
			case ENDERMAN -> EntityType.ENDERMAN;
			case ENDERMITE -> EntityType.ENDERMITE;
			case EVOKER -> EntityType.EVOKER;
			case EVOKER_FANGS -> EntityType.EVOKER_FANGS;
			case EXPERIENCE_BOTTLE -> EntityType.EXPERIENCE_BOTTLE;
			case EXPERIENCE_ORB -> EntityType.EXPERIENCE_ORB;
			case EYE_OF_ENDER -> EntityType.EYE_OF_ENDER;
			case FALLING_BLOCK -> EntityType.FALLING_BLOCK;
			case FIREWORK_ROCKET -> EntityType.FIREWORK_ROCKET;
			case FOX -> EntityType.FOX;
			case FROG -> EntityType.FROG;
			case FURNACE_MINECART -> EntityType.FURNACE_MINECART;
			case GHAST -> EntityType.GHAST;
			case GIANT -> EntityType.GIANT;
			case GLOW_ITEM_FRAME -> EntityType.GLOW_ITEM_FRAME;
			case GLOW_SQUID -> EntityType.GLOW_SQUID;
			case GOAT -> EntityType.GOAT;
			case GUARDIAN -> EntityType.GUARDIAN;
			case HOGLIN -> EntityType.HOGLIN;
			case HOPPER_MINECART -> EntityType.HOPPER_MINECART;
			case HORSE -> EntityType.HORSE;
			case HUSK -> EntityType.HUSK;
			case ILLUSIONER -> EntityType.ILLUSIONER;
			case INTERACTION -> EntityType.INTERACTION;
			case IRON_GOLEM -> EntityType.IRON_GOLEM;
			case ITEM -> EntityType.ITEM;
			case ITEM_DISPLAY -> EntityType.ITEM_DISPLAY;
			case ITEM_FRAME -> EntityType.ITEM_FRAME;
			case FIREBALL -> EntityType.FIREBALL;
			case LEASH_KNOT -> EntityType.LEASH_KNOT;
			case LIGHTNING_BOLT -> EntityType.LIGHTNING_BOLT;
			case LLAMA -> EntityType.LLAMA;
			case LLAMA_SPIT -> EntityType.LLAMA_SPIT;
			case MAGMA_CUBE -> EntityType.MAGMA_CUBE;
			case MARKER -> EntityType.MARKER;
			case MINECART -> EntityType.MINECART;
			case MOOSHROOM -> EntityType.MOOSHROOM;
			case MULE -> EntityType.MULE;
			case OCELOT -> EntityType.OCELOT;
			case PAINTING -> EntityType.PAINTING;
			case PANDA -> EntityType.PANDA;
			case PARROT -> EntityType.PARROT;
			case PHANTOM -> EntityType.PHANTOM;
			case PIG -> EntityType.PIG;
			case PIGLIN -> EntityType.PIGLIN;
			case PIGLIN_BRUTE -> EntityType.PIGLIN_BRUTE;
			case PILLAGER -> EntityType.PILLAGER;
			case POLAR_BEAR -> EntityType.POLAR_BEAR;
			case POTION -> EntityType.POTION;
			case PUFFERFISH -> EntityType.PUFFERFISH;
			case RABBIT -> EntityType.RABBIT;
			case RAVAGER -> EntityType.RAVAGER;
			case SALMON -> EntityType.SALMON;
			case SHEEP -> EntityType.SHEEP;
			case SHULKER -> EntityType.SHULKER;
			case SHULKER_BULLET -> EntityType.SHULKER_BULLET;
			case SILVERFISH -> EntityType.SILVERFISH;
			case SKELETON -> EntityType.SKELETON;
			case SKELETON_HORSE -> EntityType.SKELETON_HORSE;
			case SLIME -> EntityType.SLIME;
			case SMALL_FIREBALL -> EntityType.SMALL_FIREBALL;
			case SNIFFER -> EntityType.SNIFFER;
			case SNOW_GOLEM -> EntityType.SNOW_GOLEM;
			case SNOWBALL -> EntityType.SNOWBALL;
			case SPAWNER_MINECART -> EntityType.SPAWNER_MINECART;
			case SPECTRAL_ARROW -> EntityType.SPECTRAL_ARROW;
			case SPIDER -> EntityType.SPIDER;
			case SQUID -> EntityType.SQUID;
			case STRAY -> EntityType.STRAY;
			case STRIDER -> EntityType.STRIDER;
			case TADPOLE -> EntityType.TADPOLE;
			case TEXT_DISPLAY -> EntityType.TEXT_DISPLAY;
			case TNT -> EntityType.TNT;
			case TNT_MINECART -> EntityType.TNT_MINECART;
			case TRADER_LLAMA -> EntityType.TRADER_LLAMA;
			case TRIDENT -> EntityType.TRIDENT;
			case TROPICAL_FISH -> EntityType.TROPICAL_FISH;
			case TURTLE -> EntityType.TURTLE;
			case VEX -> EntityType.VEX;
			case VILLAGER -> EntityType.VILLAGER;
			case VINDICATOR -> EntityType.VINDICATOR;
			case WANDERING_TRADER -> EntityType.WANDERING_TRADER;
			case WARDEN -> EntityType.WARDEN;
			case WITCH -> EntityType.WITCH;
			case WITHER -> EntityType.WITHER;
			case WITHER_SKELETON -> EntityType.WITHER_SKELETON;
			case WITHER_SKULL -> EntityType.WITHER_SKULL;
			case WOLF -> EntityType.WOLF;
			case ZOGLIN -> EntityType.ZOGLIN;
			case ZOMBIE -> EntityType.ZOMBIE;
			case ZOMBIE_HORSE -> EntityType.ZOMBIE_HORSE;
			case ZOMBIE_VILLAGER -> EntityType.ZOMBIE_VILLAGER;
			case ZOMBIFIED_PIGLIN -> EntityType.ZOMBIFIED_PIGLIN;
			case PLAYER -> EntityType.PLAYER;
			case FISHING_BOBBER -> EntityType.FISHING_BOBBER;
		};
	}
}