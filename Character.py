class Stats():
    def __init__(self, stats):
        self.str,self.con,self.dex,self.int,self.wis,self.cha,self.max_hp,self.ac = stats

    def __repr__(self):
        return str(self)
    def __str__(self):
        return f'''str: {self.str}
con: {self.con}
dex: {self.dex}
int: {self.int}
wis: {self.wis}
cha: {self.cha}
hp: {self.hp}
ac: {self.ac}'''
        
class Character():
    def __init__(self, stats, attacks):
        self.stats = stats
        self.attacks = attacks
        self.hp = stats.max_hp
        
    def attack(self, target, attack):
        attack.execute(target)

    def restore(self):
        self.hp = self.stats.max_hp

    def target(self, targets):
        best_target = None
        max_dps = 0
        for target in targets:
            for attack in target.attacks:
                hit, miss = 0, 0
                for _ in range(100):
                    if attack.hits():
                        hit += 1
                    else:
                        miss += 1
                dps = hit / (hit + miss) * attack.damage.expected
                if dps > max_dps:
                    best_target = target
                    max_dps = dps
        return best_target

    def pick_attack(self, targets):
        best_attack = None
        max_dps = 0
        for target in targets:
            for attack in self.attacks:
                hit, miss = 0, 0
                for _ in range(100):
                    if attack.hits():
                        hit += 1
                    else:
                        miss += 1
                dps = hit / (hit + miss) * attack.damage.expected
                if dps > max_dps:
                    best_attack = attack
                    max_dps = dps
        return best_attack
        
    def __repr__(self):
        return 'Character\n'+str(self.stats)+'\n'+str(self.attacks)
    def __str__(self):
        return 'Character\n'+str(self.stats)
