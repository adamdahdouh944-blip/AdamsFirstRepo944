from character import character

class Hero (character):
    def __init__(self):
        super().__init__()
        super().set_stats("hero", 7, 100)
        super().addToInventory(items = ["sword", "health potion", "rope"])

        self.health_potion_strength = 5

    def set_name(self, name):
        self.stats['name'] = name
        self.get_stats()

    def heal(self, item_name):

        if (self.inventory.count("health potion") <= 0):
            print (f"you don't have any {item_name}")
            return

        print (f"You've used a {item_name} you've restored {self.health_potion_strength} Health")
        self.stats["health"] += self.health_potion_strength

        if (self.stats["health"] >= self.max_health):
            print(f"You've Reached Max Health")
            self.stats["health"] = self.max_health

        print(f"Your Health is now {self.stats['health']}")
        self.inventory.remove("health potion")
        print(f"Your inventory is now {self.inventory}")

    def use_item(self):
        item_name = input(f"What item do you want to use? {self.inventory}\n")
        print (f"The item you want to use is {item_name}")
        match item_name:
            case "sword":
                pass
            case "health potion":
                self.heal(self, item_name)
                #Remove health potion from inventory
            case "rope":
                pass
            case _:
                print(f"{item_name} is not in your inventory")
