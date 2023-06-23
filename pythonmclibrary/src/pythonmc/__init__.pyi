from __future__ import annotations

from block.block import Block
from block.block_pos import BlockPos
from block.block_state import BlockState
from block.blocks import Blocks

from entity.effects.status_effect_instance import StatusEffectInstance
from entity.effects.status_effects import StatusEffects
from entity.arm import Arm
from entity.damage_sources import DamageSources
from entity.entities import Entities
from entity.entity import Entity
from entity.hand import Hand
from entity.living_entity import LivingEntity
from entity.removal_reasons import RemovalReasons

from item.enchantment.enchantment import Enchantment
from item.enchantment.enchantment_rarity import EnchantmentRarity
from item.enchantment.enchantments import Enchantments
from item.hide_flags import HideFlags
from item.item import Item
from item.item_rarity import ItemRarity
from item.item_stack import ItemStack
from item.items import Items

from player.ender_chest_inventory import EnderChestInventory
from player.hunger_manager import HungerManager
from player.player_entity import PlayerEntity
from player.player_inventory import PlayerInventory
from player.player_manager import PlayerManager

from scoreboard.rules.collision_rules import CollisionRules
from scoreboard.rules.visibility_rules import VisibilityRules
from scoreboard.render_types import RenderTypes
from scoreboard.scoreboard import Scoreboard
from scoreboard.scoreboard_criterions import ScoreboardCriterions
from scoreboard.scoreboard_objective import ScoreboardObjective
from scoreboard.scoreboard_player_score import ScoreboardPlayerScore
from scoreboard.team import Team

from server.difficulty.difficulties import Difficulties
from server.difficulty.difficulty import Difficulty
from server.gamemode.game_mode import GameMode
from server.gamemode.game_modes import GameModes
from server.text.formatting import Formatting
from server.text.text import Text
from server.server import Server

from world.position.vec2f import Vec2f
from world.position.vec3d import Vec3d
from world.executor import Executor
from world.particles import Particles
from world.time import Time
from world.weather import Weather
from world.world import World
from world.worlds import Worlds

server: Server
executor: Executor
pythonMCVersion: str
pythonMCMajor: int
pythonMCMinor: int
pythonMCPatch: int
namespace: str
path: str
