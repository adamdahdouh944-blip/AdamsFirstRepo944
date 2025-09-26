class character ():
    def __init__(self):

        self.max_health = 100

        self.stats = {
            "name" : "character",
            "strength" : 0,
            "health" : 0,
        }

        self.inventory = []

        self.position = (0,0)

    def get_stats(self):
        print("Your Stats Are: ")
        for key, value in dict(self.stats).items():
            print(f"{key} : {value}")
        
    def set_stats(self, name, strength, health):
        self.stats.update({"name" : name})
        self.stats.update({"strength" : strength})
        self.stats.update({"health" : health})

    def addToInventory(self, items): #items is a list
        for item in items:
            self.inventory.append(item)

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
