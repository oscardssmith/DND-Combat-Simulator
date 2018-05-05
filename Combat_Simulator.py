from Character import Character, Stats
from Attack import Attack
from Die_Simulator import die_parse

Adam = Character(Stats((12,11,10,10,14,17,10,16)),
                 [Attack('d20+1', 'd8+1'),Attack('d20+1', 'd10+1'),])
Oscar = Character(Stats((16,14,13,11,3,11,12,16)),
                  [Attack('d20+3', 'd8+3'),Attack('d20+1', 'd10+1'),])
James = Character(Stats((8, 12,10,12,17,6, 9, 12)),
                  [Attack('d20', 'd8', stat='dex', test='13-{0}')])
Nikko = Character(Stats((8, 11,13,18,11,6, 8, 13)),
                  [Attack('d20', 'd8', stat='dex', test='14-{0}')])

characters = [Adam, Oscar, James, Nikko]
enimies = []

print(characters)
