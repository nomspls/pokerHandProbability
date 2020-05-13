import random
import pandas as pd

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
class Deck: 
    def ranks(self):
        #return ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
        # return ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        return ['2','3','4','5','6','7','8','9','10','11','12','13','14']
    
    def suits(self):
        #return ['clubs', 'diamonds', 'hearts', 'spades']
        return ['c', 'd', 'h', 's']
    
    def __init__(self):
        self.full = []
        self.full = [Card(rank,suit) for rank in self.ranks() for suit in self.suits()]
        
    def fullDeck(self):
        self.fulldeck = [str(self.full[nr]) for nr in range(len(self.full))]
        return self.fulldeck
        
    def drawHand(self, n):
        return random.sample(self.full, n)
    
    def remover(self, cards):
        self.left = set(self.full) - set(cards)
        return self.left
    
    def drawRiver(self, n):
        return random.sample(self.left, n)


def checkFlush(suits):
    for letter in deck.suits():
        if suits.count(letter) >= 5:
            return True
   
def checkStraight(ranks):
    straight = []
    for n in range(9):
        straight1 = '23456'
        straight2 = [int(straight1[0]) + n,int(straight1[1]) + n,int(straight1[2]) + n,int(straight1[3]) + n,int(straight1[4]) + n]
        straight.append(''.join(map(str, straight2)))
    tmp =list(set(ranks))
    tmp.sort(key=float)
    temp = ''.join(tmp)
    if any(sublist in temp for sublist in straight):
        return True
    elif '2345' in temp and temp[-1] == '14':
        return True
    
def check4(ranks):
    for rank in deck.ranks():
        if ranks.count(rank) == 4:
            return True
        
def check3(ranks):
    for rank in deck.ranks():
        if ranks.count(rank) == 3:
            return True 
        
def checkFH(ranks):
    if check3(ranks):
        for rank in deck.ranks():
            if ranks.count(rank) == 2:
                return True
            
def checkStraightFlush(ranks, suits):
    if checkFlush(suits) and checkStraight(ranks):
        return True

def checkRoyalFlush(ranks,  suits):
    if checkFlush(suits) and checkStraight(ranks):
        if '1011121314' in ''.join(sorted(set(ranks))):
            return True

def checkPair(ranks):
    for rank in deck.ranks():
        if ranks.count(rank) == 2:
            return True 
        
def check2Pair(ranks):
    if checkPair(ranks) == True and checkFH(ranks) != True:
        if len(set(ranks)) < 6:
            return True
        
def checkPoker(poker):
    ranks, suits = [obj.rank for obj in poker], [obj.suit for obj in poker]
    
    if checkRoyalFlush(ranks, suits):
        return 'Royal flush'    
    elif checkStraightFlush(ranks, suits):
        return 'Straight flush'
    elif check4(ranks):
        return 'Four of a kind'
    elif checkFH(ranks):
        return 'Full house'
    elif checkFlush(suits):
        return 'Flush'
    elif checkStraight(ranks):
        return 'Straight'
    elif check3(ranks):
        return 'Three of a kind'
    elif check2Pair(ranks):
        return 'Two pair'
    elif checkPair(ranks):
        return 'One pair'
    else:
        return 'High card'


if __name__ == '__main__':
    deck = Deck()
    outcomes = []
    
    for i in range(1000):
        hand = set(deck.drawHand(2))
        deck.remover(hand) 
        river = set(deck.drawRiver(5))
        poker = river.union(hand)
        outcomes.append(checkPoker(poker))
    #print('\n'.join(outcomes))
            
    df = pd.DataFrame(outcomes, columns=['outcome'])
    df.index.name = 'Tries'
    df.index += 1
    df.to_csv('handData.csv')
    
    
    
    
    # print("River:\n"+"\n".join(map(str, river)))
    # print("\nYour hand:\n"+"\n".join(map(str, hand)))

    # print(checkPoker(poker))
