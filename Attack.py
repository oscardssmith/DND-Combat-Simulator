print("hi")

class Attack:
    def __init__(self, toHitRoll, damage, stat = 'ac', test='{0}'):
        self.ToHitRoll=parse_dice(ToHitRoll)
        self.stat=stat
        self.damage=parse_dice(damage)
        self.test=test
    
    def execute(attacker,targets):
        for target in targets:
            ToHitRoll.roll()
            threshold=eval(test.format(target[stat]))
            if(ToHitRoll>threshold):
                target['hp']-=damage.roll()
