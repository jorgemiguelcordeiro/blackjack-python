from blackjack.deck import Deck
from blackjack.player import Player, Dealer


'''
This class coordinates all the game.
First we shuffle, then we deal, then player decides, then dealer decides, then we judge the winner.

'''

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()  # creates a new 52-card deck in permanent memory. If we used here local variables (instead of self), those variables vanish the moment the __init__ function finishes running.
        self.player = Player("Player") # creates the human user 
        self.dealer = Dealer("Dealer") # creates the dealer

    

    def player_turn(self):
        """
        Handles the Hit/Stand loop. Returns False if player busts, True otherwise.
        This forces the player to keep making choices until the turn is essentially over.
        """
        while True:
            choice = input("\nDo you want to (H)it or (S)tand? ").strip().lower() #removes accidental spaces and lwoercase
            
            
            #if the user wants a card
            if choice in ['h', 'hit']:
                new_card = self.deck.deal()  #get a card from the deck
                print(f"You drew a {new_card}")
                self.player.receive_card(new_card) #give the card to the player
                self.player.show_hand()  #showing the hand

                #in here we check the @property total. 
                if self.player.total > 21:
                    print("Bust! You went over 21. Dealer wins.")
                    return False # turn is over
                
            # if the user wants to stop
            elif choice in ['s', 'stand']:
                print("You chose to stand.")
                return True # Player stood
            
            #some input validation
            else:
                print("Invalid input. Please enter 'h' or 's'.")

    def dealer_turn(self):
        """
        Dealer reveals card and hits according to should_hit
        """
        # 1 - First step of the dealer's phase is to flip the hidden card
        print("\nDealer's Turn")
        # Reveal the face-down card
        self.dealer.show_hand(hide_first_card=False)

        # 2 - we use the logic of should_hit. The Dealer must hit if their total is 16 or less
        while self.dealer.should_hit():
            print("Dealer hits...")
            new_card = self.deck.deal()
            self.dealer.receive_card(new_card)
            self.dealer.show_hand(hide_first_card=False)

        if self.dealer.total > 21:
            print("Dealer busted!")
        else:
            print("Dealer stands.")

    def determine_winner(self):
        """Compares totals to find the winner."""

        #we convert final scores into local variables for easier reading

        p_total = self.player.total
        d_total = self.dealer.total

        print(f"\nFinal Scores -> You: {p_total} | Dealer: {d_total}")

        if d_total > 21:
            print("Dealer busted. You win!")
        elif p_total > d_total:
            print("You win!")
        elif d_total > p_total:
            print("Dealer wins.")
        else:
            print("It's a push (tie).")


    # main loop of the game
    def play_round(self):  
        print("\nA new round is starting")
        
        # 1. Shuffle
        self.deck.shuffle()

        # 2. Initial Deal (2 cards for player and dealer)
        for x in range(2):
            #removes a card from the deck self.deck.deal() and takes the return card and puts it into the hand list.
            self.player.receive_card(self.deck.deal())
            self.dealer.receive_card(self.deck.deal())

        
        '''
        In the begginign of game, the player sees everything they have.
        The dealer hides their first card (using the logic we wrote in player.py)
        '''

        # 3. Show Initial State
        # Player shows all
        self.player.show_hand()
        # Dealer shows one face up, one face down
        self.dealer.show_hand(hide_first_card=True)


        # Only if the player survives (returns True) do we proceed to the Dealer's turn. If they bust, we skip the rest.
        # 4. Player's Turn
        if self.player_turn():
            # If player didn't bust, proceed to Dealer's Turn
            self.dealer_turn()
            # 6. Determine Winner
            self.determine_winner()
        
        print("\nGame Over")

def main():
    game = BlackjackGame()
    game.play_round()

if __name__ == "__main__":
    main()