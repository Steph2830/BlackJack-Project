import random
import db as db

def addChips():
    while True:
        addChips = input("You don't have enough chips left to bet, would you like to add more? (Y/N)")
        

def determineWin(playerScore, dealerScore):
    if playerScore == dealerScore:
        print("Game is tied")
        return 0
    if playerScore > 21:
        print("You lost fool")
        return -1
    if dealerScore > 21:
        print("You win, dealer sucks")
        return 1
    if playerScore > dealerScore:
        print("Player Wins")
        return 1
    if playerScore < dealerScore:
        print("Player loses")
        return -1


def getPlayerScore(playerCards):
    playerScore = 0
    i = 0
    for i in range(len(playerCards)):
        amount = playerCards[i][2]
        playerScore = playerScore + amount
        i += 1
    return playerScore

def getDealerScore(dealerCards):
    dealerScore = 0
    i = 0
    for i in range(len(dealerCards)):
        amount = dealerCards[i][2]
        dealerScore = dealerScore + amount
        i += 1
    return dealerScore

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
    # print welcome message
    print("THIS IS BLACKJACK!!")
    print()
    # get money text file/read balance
    chips = db.showMoney()
    print("You have " + chips + " chips to play with")
    while True:
        # get user input "Do you want to play yes or no"
        choice = firstChoice()
        # get enter by wager amount
        bet = betAmount()
        # deal to player and dealer
        playerCards = []
        playerCard = random.choice(deck)
        playerCards.append(playerCard)
        deck.remove(playerCard)
        dealerCards = []
        dealerCard = random.choice(deck)
        dealerCards.append(dealerCard)
        deck.remove(dealerCard)
        playerCard = random.choice(deck)
        playerCards.append(playerCard)
        deck.remove(playerCard)
        dealerCard = random.choice(deck)
        dealerCards.append(dealerCard)
        deck.remove(dealerCard)
        print("DEALER CARDS:")
        print(dealerCards[0][1], dealerCards[0][0])
        print("??????")
        print("PLAYER CARDS:")
        for card in playerCards:
            print(card[1], card[0])
        # get scores(function)
        playerScore = getPlayerScore(playerCards)
        dealerScore = getDealerScore(dealerCards)
        # check for double aces

        # check for player score
        if playerScore == 21:
            print("YOU JUST GOT BLACKJACK!!!!!! YOU WIN!!!")
            bet = db.winMoney()
        # if player score is <= 21,ask player if they want to hit or stand
        while playerScore <= 21:
            secondChoice = input("Would you like to hit or stand?(H/S)")
            # if player hits,add new card to player hand
            if secondChoice.lower() == "h":
                playerCard = random.choice(deck)
                playerCards.append(playerCard)
                deck.remove(playerCard)
                playerScore = getPlayerScore(playerCards)
                print("PLAYER CARDS:")
                for card in playerCards:
                    print(card[1], card[0])
                continue
            if secondChoice.lower() == "s":
                print("DEALER CARDS:")
                for card in dealerCards:
                    print(card[1], card[0])
                break
            else:
                print("You must enter either h or s")
                continue
            # if player scores over 21.player busts
        if playerScore > 21:
            print("BUSTEDDDDDDD!!! YOU LOST!")
            break

        # if score is <= 16,and player score is <= 21,dealer must hit and get new card
        while True:

            if playerScore > 21:
                break

            elif dealerScore > 17:
                break

            elif dealerScore <= 16:
                print("Dealer is hitting")
                dealerCard = random.choice(deck)
                dealerCards.append(dealerCard)
                deck.remove(dealerCard)
                print(dealerCard[1], dealerCard[0])
                dealerScore = getDealerScore(dealerCards)

        if dealerScore > 21:
            print("BUSTEDDDDD!")

        if dealerScore == 21:
            print("DEALER GOT BLACKJACK!")

        # print player score
        print("player score " + str(playerScore))
        # print dealer score
        print("dealer score " + str(dealerScore))
        # determine who won
        checkWin = determineWin(playerScore, dealerScore)
        if checkWin == 0:
            endChips = db.winMoney(bet)
        if checkWin == 1:
            endChips = db.winMoney(bet * 1.5)
        # check avaiable money

        # check to see if lower then $4, if yes ask if they want to add more money

    # check deck length(main)
        # should be <= 26,if less then 26, half of deck has been used, reshuffle needed

    # make new deck

if __name__ == "__main__":
    main()

