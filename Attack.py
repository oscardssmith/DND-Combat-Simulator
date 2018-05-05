from Die_Simulator import die_parse

class Attack:
    def __init__(self, toHitRoll, damage, stat = 'ac', test='{0}'):
        self.toHitRoll=die_parse(toHitRoll)
        self.stat=stat
        self.damage=die_parse(damage)
        self.test=test
    
    def execute(attacker,targets):
        for target in targets:
            toHitRoll.roll()
            threshold=eval(test.format(target[stat]))
            if(ToHitRoll>threshold):
                target['hp']-=damage.roll()
