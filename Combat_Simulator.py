Adam = Character(stats(12,11,10,10,14,17,10,16},
                 [Attack('d20+1', 'd8+1'),Attack('d20+1', 'd10+1'),])
Oscar = Character(stats(16,14,'dex':13,'int':11,'wis':3,'cha':11, 'hp':12, 'ac':16},
                  [Attack('d20+3', 'd8+3'),Attack('d20+1', 'd10+1'),])
James = Character({'str':8, 'con':12,'dex':10,'int':12,'wis':17,'cha':6, 'hp':9, 'ac':12},
                  [Attack('d20', 'd8', stat='dex', test='13-{0}')])
Nikko = Character({'str':8, 'con':11,'dex':13,'int':18,'wis':11,'cha':6, 'hp':8, 'ac':13},
                  [Attack('d20', 'd8', stat='dex', test='14-{0}')])

characters = [Adam, Oscar, James, Nikko]
enimies = []
