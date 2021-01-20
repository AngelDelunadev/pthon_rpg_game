from character import Character
class Hero(Character):
    def __init__(self,health = 10,power = 5):
        self.health = health
        self.power = power

    def attack(self,goblin):
        goblin.health -= self.power
        print("You do %d damage to the goblin." % self.power)

    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))