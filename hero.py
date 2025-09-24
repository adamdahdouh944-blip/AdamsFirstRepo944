class Hero ():
    def __init__(self):
        
        self.max_health = 100.0
        self.health_potion_strength = 5

        self.stats = {
            "name" : "hero",
            "strength" : 7,
            "health" : 100.0
        }

        self.inventory = ["sword", "health potion", "rope"]
    
    def get_stats(self):
        print("Your Stats Are: ")
        for key, value in self.stats.items():
            print(f"{key} : {value}")

    def set_name(self, name):
        self.stats['name'] = name
        self.get_stats()

    def move(self):
        pass
    
    def attack(self):
        pass

    def take_damage(self, damage):
        self.stats["health"] -= damage
        print(f"Your Health is now {self.stats['health']}")
        pass

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


hero = Hero()
hero.get_stats()
hero.set_name("Adam")
hero.stats["health"] = 70
hero.heal("health potion")
print("\n.............................\n")