from Die_Simulator import die_parse, modifier
from Character import Character, Stats

class Attack:
    def __init__(self, toHitRoll, damage):
        self.toHitRoll = die_parse(toHitRoll)
        self.damage = die_parse(damage)
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return f'{self.uses} uses: {self.toHitRoll} to hit, {self.damage} damage'
    
    def execute(self, attacker,targets):
        for target in targets:
            if self.hits(attacker, target):
                target.hp -= self.damage.roll()

    def hits(self, attacker, target):
        return self.toHitRoll.roll() > target.stats.ac

class Spell(Attack):
    def __init__(self, toHitRoll, damage, stat = 'ac', test='{0}', uses = float('inf')):
        self.toHitRoll = die_parse(toHitRoll)
        self.stat = stat
        self.damage = die_parse(damage)
        self.test = test
        self.uses = uses

    def execute(self, attacker,targets):
        self.uses -= 1
        for target in targets:
            if self.hits(attacker, target):
                target.hp -= self.damage.roll()
                if target.hp > target.stats.max_hp:
                    target.hp = target.stats.max_hp

    def hits(self, attacker, target):
        roll = self.toHitRoll.roll()
        #TODO: This line is really slow (optimize)
        threshold = eval(self.test.format(getattr(target.stats, self.stat)))
        return roll > threshold

if __name__ == '__main__':
    a = Attack('d20+1', 'd8+1')
    
    Adam = Character(Stats((12,11,10,10,14,17,10,16)),
                    [Attack('d20+1', 'd8+1'),Attack('d20+1', 'd10+1'),])

    for _ in range(10):
        a.execute(Adam, (Adam,))
    print(a)
