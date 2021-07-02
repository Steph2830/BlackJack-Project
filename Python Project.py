# Function to print the cards
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
	
	# The Card Class definition
class Card:
	def __init__(self, suit, value, card_value):
		
		# Suit of the Card like Spades and Clubs
		self.suit = suit

		# Representing Value of the Card like A for Ace, K for King
		self.value = value

		# Score Value for the Card like 10 for King
		self.card_value = card_value
