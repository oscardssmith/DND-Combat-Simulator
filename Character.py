class Stats():
    def __init__(self, stats):
        self.str,self.con,self.dex,self.int,self.wis,self.cha,self.hp,self.ac = stats

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
        
    def attack(self, target, attack):
        attack.execute(target)

    def __repr__(self):
        return 'Character\n'+str(self.stats)+'\n'+str(self.attacks)
    def __str__(self):
        return 'Character\n'+str(self.stats)
