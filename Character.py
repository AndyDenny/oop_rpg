class Character:
    def __init__(self, name, health, max_health, attack_power):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.attack_power = attack_power

    def take_damage(self, damage):
        if self.health > damage:
            self.health -= damage
        else:
            self.health = 0

    def is_alive(self):
        if self.health <= 0:
            return True
        else:
            return False

    def attack(self, target):
        target.health -= self.attack_power