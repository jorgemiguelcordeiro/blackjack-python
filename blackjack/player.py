
'''
Since we must use OOP, we are going to take advantage of Inheritance.
Instead of writing code for a Player and then writing almost the exact same code for a Dealer, we create a shared parent class called Person. 
Both the Player and the Dealer are "Persons" in the context of this game—they both have names, they both hold cards, and they both need to calculate their totals.
'''


class Person:  #parent class - foundation for player and dealer
    def __init__(self, name):
        self.name = name  #it requires the name "Dealer" or "Player"
        self.hand = []  #empty list to hold the card integers

    def receive_card(self, card): #method to accept a card dealt from the Deck

        if card:  #to make sure the deck is not empty
            self.hand.append(card) #add to the end of the list



    '''
    The @property decorator turns a function into something that looks like a variable.
    If we used a normal variable, like self.XYZ. When player hits (self.hand.append(card))
    self.hand would change, but not self.XYZ

    We would have to do something like this, by not using @property. Not feasible:

    def receive_card(self, card):
        self.hand.append(card)       
        self.total = sum(self.hand)  
    
    '''
    @property
    def total(self): 
        
        return sum(self.hand)  #Total value of the hand.
    
    '''
    in this game, we need to show the cards constantly
    after the deal, after the player and dealer hits and at the end.
    However, at the start of each game, the Dealer hides their first card.
    '''

    def show_hand(self, hide_first_card=False):

        

        if hide_first_card:  #beggining of the game - Dealer hides their first card.

            print(f"{self.name}'s Hand: [Hidden Card], {self.hand[1:]}") #list slicing - It skips index 0 (the first card).
            print(f"{self.name}'s Visible Total: {self.hand[1]}") #value of the second card

        else:  
            print(f"{self.name}'s Hand: {self.hand}") 
            print(f"{self.name}'s Total: {self.total}")


#human user - we just need to copy from Person. No automatic rules - user makes choices via input()
class Player(Person):
    
    pass   

class Dealer(Person):
    
    #instructions from the assignment 
    def should_hit(self):
        """
        Dealer must hit if total is 16 or less.
        Dealer must stand if total is 17 or more.
        """
        return self.total <= 16