# MinecraftDataHelper

### 一个 `Minecraft` 数据包配方小工具

#### 使用 `pip install mcdatahelper` 来安装模块

### 样例代码

```
from MinecraftDataHelper import items, tags
from MinecraftDataHelper.Recipes import *

testGen = allRecipes('testGen')

testGen.CraftingShaped.pattern('ABA').pattern('AAA').pattern('ABA').key('A', items.APPLE).key('B', items.BOOK).result(items.SAND, 64).build('test1')
testGen.CraftingShapeless.ingredients(items.BIRCH_LOG).ingredients(items.BIRCH_LOG).result(items.BIRCH_BOAT).build('test2')
testGen.CraftingShapeless.ingredients(tags.LOGS).result(items.BROWN_DYE, 64).build('1111')
testGen.Smelting.ingredient(items.OAK_LEAVES).experience(0).cookingtime(100).result(items.OAK_LOG).build('test3')
testGen.Smithing.base(items.APPLE).addition(items.GOLD_BLOCK).result(items.GOLDEN_APPLE).build('test4')
testGen.Campfire.ingredient(items.BIRCH_LOG).result(items.BIRCH_BOAT).build('test5')
testGen.StoneCutting.ingredient(items.STONE).result(items.STONE_SLAB).count(2).build('test6')
testGen.Smoking.ingredient(items.OAK_LEAVES).experience(0).cookingtime(100).result(items.OAK_LOG).build('test7')
testGen.Blasting.ingredient(items.OAK_LEAVES).experience(0).cookingtime(100).result(items.OAK_LOG).build('test8')
```
