from Character import *


class Player(Character):
    def __init__(self, inventory, level):
        self.inventory = inventory
        self.level = level

    def heal(self, amount):
        if self.health + amount > self.max_health:
            self.health = self.max_health
        else:
            self.health += amount

    def move(self, direction):
        pass

    def look_around(self):
        pass
    