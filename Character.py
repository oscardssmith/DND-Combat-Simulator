
class Character():
    def __init__(self, stats, attacks):
        self.stats = stats
        self.attacks = attacks
        
    def attack(self, target, attack):
        target.stats[hp] -= attack.damage(target)
