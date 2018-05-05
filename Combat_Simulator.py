from Character import Character, Stats
from Attack import Attack, Spell
from Die_Simulator import die_parse,modifier
from time import time

Adam = Character(Stats((12,11,10,10,14,17,10,16)),
                 [Attack('d20+1', 'd8+1'),Attack('d20+1', 'd10+1'),])
Oscar = Character(Stats((16,14,13,11,3,11,12,16)),
                  [Attack('d20+3', 'd8+3'),Attack('d20+1', 'd10+1'),])
James = Character(Stats((8, 12,10,12,17,6, 9, 12)),
                  [Spell('d20', 'd8', stat='dex', test='13-modifier({0})')])
Nikko = Character(Stats((8, 11,13,18,11,6, 8, 13)),
                  [Spell('d20', 'd8', stat='dex', test='14-modifier({0})')])

characters = [Adam, Oscar, James, Nikko]
enemies = []

for i in range(3,21):
    enemies.append(Character(Stats((i,i,i,i,i,i,i,i)),[]))

t1 = time()
for i in range(0,10000):
    for character in characters:
        #print(character)
        for attack in character.attacks:
            totals = [0]*len(range(3,21))
            i=0
            for enemy in enemies:
                attack.execute(character,(enemy,))
                totals[i]+=enemy.stats.max_hp-enemy.hp
                enemy.restore()
                i+=1
            #print(totals)
#print(characters)
print(time()-t1)
