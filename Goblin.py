from enemy import Enemy
import random

class Goblin (Enemy):
    def __init__(self):
        super().__init__()
        super().set_stats("Goblin", 5, 66)
        super().addToInventory(items = ["knife", "molotov"])

    def use_item(self):
       Chance = random.randint(1,10) 
       if (Chance >= 1 and Chance <= 5):
           print(f"Goblin did nothing")
           return
       if (Chance > 5 and Chance <= 8):
            print(f"Goblin used knife")
            #stab()
       if (Chance > 8 and Chance <= 10):
           print(f"Goblin used Molotov")
           #throw_molotov()


gobby = Goblin()
for i in range(1, 10):
    gobby.use_item()
    




        



