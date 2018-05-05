from Die_Simulator import die_parse, modifier

class Attack:
    __slots__ = 'toHitRoll', 'damage'
    def __init__(self, toHitRoll, damage):
        self.toHitRoll = die_parse(toHitRoll)
        self.damage = die_parse(damage)
    
    def execute(self, attacker,targets):
        for target in targets:
            if self.hits(attacker, target):
                target.hp -= self.damage.roll()

    def hits(self, attacker, target):
        return self.toHitRoll.roll() > target.stats.ac
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return f'{self.toHitRoll} to hit, {self.damage} damage'


class Spell(Attack):
    __slots__ = 'stat', 'test', 'uses'
    def __init__(self, toHitRoll, damage, stat = 'ac', test='{0}', uses = float('inf')):
        super().__init__(toHitRoll, damage)
        self.stat = stat
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
    
    from Character import Character, Stats
    a = Attack('d20+1', 'd8+1')
    b = Spell('d20+3','d8',stat='dex', test='13-modifier({0})', uses=5)
    Adam = Character(Stats((12,11,10,10,14,17,10,16)), [])

    for _ in range(10):
        a.execute(Adam, (Adam,))
        b.execute(Adam, (Adam,))
    print(a, Adam)
