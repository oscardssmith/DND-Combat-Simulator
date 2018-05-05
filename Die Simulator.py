import random

class Die():
    '''
        1 is the loneliest number of dice.
        It either has some faces or is just a plain old x sided die.
    '''
    
    def __init__(self, maximum=6, faces=None):
        '''
            Takes in a maximum or a sequence of faces.
            If faces are given, picks from that distribution.
            Otherwise, it is a standard dice with the maximum value d6 default
        '''
        
        self.maximum = maximum
        if faces = None:
            self.faces = range(1, maximum + 1)
        else:
            self.faces = faces
        
    def roll(self):
        ''' Returns a random face.'''
        return random.choice(self.faces)

    def __repr__(self):
        if self.faces == range(1, self.maximum + 1):
            return 'd' + str(self.maximum)
        return 'Die('+str(faces)+')'

class DiceList(list):
    ''' A list of Die '''
    
    def roll(self):
        ''' Returns the sum of the die. '''
        val = 0
        for die in self:
            val += die.roll()
        return val
        
def die_parse(dice):
    '''takes in a string like 4d6+d8+3 and turns it into a DiceList'''
    dice_strings = dice.split('+')
    dice = DiceList()
    for die in dice_strings:
        print(die)
        if 'd' not in die:
            dice.append(Die(int(die)))
        else:
            parts = die.split('d')
            print(parts)
            if parts[0] == '':
                dice.append(Die(int(parts[1])))
            else:
                for num in range(int(parts[0])):
                    dice.append(Die(int(parts[1])))
    return dice

a = DiceList((Die(6),Die(8)))
b = die_parse('4d6+d8+3')
print(a,b)
