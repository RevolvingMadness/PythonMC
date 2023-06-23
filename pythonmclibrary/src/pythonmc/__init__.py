from __future__ import annotations

from pythonmc.block.block import Block
from pythonmc.block.block_pos import BlockPos
from pythonmc.block.block_state import BlockState
from pythonmc.block.blocks import Blocks
from pythonmc.entity.arm import Arm
from pythonmc.entity.damage_sources import DamageSources
from pythonmc.entity.effects.status_effect_instance import StatusEffectInstance
from pythonmc.entity.effects.status_effects import StatusEffects
from pythonmc.entity.entities import Entities
from pythonmc.entity.entity import Entity
from pythonmc.entity.hand import Hand
from pythonmc.entity.living_entity import LivingEntity
from pythonmc.entity.removal_reasons import RemovalReasons
from pythonmc.item.enchantment.enchantment import Enchantment
from pythonmc.item.enchantment.enchantment_rarity import EnchantmentRarity
from pythonmc.item.enchantment.enchantments import Enchantments
from pythonmc.item.hide_flags import HideFlags
from pythonmc.item.item import Item
from pythonmc.item.item_rarity import ItemRarity
from pythonmc.item.item_stack import ItemStack
from pythonmc.item.items import Items
from pythonmc.player.ender_chest_inventory import EnderChestInventory
from pythonmc.player.hunger_manager import HungerManager
from pythonmc.player.player_entity import PlayerEntity
from pythonmc.player.player_inventory import PlayerInventory
from pythonmc.player.player_manager import PlayerManager
from pythonmc.scoreboard.render_types import RenderTypes
from pythonmc.scoreboard.rules.collision_rules import CollisionRules
from pythonmc.scoreboard.rules.visibility_rules import VisibilityRules
from pythonmc.scoreboard.scoreboard import Scoreboard
from pythonmc.scoreboard.scoreboard_criterions import ScoreboardCriterions
from pythonmc.scoreboard.scoreboard_objective import ScoreboardObjective
from pythonmc.scoreboard.scoreboard_player_score import ScoreboardPlayerScore
from pythonmc.scoreboard.team import Team
from pythonmc.server.difficulty.difficulties import Difficulties
from pythonmc.server.difficulty.difficulty import Difficulty
from pythonmc.server.gamemode.game_mode import GameMode
from pythonmc.server.gamemode.game_modes import GameModes
from pythonmc.server.server import Server
from pythonmc.server.text.formatting import Formatting
from pythonmc.server.text.text import Text
from pythonmc.world.executor import Executor
from pythonmc.world.particles import Particles
from pythonmc.world.position.vec2f import Vec2f
from pythonmc.world.position.vec3d import Vec3d
from pythonmc.world.time_ import Time
from pythonmc.world.weather import Weather
from pythonmc.world.world import World
from pythonmc.world.worlds import Worlds

server = Server()
executor = Executor()
pythonMCVersion = ""
pythonMCMajor = 0
pythonMCMinor = 0
pythonMCPatch = 0
namespace = ""
path = ""
