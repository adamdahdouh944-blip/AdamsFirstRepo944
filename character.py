class character ():
    def __init__(self):

        self.max_health = 100

        self.stats = {
            "name" : "character",
            "strength" : 0,
            "health" : 0,
        }

        self.inventory = []

        self.position = [0,0]

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

    def move(self, position):
        action = input(f"Select a direction you want to go: North, South, East and West\n")
        print(f"The direction you have selected is {action}")
        match action:
            case "north":
                position[0] -= 1
                print(f"You went North!")
                return position
            case "south":
                position[0] += 1
                print(f"You went South!")
                return position
            case "east":
                position[1] += 1
                print(f"You went East!")
                return position 
            case "west":
                position[1] -= 1
                print(f"You went West")
                return position
            case _:
                print (f"That is not a direction you can go in!")
                return
    
    def inRange(self, game_world, position, target_position):
        #get game_world and user_position
        position = self.position
        #check all 8 cells adjacent to the users_position
        Range = [
            game_world[position[0] + 1][position[1]],
            game_world[position[0] - 1][position[1]],
            game_world[position[0]][position[1] + 1],
            game_world[position[0]][position[1] - 1],
            game_world[position[0] + 1][position[1] + 1],
            game_world[position[0] - 1][position[1] - 1],
            game_world[position[0] + 1][position[1] - 1],
            game_world[position[0] - 1][position[1] + 1]
        ]
        #if adjacent cells = target_positon
        for row in Range:
            for cell in row:
                if (cell == target_position):
                    return True
                else:
                    return False


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
