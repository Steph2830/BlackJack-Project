import random
import db as db

def betAmount():
    maxBet = db.showMoney()
    while True:
        bet = float(input("How much would you like to bet? Pick an amount between 5 and 1000"))
        if bet <= 4 or bet > 1000:
            print("You must enter a bet between 5 and 1000")
            continue
        if bet > float(maxBet):
            print("You only have " +maxBet+ "chips left to bet")
            continue
        endChips = db.betMoney(bet)
        return bet

def firstChoice():
    while True:
        choice = input("Would you like to play?(Y/N)")
        if choice.lower() == "y":
            return choice
        if choice.lower() == "n":
            print("Thanks for playing,Goodbye")
            exit()
        else:
            print("Invalid input, please enter y or n")
            continue

def createCards():
    suits = ["♠", "♥", "♣", "♦"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

    deck = []
    for suit in suits:
        counter = 0
        for rank in ranks:
            createdCard = []
            createdCard.append(suit)
            createdCard.append(rank)
            createdCard.append(values[counter])
            deck.append(createdCard)
            counter += 1
    return deck

def main():
    deck = createCards()
    # print welcome message(main)
    print("THIS IS BLACKJACK!!")
    print()
    # get money text file/read balance(db)
    chips = db.showMoney()
    print("You have " + chips+ " chips to play with")
    # get user input "Do you want to play yes or no"(function)
    choice = firstChoice()
    # get enter by wager amount(possible function)
    bet = betAmount()
# create deck(function,must have global scope)
# deal to player and dealer(function)
# get scores(function)
# print dealer hand with a blank card(main)
# print player hand(main)
# check for double aces(main)
# check for player score(possible function,or while loop)
    # if player is dealt 21,player wins and wager x1.5 to money
    # if player score is <= 21,ask player if they want to hit or stand
    # if player hits,add new card to player hand
    # if player scores over 21.player busts

# check dealer score(main)
    # if score is <= 16,and player score is <= 21,dealer must hit and get new card
    # if dealer gets 21,dealer wins
    # if dealer gets over 21 they bust

# print player score(main)
# print dealer score(main)
# determine who won(main)
    # player loses if they score less then dealer

#how to win(function)
    # when player score = dealer score,return player's wager as win
    # if player loses,no money added
    # if player score greater then dealer score, player gets wager returned x 1.5

# check avaiable money(function)
    # check to see if lower then $4, if yes ask if they want to add more money

# check deck length(main)
    # should be <= 26,if less then 26, half of deck has been used, reshuffle needed

# make new deck

if __name__ == "__main__":
    main()
