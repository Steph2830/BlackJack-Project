import random
import os
import time

# Card class Definition
class card:
    def __init__(self, suit, value, cardValve):

        #Suit of the Card(Spades,Clubs,Hearts,Diamonds)
        self.suit = suit

        #Value of the Card
        self.value = value

        #Score Value of the Card
        self.cardValue = cardValue

#Function to clear the Terminal
    def clear():
        os.system("clear")

#Function for Printing the Cards
    def print_cards(cards, hidden):

        s = ""
        for card in cards:
            s = s + "\t ________________"
        if hidden:
            s += "\t ________________"
        print(s)


        s = ""
        for card in cards:
            s = s + "\t|                |"
        if hidden:
            s += "\t|                |"		
        print(s)

        s = ""
        for card in cards:
            if card.value == '10':
                s = s + "\t|  {}            |".format(card.value)
            else:
                s = s + "\t|  {}             |".format(card.value)	
        if hidden:
            s += "\t|                |"		
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        if hidden:
            s += "\t|      * *       |"	
        print(s)	

        s = ""
        for card in cards:
            s = s + "\t|                |"
        if hidden:
            s += "\t|    *     *     |"	
        print(s)	

        s = ""
        for card in cards:
            s = s + "\t|                |"
        if hidden:
            s += "\t|   *       *    |"	
        print(s)	

        s = ""
        for card in cards:
            s = s + "\t|                |"
        if hidden:
            s += "\t|   *       *    |"	
        print(s)	

        s = ""
        for card in cards:
            s = s + "\t|       {}        |".format(card.suit)
        if hidden:
            s += "\t|          *     |"	
        print(s)	

        s = ""
        for card in cards:
            s = s + "\t|                |"
        if hidden:
            s += "\t|         *      |"	
        print(s)	

        s = ""
        for card in cards:
            s = s + "\t|                |"
        if hidden:
            s += "\t|        *       |"	
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        if hidden:
            s += "\t|                |"	
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        if hidden:
            s += "\t|                |"	
        print(s)	

        s = ""
        for card in cards:
            if card.value == '10':
                s = s + "\t|            {}  |".format(card.value)
            else:
                s = s + "\t|            {}   |".format(card.value)
        if hidden:
            s += "\t|        *       |"			
        print(s)	
            
        s = ""
        for card in cards:
            s = s + "\t|________________|"
        if hidden:
            s += "\t|________________|"	
        print(s)		

        print()                       

        #Function for a game of blackjack
    def blackjackGame(deck):

        #Cards for Dealer and Player
        playerCards = []
        dealerCards = []

        # Scores for the Dealer and Player
        playerScore = 0
        dealerScore = 0


    clear()

    #First dealing for player and dealer
    while len(playerCards) <2:

        #Deal a random card
        playerCard =random.choice(deck)
        playerCards.append(playerCard)
        deck.remove(playerCard)

        #Update player score
        playerScore += playerCard.cardValue

        #If both cards are Ace,make the first Ace value 1
        if len(playerCards) == 2:
            if playerCards[0].cardValue == 11 and playerCards[1].cardValue == 11:
                playerCards[0].cardValue = 1
                playerScore -= 10

        #Print player cards and score
        print("PLAYER CARDS:")
        printCards(playerCards, False)
        print("PLAYER SCORE =",playerScore)

        input()

        #Deal a random card
        dealerCard = random.choice(deck)
        dealerCards.append(dealerCard)
        deck.remove(dealerCard)

        #Update dealer score
        dealerScore += dealerCard.cardValue

        #Print dealer cards and score,but hide the second card and the score
        print("DEALER CARDS:")
        if len(dealerCards) == 1:
               printCards(dealerCards, False)
               print("DEALER SCORE =",dealerScore)
        else:
            printCards(dealerCards[:-1],True)
            print("DEALER SCORE =" dealerScore - dealerCards[-1].cardValue)

        # In case both the cards are Ace, make the second ace value as 1 
	if len(dealer_cards) == 2:
		if dealer_cards[0].card_value == 11 and dealer_cards[1].card_value == 11:
			dealer_cards[1].card_value = 1
			dealer_score -= 10

        input()    


