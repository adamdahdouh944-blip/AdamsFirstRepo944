from character import character

class Enemy (character):
    def __init__(self):
        super().__init__()
        super().set_stats("Enemy", 5, 30)


goblin = Enemy()
goblin.get_stats()