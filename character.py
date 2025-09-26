class character ():
    def __init__(self):

        self.max_health = 100

        self.stats = {
            "name" : name,
            "strength" : strength,
            "health" : health
        }

        self.inventory = ["item 1", "item 2", "item 3"]

        print(f"This is the Character Class")

    def get_stats(self):
        print("Your Stats Are: ")
        for key, value in self.stats.items():
            print(f"{key} : {value}")
        
    def set_stats(self, name, strength, health):
        self.stats['name'] = name
        self.stats['strength'] = strength
        self.stats['health'] = health

    def set_inventory(self, item1, item2, item3):
        self.inventory["item 1"] = item1
        self.inventory["item 2"] = item2
        self.inventory["item 3"] = item3

    def retreat(self):
        print(f"you retreated")

    def move(self):
        pass
    
    def attack(self):
        #if (inRange() < 1):
            #print(f"There are no enemies in range\n")
            #return

        #target = input(f"Who do you want to attack? {self.inRange()}\n")
        #print(f"Enemy Selected: {target}")
        #match target:
            #case "goblin"
                #pass
            #case "dragon"
                #pass
        pass

    def take_damage(self, damage):
        self.stats["health"] -= damage
        print(f"Your Health is now {self.stats['health']}")