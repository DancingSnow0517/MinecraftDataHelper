from MinecraftDataHelper import items
from MinecraftDataHelper.items import Item


class Tag:
    def __init__(self, name, namespace='minecraft'):
        self.name = name
        self.namespace = namespace
        self.list = []

    def add(self, *item):
        for i in item:
            if isinstance(i, Item):
                if i not in self.list:
                    self.list.append(i)
            elif isinstance(i, Tag):
                for j in i.list:
                    self.list.append(j)

    def remove(self, item: Item):
        if item in self.list:
            self.list.remove(item)

    def getList(self) -> str:
        rt = []
        for i in self.list:
            rt.append(i.__str__())
        return rt.__str__()

    def __str__(self) -> str:
        return f'{self.namespace}:{self.name}'


ACACIA_LOGS = Tag('acacia_logs')
ACACIA_LOGS.add(items.ACACIA_LOG, items.ACACIA_WOOD, items.STRIPPED_ACACIA_LOG, items.STRIPPED_ACACIA_WOOD)
ANVIL = Tag('anvil')
ANVIL.add(items.ANVIL, items.CHIPPED_ANVIL, items.DAMAGED_ANVIL)
ARROWS = Tag('arrows')
ARROWS.add(items.ARROW, items.TIPPED_ARROW, items.SPECTRAL_ARROW)
AXOLOTL_TEMPT_ITEMS = Tag('axolotl_tempt_items')
AXOLOTL_TEMPT_ITEMS.add(items.TROPICAL_FISH_BUCKET)
BANNERS = Tag('banners')
BANNERS.add(items.WHITE_BANNER, items.ORANGE_BANNER, items.MAGENTA_BANNER, items.LIGHT_BLUE_BANNER, items.YELLOW_BANNER,
            items.LIME_BANNER, items.PINK_BANNER, items.GRAY_BANNER, items.LIGHT_GRAY_BANNER, items.CYAN_BANNER,
            items.PURPLE_BANNER, items.BLUE_BANNER, items.BROWN_BANNER, items.GREEN_BANNER, items.RED_BANNER,
            items.BLACK_BANNER)
BEACON_PAYMENT_ITEMS = Tag('beacon_payment_items')
BEACON_PAYMENT_ITEMS.add(items.NETHERITE_INGOT, items.EMERALD, items.DIAMOND, items.GOLD_INGOT, items.IRON_INGOT)
BEDS = Tag('beds')
BEDS.add(items.RED_BED, items.BLACK_BED, items.BLUE_BED, items.BROWN_BED, items.CYAN_BED, items.GRAY_BED,
         items.GREEN_BED, items.LIGHT_BLUE_BED, items.LIGHT_GRAY_BED, items.LIME_BED, items.MAGENTA_BED,
         items.ORANGE_BED, items.PINK_BED, items.PURPLE_BED, items.WHITE_BED, items.YELLOW_BED)
BIRCH_LOGS = Tag('birch_logs')
BIRCH_LOGS.add(items.BIRCH_LOG, items.BIRCH_WOOD, items.STRIPPED_BIRCH_LOG, items.STRIPPED_BIRCH_WOOD)
BOATS = Tag('boats')
BOATS.add(items.OAK_BOAT, items.SPRUCE_BOAT, items.BIRCH_BOAT, items.JUNGLE_BOAT, items.ACACIA_BOAT,
          items.DARK_OAK_BOAT)
CANDLES = Tag('candles')
CANDLES.add(items.CANDLE, items.WHITE_CANDLE, items.ORANGE_CANDLE, items.MAGENTA_CANDLE, items.LIGHT_BLUE_CANDLE,
            items.YELLOW_CANDLE, items.LIME_CANDLE, items.PINK_CANDLE, items.GRAY_CANDLE, items.LIGHT_GRAY_CANDLE,
            items.CYAN_CANDLE, items.PURPLE_CANDLE, items.BLUE_CANDLE, items.BROWN_CANDLE, items.GREEN_CANDLE,
            items.RED_CANDLE, items.BLACK_CANDLE)
CARPETS = Tag('carpets')
CARPETS.add(items.WHITE_CARPET, items.ORANGE_CARPET, items.MAGENTA_CARPET, items.LIGHT_BLUE_CARPET, items.YELLOW_CARPET,
            items.LIME_CARPET, items.PINK_CARPET, items.GRAY_CARPET, items.LIGHT_GRAY_CARPET, items.CYAN_CARPET,
            items.PURPLE_CARPET, items.BLUE_CARPET, items.BROWN_CARPET, items.GREEN_CARPET, items.RED_CARPET,
            items.BLACK_CARPET)
CLUSTER_MAX_HARVESTABLES = Tag('cluster_max_harvestables')
CLUSTER_MAX_HARVESTABLES.add(items.DIAMOND_PICKAXE, items.GOLDEN_PICKAXE, items.IRON_PICKAXE, items.NETHERITE_PICKAXE,
                             items.STONE_PICKAXE, items.WOODEN_PICKAXE)
COALS = Tag('coals')
COALS.add(items.COAL, items.CHARCOAL)
COAL_ORES = Tag('coal_ores')
COAL_ORES.add(items.COAL_ORE, items.DEEPSLATE_COAL_ORE)
COPPER_ORES = Tag('copper_ores')
COPPER_ORES.add(items.COPPER_ORE, items.DEEPSLATE_COPPER_ORE)
CREEPER_DROP_MUSIC_DISCS = Tag('creeper_drop_music_discs')
CREEPER_DROP_MUSIC_DISCS.add(items.MUSIC_DISC_13, items.MUSIC_DISC_CAT, items.MUSIC_DISC_BLOCKS, items.MUSIC_DISC_CHIRP,
                             items.MUSIC_DISC_FAR, items.MUSIC_DISC_MALL, items.MUSIC_DISC_MELLOHI,
                             items.MUSIC_DISC_STAL, items.MUSIC_DISC_STRAD, items.MUSIC_DISC_WARD, items.MUSIC_DISC_11,
                             items.MUSIC_DISC_WAIT)
CRIMSON_STEMS = Tag('crimson_stems')
CRIMSON_STEMS.add(items.CRIMSON_STEM, items.STRIPPED_CRIMSON_STEM, items.CRIMSON_HYPHAE, items.STRIPPED_CRIMSON_HYPHAE)
DARK_OAK_LOGS = Tag('dark_oak_logs')
DARK_OAK_LOGS.add(items.DARK_OAK_LOG, items.DARK_OAK_WOOD, items.STRIPPED_DARK_OAK_LOG, items.STRIPPED_DARK_OAK_WOOD)
DIAMOND_ORES = Tag('diamond_ores')
DIAMOND_ORES.add(items.DIAMOND_ORE, items.DEEPSLATE_DIAMOND_ORE)
EMERALD_ORES = Tag('emerald_ores')
EMERALD_ORES.add(items.EMERALD_ORE, items.DEEPSLATE_EMERALD_ORE)
FISHES = Tag('fishes')
FISHES.add(items.COD, items.COOKED_COD, items.SALMON, items.COOKED_SALMON, items.PUFFERFISH, items.TROPICAL_FISH)
FOX_FOOD = Tag('fox_food')
FOX_FOOD.add(items.SWEET_BERRIES, items.GLOW_BERRIES)
FREEZE_IMMUNE_WEARABLES = Tag('freeze_immune_wearables')
FREEZE_IMMUNE_WEARABLES.add(items.LEATHER_BOOTS, items.LEATHER_LEGGINGS, items.LEATHER_CHESTPLATE, items.LEATHER_HELMET,
                            items.LEATHER_HORSE_ARMOR)
GOLD_ORES = Tag('gold_ores')
GOLD_ORES.add(items.GOLD_ORE, items.NETHER_GOLD_ORE, items.DEEPSLATE_GOLD_ORE)
IGNORED_BY_PIGLIN_BABIES = Tag('ignored_by_piglin_babies')
IGNORED_BY_PIGLIN_BABIES.add(items.LEATHER)
IRON_ORES = Tag('iron_ores')
IRON_ORES.add(items.IRON_ORE, items.DEEPSLATE_IRON_ORE)
JUNGLE_LOGS = Tag('jungle_logs')
JUNGLE_LOGS.add(items.JUNGLE_LOG, items.JUNGLE_WOOD, items.STRIPPED_JUNGLE_LOG, items.STRIPPED_JUNGLE_WOOD)
LAPIS_ORES = Tag('lapis_ores')
LAPIS_ORES.add(items.LAPIS_ORE, items.DEEPSLATE_LAPIS_ORE)
LEAVES = Tag('leaves')
LEAVES.add(items.JUNGLE_LEAVES, items.OAK_LEAVES, items.SPRUCE_LEAVES, items.DARK_OAK_LEAVES, items.ACACIA_LEAVES,
           items.BIRCH_LEAVES, items.AZALEA_LEAVES, items.FLOWERING_AZALEA_LEAVES)
LECTERN_BOOKS = Tag('lectern_books')
LECTERN_BOOKS.add(items.WRITTEN_BOOK, items.WRITABLE_BOOK)
MUSIC_DISCS = Tag('music_discs')
MUSIC_DISCS.add(CREEPER_DROP_MUSIC_DISCS, items.MUSIC_DISC_PIGSTEP)
NON_FLAMMABLE_WOOD = Tag('non_flammable_wood')
NON_FLAMMABLE_WOOD.add(items.WARPED_STEM, items.STRIPPED_WARPED_STEM, items.WARPED_HYPHAE, items.STRIPPED_WARPED_HYPHAE,
                       items.CRIMSON_STEM, items.STRIPPED_CRIMSON_STEM, items.CRIMSON_HYPHAE,
                       items.STRIPPED_CRIMSON_HYPHAE, items.CRIMSON_PLANKS, items.WARPED_PLANKS, items.CRIMSON_SLAB,
                       items.WARPED_SLAB, items.CRIMSON_PRESSURE_PLATE, items.WARPED_PRESSURE_PLATE,
                       items.CRIMSON_FENCE, items.WARPED_FENCE, items.CRIMSON_TRAPDOOR, items.WARPED_TRAPDOOR,
                       items.CRIMSON_FENCE_GATE, items.WARPED_FENCE_GATE, items.CRIMSON_STAIRS, items.WARPED_STAIRS,
                       items.CRIMSON_BUTTON, items.WARPED_BUTTON, items.CRIMSON_DOOR, items.WARPED_DOOR,
                       items.CRIMSON_SIGN, items.WARPED_SIGN)
OAK_LOGS = Tag('oak_logs')
OAK_LOGS.add(items.OAK_LOG, items.OAK_WOOD, items.STRIPPED_OAK_LOG, items.STRIPPED_OAK_WOOD)
PIGLIN_FOOD = Tag('piglin_food')
PIGLIN_FOOD.add(items.PORKCHOP, items.COOKED_PORKCHOP)
PIGLIN_LOVED = Tag('piglin_loved')
PIGLIN_LOVED.add(GOLD_ORES, items.GOLD_BLOCK, items.GILDED_BLACKSTONE, items.LIGHT_WEIGHTED_PRESSURE_PLATE,
                 items.GOLD_INGOT, items.BELL, items.CLOCK, items.GOLDEN_CARROT, items.GLISTERING_MELON_SLICE,
                 items.GOLDEN_APPLE, items.ENCHANTED_GOLDEN_APPLE, items.GOLDEN_HELMET, items.GOLDEN_CHESTPLATE,
                 items.GOLDEN_LEGGINGS, items.GOLDEN_BOOTS, items.GOLDEN_HORSE_ARMOR, items.GOLDEN_SWORD,
                 items.GOLDEN_PICKAXE, items.GOLDEN_SHOVEL, items.GOLDEN_AXE, items.GOLDEN_HOE, items.RAW_GOLD,
                 items.RAW_GOLD_BLOCK)
PIGLIN_REPELLENTS = Tag('piglin_repellents')
PIGLIN_REPELLENTS.add(items.SOUL_TORCH, items.SOUL_LANTERN, items.SOUL_CAMPFIRE)
PLANKS = Tag('planks')
PLANKS.add(items.OAK_PLANKS, items.SPRUCE_PLANKS, items.BIRCH_PLANKS, items.JUNGLE_PLANKS, items.ACACIA_PLANKS,
           items.DARK_OAK_PLANKS, items.CRIMSON_PLANKS, items.WARPED_PLANKS)
RAILS = Tag('rails')
RAILS.add(items.RAIL, items.POWERED_RAIL, items.DETECTOR_RAIL, items.ACTIVATOR_RAIL)
REDSTONE_ORES = Tag('redstone_ores')
REDSTONE_ORES.add(items.REDSTONE_ORE, items.DEEPSLATE_REDSTONE_ORE)
SAND = Tag('sand')
SAND.add(items.SAND, items.RED_SAND)
SAPLINGS = Tag('saplings')
SAPLINGS.add(items.OAK_SAPLING, items.SPRUCE_SAPLING, items.BIRCH_SAPLING, items.JUNGLE_SAPLING, items.ACACIA_SAPLING,
             items.DARK_OAK_SAPLING, items.AZALEA, items.FLOWERING_AZALEA)
SIGNS = Tag('signs')
SIGNS.add(items.OAK_SIGN, items.SPRUCE_SIGN, items.BIRCH_SIGN, items.ACACIA_SIGN, items.JUNGLE_SIGN,
          items.DARK_OAK_SIGN, items.CRIMSON_SIGN, items.WARPED_SIGN)
SMALL_FLOWERS = Tag('small_flowers')
SMALL_FLOWERS.add(items.DANDELION, items.POPPY, items.BLUE_ORCHID, items.ALLIUM, items.AZURE_BLUET, items.RED_TULIP,
                  items.ORANGE_TULIP, items.WHITE_TULIP, items.PINK_TULIP, items.OXEYE_DAISY, items.CORNFLOWER,
                  items.LILY_OF_THE_VALLEY, items.WITHER_ROSE)
SOUL_FIRE_BASE_BLOCKS = Tag('soul_fire_base_blocks')
SOUL_FIRE_BASE_BLOCKS.add(items.SOUL_SAND, items.SOUL_SOIL)
SPRUCE_LOGS = Tag('spruce_logs')
SPRUCE_LOGS.add(items.SPRUCE_LOG, items.SPRUCE_WOOD, items.STRIPPED_SPRUCE_LOG, items.STRIPPED_SPRUCE_WOOD)
STONE_BRICKS = Tag('stone_bricks')
STONE_BRICKS.add(items.STONE_BRICKS, items.MOSSY_STONE_BRICKS, items.CRACKED_STONE_BRICKS, items.CHISELED_STONE_BRICKS)
STONE_CRAFTING_MATERIALS = Tag('stone_crafting_materials')
STONE_CRAFTING_MATERIALS.add(items.COBBLESTONE, items.BLACKSTONE, items.COBBLED_DEEPSLATE)
STONE_TOOL_MATERIALS = Tag('stone_tool_materials')
STONE_TOOL_MATERIALS.add(items.COBBLESTONE, items.BLACKSTONE, items.COBBLED_DEEPSLATE)
TALL_FLOWERS = Tag('tall_flowers')
TALL_FLOWERS.add(items.SUNFLOWER, items.LILAC, items.PEONY, items.ROSE_BUSH)
WALLS = Tag('walls')
WALLS.add(items.COBBLESTONE_WALL, items.MOSSY_COBBLESTONE_WALL, items.BRICK_WALL, items.PRISMARINE_WALL,
          items.RED_SANDSTONE_WALL, items.MOSSY_STONE_BRICK_WALL, items.GRANITE_WALL, items.STONE_BRICK_WALL,
          items.NETHER_BRICK_WALL, items.ANDESITE_WALL, items.RED_NETHER_BRICK_WALL, items.SANDSTONE_WALL,
          items.END_STONE_BRICK_WALL, items.DIORITE_WALL, items.BLACKSTONE_WALL, items.POLISHED_BLACKSTONE_BRICK_WALL,
          items.POLISHED_BLACKSTONE_WALL, items.COBBLED_DEEPSLATE_WALL, items.POLISHED_DEEPSLATE_WALL,
          items.DEEPSLATE_TILE_WALL, items.DEEPSLATE_BRICK_WALL)
WARPED_STEMS = Tag('warped_stems')
WARPED_STEMS.add(items.WARPED_STEM, items.STRIPPED_WARPED_STEM, items.WARPED_HYPHAE, items.STRIPPED_WARPED_HYPHAE)
WOODEN_BUTTONS = Tag('wooden_buttons')
WOODEN_BUTTONS.add(items.OAK_BUTTON, items.SPRUCE_BUTTON, items.BIRCH_BUTTON, items.JUNGLE_BUTTON, items.ACACIA_BUTTON,
                   items.DARK_OAK_BUTTON, items.CRIMSON_BUTTON, items.WARPED_BUTTON)
WOODEN_DOORS = Tag('wooden_doors')
WOODEN_DOORS.add(items.OAK_DOOR, items.SPRUCE_DOOR, items.BIRCH_DOOR, items.JUNGLE_DOOR, items.ACACIA_DOOR,
                 items.DARK_OAK_DOOR, items.CRIMSON_DOOR, items.WARPED_DOOR)
WOODEN_FENCES = Tag('wooden_fences')
WOODEN_FENCES.add(items.OAK_FENCE, items.ACACIA_FENCE, items.DARK_OAK_FENCE, items.SPRUCE_FENCE, items.BIRCH_FENCE,
                  items.JUNGLE_FENCE, items.CRIMSON_FENCE, items.WARPED_FENCE)
WOODEN_PRESSURE_PLATES = Tag('wooden_pressure_plates')
WOODEN_PRESSURE_PLATES.add(items.OAK_PRESSURE_PLATE, items.SPRUCE_PRESSURE_PLATE, items.BIRCH_PRESSURE_PLATE,
                           items.JUNGLE_PRESSURE_PLATE, items.ACACIA_PRESSURE_PLATE, items.DARK_OAK_PRESSURE_PLATE,
                           items.CRIMSON_PRESSURE_PLATE, items.WARPED_PRESSURE_PLATE)
WOODEN_SLABS = Tag('wooden_slabs')
WOODEN_SLABS.add(items.OAK_SLAB, items.SPRUCE_SLAB, items.BIRCH_SLAB, items.JUNGLE_SLAB, items.ACACIA_SLAB,
                 items.DARK_OAK_SLAB, items.CRIMSON_SLAB, items.WARPED_SLAB)
WOODEN_STAIRS = Tag('wooden_stairs')
WOODEN_STAIRS.add(items.OAK_STAIRS, items.SPRUCE_STAIRS, items.BIRCH_STAIRS, items.JUNGLE_STAIRS, items.ACACIA_STAIRS,
                  items.DARK_OAK_STAIRS, items.CRIMSON_STAIRS, items.WARPED_STAIRS)
WOODEN_TRAPDOORS = Tag('wooden_trapdoors')
WOODEN_TRAPDOORS.add(items.ACACIA_TRAPDOOR, items.BIRCH_TRAPDOOR, items.DARK_OAK_TRAPDOOR, items.JUNGLE_TRAPDOOR,
                     items.OAK_TRAPDOOR, items.SPRUCE_TRAPDOOR, items.CRIMSON_TRAPDOOR, items.WARPED_TRAPDOOR)
WOOL = Tag('wool')
WOOL.add(items.WHITE_WOOL, items.ORANGE_WOOL, items.MAGENTA_WOOL, items.LIGHT_BLUE_WOOL, items.YELLOW_WOOL,
         items.LIME_WOOL, items.PINK_WOOL, items.GRAY_WOOL, items.LIGHT_GRAY_WOOL, items.CYAN_WOOL, items.PURPLE_WOOL,
         items.BLUE_WOOL, items.BROWN_WOOL, items.GREEN_WOOL, items.RED_WOOL, items.BLACK_WOOL)
TRAPDOORS = Tag('trapdoors')
TRAPDOORS.add(WOODEN_TRAPDOORS, items.IRON_TRAPDOOR)
STAIRS = Tag('stairs')
STAIRS.add(WOODEN_STAIRS, items.COBBLESTONE_STAIRS, items.SANDSTONE_STAIRS, items.NETHER_BRICK_STAIRS,
           items.STONE_BRICK_STAIRS, items.BRICK_STAIRS, items.PURPUR_STAIRS, items.QUARTZ_STAIRS,
           items.RED_SANDSTONE_STAIRS, items.PRISMARINE_BRICK_STAIRS, items.PRISMARINE_STAIRS,
           items.DARK_PRISMARINE_STAIRS, items.POLISHED_GRANITE_STAIRS, items.SMOOTH_RED_SANDSTONE_STAIRS,
           items.MOSSY_STONE_BRICK_STAIRS, items.POLISHED_DIORITE_STAIRS, items.MOSSY_COBBLESTONE_STAIRS,
           items.END_STONE_BRICK_STAIRS, items.STONE_STAIRS, items.SMOOTH_SANDSTONE_STAIRS, items.SMOOTH_QUARTZ_STAIRS,
           items.GRANITE_STAIRS, items.ANDESITE_STAIRS, items.RED_NETHER_BRICK_STAIRS, items.POLISHED_ANDESITE_STAIRS,
           items.DIORITE_STAIRS, items.BLACKSTONE_STAIRS, items.POLISHED_BLACKSTONE_BRICK_STAIRS,
           items.POLISHED_BLACKSTONE_STAIRS, items.COBBLED_DEEPSLATE_STAIRS, items.POLISHED_DEEPSLATE_STAIRS,
           items.DEEPSLATE_TILE_STAIRS, items.DEEPSLATE_BRICK_STAIRS, items.OXIDIZED_CUT_COPPER_STAIRS,
           items.WEATHERED_CUT_COPPER_STAIRS, items.EXPOSED_CUT_COPPER_STAIRS, items.CUT_COPPER_STAIRS,
           items.WAXED_WEATHERED_CUT_COPPER_STAIRS, items.WAXED_EXPOSED_CUT_COPPER_STAIRS,
           items.WAXED_CUT_COPPER_STAIRS, items.WAXED_OXIDIZED_CUT_COPPER_STAIRS)
BUTTONS = Tag('buttons')
BUTTONS.add(WOODEN_BUTTONS, items.STONE_BUTTON, items.POLISHED_BLACKSTONE_BUTTON)
FENCES = Tag('fences')
FENCES.add(WOODEN_FENCES, items.NETHER_BRICK_FENCE)
FLOWERS = Tag('flowers')
FLOWERS.add(SMALL_FLOWERS, TALL_FLOWERS, items.FLOWERING_AZALEA_LEAVES, items.FLOWERING_AZALEA)
LOGS_THAT_BURN = Tag('logs_that_burn')
LOGS_THAT_BURN.add(DARK_OAK_LOGS, OAK_LOGS, ACACIA_LOGS, BIRCH_LOGS, JUNGLE_LOGS, SPRUCE_LOGS)
DOORS = Tag('doors')
DOORS.add(WOODEN_DOORS, items.IRON_DOOR)
OCCLUDES_VIBRATION_SIGNALS = Tag('occludes_vibration_signals')
OCCLUDES_VIBRATION_SIGNALS.add(WOOL)
SLABS = Tag('slabs')
SLABS.add(WOODEN_SLABS, items.STONE_SLAB, items.SMOOTH_STONE_SLAB, items.STONE_BRICK_SLAB, items.SANDSTONE_SLAB,
          items.PURPUR_SLAB, items.QUARTZ_SLAB, items.RED_SANDSTONE_SLAB, items.BRICK_SLAB, items.COBBLESTONE_SLAB,
          items.NETHER_BRICK_SLAB, items.PETRIFIED_OAK_SLAB, items.PRISMARINE_SLAB, items.PRISMARINE_BRICK_SLAB,
          items.DARK_PRISMARINE_SLAB, items.POLISHED_GRANITE_SLAB, items.SMOOTH_RED_SANDSTONE_SLAB,
          items.MOSSY_STONE_BRICK_SLAB, items.POLISHED_DIORITE_SLAB, items.MOSSY_COBBLESTONE_SLAB,
          items.END_STONE_BRICK_SLAB, items.SMOOTH_SANDSTONE_SLAB, items.SMOOTH_QUARTZ_SLAB, items.GRANITE_SLAB,
          items.ANDESITE_SLAB, items.RED_NETHER_BRICK_SLAB, items.POLISHED_ANDESITE_SLAB, items.DIORITE_SLAB,
          items.CUT_SANDSTONE_SLAB, items.CUT_RED_SANDSTONE_SLAB, items.BLACKSTONE_SLAB,
          items.POLISHED_BLACKSTONE_BRICK_SLAB, items.POLISHED_BLACKSTONE_SLAB, items.COBBLED_DEEPSLATE_SLAB,
          items.POLISHED_DEEPSLATE_SLAB, items.DEEPSLATE_TILE_SLAB, items.DEEPSLATE_BRICK_SLAB,
          items.WAXED_WEATHERED_CUT_COPPER_SLAB, items.WAXED_EXPOSED_CUT_COPPER_SLAB, items.WAXED_CUT_COPPER_SLAB,
          items.OXIDIZED_CUT_COPPER_SLAB, items.WEATHERED_CUT_COPPER_SLAB, items.EXPOSED_CUT_COPPER_SLAB,
          items.CUT_COPPER_SLAB, items.WAXED_OXIDIZED_CUT_COPPER_SLAB)
LOGS = Tag('logs')
LOGS.add(LOGS_THAT_BURN, CRIMSON_STEMS, WARPED_STEMS)
