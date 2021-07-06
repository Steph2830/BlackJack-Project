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
