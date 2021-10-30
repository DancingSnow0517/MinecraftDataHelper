import os
import json

from MinecraftDataHelper.items import Item
from MinecraftDataHelper.tags import Tag


class allRecipes:
    def __init__(self, namespace='gen'):
        self.namespace = namespace
        self.StoneCutting = StoneCutting(namespace)
        self.Smoking = Smoking(namespace)
        self.Smelting = Smelting(namespace)
        self.Smithing = Smithing(namespace)
        self.Campfire = Campfire(namespace)
        self.Blasting = Blasting(namespace)
        self.CraftingShapeless = CraftingShapeless(namespace)
        self.CraftingShaped = CraftingShaped(namespace)


class StoneCutting:
    def __init__(self, namespace='gen'):
        self.namespace = namespace
        self.js = {
            "type": "minecraft:stonecutting",
            "ingredient": [],
            "count": 1,
            "result": ''
        }

    def ingredient(self, s):
        if len(self.js["ingredient"]) == 1:
            raise Exception('ingredients最多 1 个物品')
        if isinstance(s, Item):
            self.js["ingredient"].append({"item": s.__str__()})
        else:
            raise Exception('不能使用非Item对象')
        return self

    def count(self, count):
        if count <= 0 or count > 64:
            raise Exception(f'物品数量必须为 1-64 的整数, 你的值 {count}')
        else:
            self.js["count"] = count
        return self

    def result(self, x):
        if isinstance(x, Item):
            self.js["result"] = x.__str__()
        return self

    def build(self, path):
        if not os.path.exists(f'data/{self.namespace}/recipes/'):
            os.makedirs(f'data/{self.namespace}/recipes/')
        with open(f'data/{self.namespace}/recipes/{path}.json', 'w') as f:
            json.dump(self.js, f, indent=4)
        self.js = {
            "type": "minecraft:stonecutting",
            "ingredient": [],
            "count": 1,
            "result": ''
        }
        return


class Smoking:
    def __init__(self, namespace='gen'):
        self.namespace = namespace
        self.js = {
            "type": "smoking",
            "ingredient": [],
            "cookingtime": 100,
            "experience": 0,
            "result": ''
        }

    def ingredient(self, s):
        if len(self.js["ingredient"]) == 1:
            raise Exception('ingredients最多 1 个物品')
        if isinstance(s, Tag):
            self.js["ingredient"].append({"tag": s.__str__()})
        elif isinstance(s, Item):
            self.js["ingredient"].append({"item": s.__str__()})
        else:
            raise Exception('不能使用非Tag/Item对象')
        return self

    def cookingtime(self, time):
        if isinstance(time, int) and time > 0:
            self.js["cookingtime"] = time
        else:
            raise Exception(f'cookingtime 必须为大于 0 的整数，得到了 {time}')
        return self

    def experience(self, exp):
        if isinstance(exp, int) and exp >= 0:
            self.js["experience"] = exp
        else:
            raise Exception(f'experience 必须为大于等于 0 的整数，得到了 {exp}')
        return self

    def result(self, x):
        if isinstance(x, Item):
            self.js["result"] = x.__str__()
        return self

    def build(self, path):
        if not os.path.exists(f'data/{self.namespace}/recipes/'):
            os.makedirs(f'data/{self.namespace}/recipes/')
        with open(f'data/{self.namespace}/recipes/{path}.json', 'w') as f:
            json.dump(self.js, f, indent=4)
        self.js = {
            "type": "smoking",
            "ingredient": [],
            "cookingtime": 100,
            "experience": 0,
            "result": ''
        }
        return


class Smithing:
    def __init__(self, namespace='gen'):
        self.namespace = namespace
        self.js = {
            "type": "smithing",
            "base": {},
            "addition": {},
            "result": {}
        }

    def base(self, s):
        if isinstance(s, Tag):
            self.js["base"]["tag"] = s.__str__()
        elif isinstance(s, Item):
            self.js["base"]["item"] = s.__str__()
        else:
            raise Exception('不能使用非Tag/Item对象')
        return self

    def addition(self, s):
        if isinstance(s, Tag):
            self.js["addition"]["tag"] = s.__str__()
        elif isinstance(s, Item):
            self.js["addition"]["item"] = s.__str__()
        else:
            raise Exception('不能使用非Tag/Item对象')
        return self

    def result(self, x):
        if isinstance(x, Item):
            self.js["result"]["item"] = x.__str__()
        return self

    def build(self, path):
        if not os.path.exists(f'data/{self.namespace}/recipes/'):
            os.makedirs(f'data/{self.namespace}/recipes/')
        with open(f'data/{self.namespace}/recipes/{path}.json', 'w') as f:
            json.dump(self.js, f, indent=4)
        self.js = {
            "type": "smithing",
            "base": {},
            "addition": {},
            "result": {}
        }
        return


class Smelting:
    def __init__(self, namespace='gen'):
        self.namespace = namespace
        self.js = {
            "type": "smelting",
            "ingredient": [],
            "cookingtime": 100,
            "experience": 0,
            "result": ''
        }

    def ingredient(self, s):
        if len(self.js["ingredient"]) == 1:
            raise Exception('ingredients最多 1 个物品')
        if isinstance(s, Tag):
            self.js["ingredient"].append({"tag": s.__str__()})
        elif isinstance(s, Item):
            self.js["ingredient"].append({"item": s.__str__()})
        else:
            raise Exception('不能使用非Tag/Item对象')
        return self

    def cookingtime(self, time):
        if isinstance(time, int) and time > 0:
            self.js["cookingtime"] = time
        else:
            raise Exception(f'cookingtime 必须为大于 0 的整数，得到了 {time}')
        return self

    def experience(self, exp):
        if isinstance(exp, int) and exp >= 0:
            self.js["experience"] = exp
        else:
            raise Exception(f'experience 必须为大于等于 0 的整数，得到了 {exp}')
        return self

    def result(self, x):
        if isinstance(x, Item):
            self.js["result"] = x.__str__()
        return self

    def build(self, path):
        if not os.path.exists(f'data/{self.namespace}/recipes/'):
            os.makedirs(f'data/{self.namespace}/recipes/')
        with open(f'data/{self.namespace}/recipes/{path}.json', 'w') as f:
            json.dump(self.js, f, indent=4)
        self.js = {
            "type": "smelting",
            "ingredient": [],
            "cookingtime": 100,
            "experience": 0,
            "result": ''
        }
        return


class Campfire:
    def __init__(self, namespace='gen'):
        self.namespace = namespace
        self.js = {
            "type": "minecraft:campfire_cooking",
            "ingredient": [],
            "cookingtime": 100,
            "experience": 0,
            "result": ''
        }

    def ingredient(self, s):
        if len(self.js["ingredient"]) == 1:
            raise Exception('ingredients最多 1 个物品')
        if isinstance(s, Tag):
            self.js["ingredient"].append({"tag": s.__str__()})
        elif isinstance(s, Item):
            self.js["ingredient"].append({"item": s.__str__()})
        else:
            raise Exception('不能使用非Tag/Item对象')
        return self

    def cookingtime(self, time):
        if isinstance(time, int) and time > 0:
            self.js["cookingtime"] = time
        else:
            raise Exception(f'cookingtime 必须为大于 0 的整数，得到了 {time}')
        return self

    def experience(self, exp):
        if isinstance(exp, int) and exp >= 0:
            self.js["experience"] = exp
        else:
            raise Exception(f'experience 必须为大于等于 0 的整数，得到了 {exp}')
        return self

    def result(self, x):
        if isinstance(x, Item):
            self.js["result"] = x.__str__()
        return self

    def build(self, path):
        if not os.path.exists(f'data/{self.namespace}/recipes/'):
            os.makedirs(f'data/{self.namespace}/recipes/')
        with open(f'data/{self.namespace}/recipes/{path}.json', 'w') as f:
            json.dump(self.js, f, indent=4)
        self.js = {
            "type": "minecraft:campfire_cooking",
            "ingredient": [],
            "cookingtime": 100,
            "experience": 0,
            "result": ''
        }
        return


class Blasting:
    def __init__(self, namespace='gen'):
        self.namespace = namespace
        self.js = {
            "type": "minecraft:blasting",
            "ingredient": [],
            "cookingtime": 100,
            "experience": 0,
            "result": ''
        }

    def ingredient(self, s):
        if len(self.js["ingredient"]) == 1:
            raise Exception('ingredients最多 1 个物品')
        if isinstance(s, Tag):
            self.js["ingredient"].append({"tag": s.__str__()})
        elif isinstance(s, Item):
            self.js["ingredient"].append({"item": s.__str__()})
        else:
            raise Exception('不能使用非Tag/Item对象')
        return self

    def cookingtime(self, time):
        if isinstance(time, int) and time > 0:
            self.js["cookingtime"] = time
        else:
            raise Exception(f'cookingtime 必须为大于 0 的整数，得到了 {time}')
        return self

    def experience(self, exp):
        if isinstance(exp, int) and exp >= 0:
            self.js["experience"] = exp
        else:
            raise Exception(f'experience 必须为大于等于 0 的整数，得到了 {exp}')
        return self

    def result(self, x):
        if isinstance(x, Item):
            self.js["result"] = x.__str__()
        return self

    def build(self, path):
        if not os.path.exists(f'data/{self.namespace}/recipes/'):
            os.makedirs(f'data/{self.namespace}/recipes/')
        with open(f'data/{self.namespace}/recipes/{path}.json', 'w') as f:
            json.dump(self.js, f, indent=4)
        self.js = {
            "type": "minecraft:blasting",
            "ingredient": [],
            "cookingtime": 100,
            "experience": 0,
            "result": ''
        }
        return


class CraftingShapeless:
    def __init__(self, namespace='gen'):
        self.namespace = namespace
        self.js = {
            "type": "minecraft:crafting_shapeless",
            "ingredients": [],
            "result": {}
        }

    def ingredients(self, s):
        if len(self.js["ingredients"]) >= 9:
            raise Exception('ingredients最多 9 个物品')
        if isinstance(s, Tag):
            self.js["ingredients"].append({"tag": s.__str__()})
        elif isinstance(s, Item):
            self.js["ingredients"].append({"item": s.__str__()})
        else:
            raise Exception('不能使用非Tag/Item对象')
        return self

    def result(self, x, count=1):
        if isinstance(x, Item):
            self.js["result"]["item"] = x.__str__()
            self.js["result"]["count"] = count
        return self

    def build(self, path):
        if not os.path.exists(f'data/{self.namespace}/recipes/'):
            os.makedirs(f'data/{self.namespace}/recipes/')
        with open(f'data/{self.namespace}/recipes/{path}.json', 'w') as f:
            json.dump(self.js, f, indent=4)
        self.js = {
            "type": "minecraft:crafting_shapeless",
            "ingredients": [],
            "result": {}
        }
        return


class CraftingShaped:
    def __init__(self, namespace='gen'):
        self.namespace = namespace
        self.js = {
            "type": "minecraft:crafting_shaped",
            "pattern": [],
            "key": {},
            "result": {}
        }

    def pattern(self, s):
        self.js["pattern"].append(s)
        return self

    def key(self, k, x):
        self.js["key"][k] = {}
        if isinstance(x, Tag):
            self.js["key"][k]["tag"] = x.__str__()
        elif isinstance(x, Item):
            self.js["key"][k]["item"] = x.__str__()
        return self

    def result(self, x, count=1):
        if count <= 0 or count > 64:
            raise Exception(f'物品数量必须为 1-64 的整数, 你的值 {count}')
        if isinstance(x, Item):
            self.js["result"]["item"] = x.__str__()
            self.js["result"]["count"] = count
        return self

    def build(self, path):
        if not os.path.exists(f'data/{self.namespace}/recipes/'):
            os.makedirs(f'data/{self.namespace}/recipes/')
        with open(f'data/{self.namespace}/recipes/{path}.json', 'w') as f:
            json.dump(self.js, f, indent=4)
        self.js = {
            "type": "minecraft:crafting_shaped",
            "pattern": [],
            "key": {},
            "result": {}
        }
        return
