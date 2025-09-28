from enemy import Enemy
import random

class Goblin (Enemy):
    def __init__(self):
        super().__init__()
        super().set_stats("Goblin", 5, 66)
        super().addToInventory(items = ["knife", "molotov"])

        self.position = [7, 6]

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

    def move(self, position):
        Chance = random.randint(1, 20)
        if (Chance >= 1 and Chance <= 5):
            position[0] -= 1
            print(f"\n{self.stats['name']} went North!\n")
            return position
        if (Chance >= 6 and Chance <= 10):
            position[0] += 1
            print(f"\n{self.stats['name']} went South!\n")
            return position
        if (Chance >= 11 and Chance <= 15):
            position[1] += 1
            print(f"\n{self.stats['name']} went East!\n")
            return position 
        if (Chance >= 16 and Chance <= 20):
            position[1] -= 1
            print(f"\n{self.stats['name']} went West\n")
            return position

    




        



