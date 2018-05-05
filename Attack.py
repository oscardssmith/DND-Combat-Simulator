from Die_Simulator import die_parse

class Attack:
    def __init__(self, toHitRoll, damage, stat = 'ac', test='{0}', uses = float('inf')):
        self.toHitRoll=die_parse(toHitRoll)
        self.stat=stat
        self.damage=die_parse(damage)
        self.test=test
        self.uses=uses
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return '{0}x {1} to hit, {2} damage'.format(uses,toHitRoll,damage)
    
    def execute(attacker,targets):
        self.uses-=1
        for target in targets:
            if self.hits(attacker, target):
                target.hp-=damage.roll()

    def hits(self, attacker, target):
        toHitRoll.roll()
        threshold=eval(test.format(target[stat]))
        return ToHitRoll > threshold
