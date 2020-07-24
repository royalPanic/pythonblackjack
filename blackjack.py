# === Imports ===
import random as r

# === Variables ===
cards = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
cardvalues = {"Ace": 11, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}
deck = [] # master deck array
househand = []
userhand = []
HRUD = [] # Human readable user-deck
HRHD = [] # Human readable house-deck

# === Class and Function Defs ===
class card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __str__(self):
        return str(self.value)+" of "+str(self.suit)
    def stringform(self):
        test = self.value()+" of "+self.suit()
        return test

def createDeck():
    global deck
    for c in cards:
        for s in suits:
            deck.append(card(s, c))

def deal(amount, hand):
    global deck
    for x in range(amount):
        hand.append(deck.pop(0))

def handConvert(hand, endhand):
    for entry in hand:
        result = str(entry)
        endhand.append(result)
    return endhand

# === Run Code ===
createDeck()
for x in range(10):
    r.shuffle(deck)
deal(1, househand)
deal(2, userhand)
handConvert(userhand,HRUD)
print(str(HRUD))
