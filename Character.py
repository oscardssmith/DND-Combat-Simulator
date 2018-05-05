class Stats():
    __slots__ = 'str', 'con', 'dex', 'int', 'wis', 'cha', 'max_hp', 'ac'
    
    def __init__(self, stats):
        if  isinstance(stats, dict):
            self.str = stats['str']
            self.con = stats['con']
            self.dex = stats['dex']
            self.int = stats['int']
            self.wis = stats['wis']
            self.cha = stats['cha']
            self.max_hp = stats['max_hp']
            self.ac =stats['ac']
        else:
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
max hp: {self.max_hp}
ac: {self.ac}'''
        
class Character():
    __slots__ = 'stats', 'attacks', 'hp'
    
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
                if attack.uses > 0:
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
                if attack.uses > 0:
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
        return f'Character\n{self.stats}\nhp: {self.hp}\n{self.attacks}'
    def __str__(self):
        return f'Character\n{self.stats}\nhp: {self.hp}'

if __name__ == '__main__':
    from Attack import Attack, Spell

    a = Attack('d20+1', 'd8+1')
    b = Spell('d20+3','d8',stat='dex', test='13-modifier({0})', uses=5)
    Adam = Character(Stats((12,11,10,10,14,17,10,16)), [a,b])
    print(Adam)
