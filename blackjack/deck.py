import random  

#This defines what a Deck is (it has a list of cards) and what it does (it can shuffle and deal).
#The deck manages its own internal data. 
#The game doesn't need to know how the cards are stored or shuffled; it just asks the deck to "deal" or "shuffle".
class Deck: 

    def __init__(self): #This is the "starter button." As soon as you create a new Deck, this function runs automatically. "Self" allows the code to distinguish between "Deck A" and "Deck B".
        
        self.cards = [] #the brain of this class is the variable self.cards. Creates an empty list named cards and attaches it to self. This initializes the "state" of the object. Every deck starts with an empty inventory.
        self.build() #the deck is ready to use the moment it exists.


    def build(self): #Defines a method named build. It takes self so it can access and modify the self.cards variable belonging to this object.
        """
        Creates a standard 52-card deck using simplified values.
        Cards 2-9 are face value. 10, J, Q, K are 10. A is 11.
        """

        # List of Values 2 through 9
        numbered_cards = list(range(2, 10))

        # Result: [10, 10, 10, 10]. This represents the 10, Jack, Queen, and King.
        face_cards = [10] * 4

        # Aces are worth 11
        aces = [11]

        # a suit (naipe) that Concatenates the three lists together
        one_suit = numbered_cards + face_cards + aces
        
        # A deck has 4 suits. It stores the final list into self.cards
        #we need to attach this to self.cards (permanent memory) to use later in shuffle and deal
        self.cards = one_suit * 4 

    def shuffle(self):
        
        random.shuffle(self.cards) #Randomizes the order of the deck.

    def deal(self): 
    # defines the method to remove and return a card
    # when we deal a card, we need to know what card it is and the card must leave the deck so it cannot be dealt again.
    # based on this, we can't use index access (deck[0]), neither the method .remove

        if len(self.cards) > 0:
            return self.cards.pop() #removes the item and returns
        else:
            return None #allows the game.py to know that the deck has run out