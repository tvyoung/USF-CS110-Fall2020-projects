#program should deal cards arbitrarily and at the same time to each player until one player’s hand is worth more than 21 points
#when that happens, the other player is the winner. it is possible that both players’ hands will simultaneously exceed 21 points, in which case neither player wins. 
#if a player is dealt an ace, the program should decide the value of the card according to the following rule: the ace will be worth 11 points, unless that makes the player’s hand exceed 21 points. In that case, the ace will be worth 1 point
#extra credit: program deals cards randomly rather than arbitrarily from the deck
import random

# Global constant for the winning number of cards
MAX = 21

# main function
def main():
    # Local variables
    hand1 = 0
    hand2 = 0
    deck = create_deck()

    #creates deck_keys list
    deck_keys = []
    #adds all the keys in deck dictionary to deck_keys as list items
    for item in deck.keys():
        deck_keys.append(item)

    #for testing:
    #print(deck_keys)

    #TODO - Deal a card to each player and calculate hand value. 
    #while hand1 or hand2 is less than MAX, continue to loop and deal cards to both players
    #while loop will end when one player's hand equals MAX or exceeds MAX
    while hand1 < MAX and hand2 < MAX:
        #deal one card randomly from deck dictionary to player 1
        #creates index variable; returns a random int between 0 and the length of deck_keys list
        index = random.randint(0, len(deck_keys)-1)
        #creates card variable; returns an item (card name) with random index number from deck_keys
        card = deck_keys[index]
        #removes item (card name) from deck_keys list
        deck_keys.remove(deck_keys[index])
        #print what player 1 was dealt
        print("player 1 was dealt", card)
        #returns value associated with specified key in deck as well as removes key-value pair
        value = deck.pop(card)
        #update value of player 1's hand given what they were dealt
        hand1 = update_hand_value(hand1, value, card)

        #deal one card randomly from deck dictionary to player 2
        index = random.randint(0, len(deck_keys)-1)
        #creates card variable; returns an item (card name) with random index number from deck_keys
        card = deck_keys[index]
        #removes item (card name) from deck_keys list
        deck_keys.remove(deck_keys[index])
        #print what player 2 was dealt
        print("player 2 was dealt", card)
        #returns value associated with specified key in deck as well as removes key-value pair
        value = deck.pop(card)
        #update value of player 2's hand given what they were dealt
        hand2 = update_hand_value(hand2, value, card)

    print("value of player 1's hand:", hand1)
    print("value of player 2's hand:", hand2)

    #TODO Determine the winner.
    #if the value of player 1's hand AND player's 2 hand both equal MAX, both players win
    if hand1 == MAX and hand2 == MAX:
        print("both players win.")
    #if the value of player 1's hand AND player 2's hand both go over MAX, no one wins
    elif hand1 > MAX and hand2 > MAX:
        print("there is no winner.")
    #if the value of player 1's hand is MAX OR player 2's hand exceeds MAX, player 1 wins
    elif hand1 == MAX or hand2 > MAX:
        print("player 1 wins.")
    #if the value of player 2's hand is MAX OR player 1's hand exceeds MAX, player 2 wins
    elif hand2 == MAX or hand1 > MAX:
        print("player 2 wins.")


# The create_deck function creates a deck of cards and
# returns the deck.
def create_deck():
    # Set up local variables
    suits = ['Spades','Hearts','Clubs','Diamonds']
    special_values = {'Ace':1, 'King':10, 'Queen':10, 'Jack':10}

    # Create list of all the card values
    numbers = ['Ace', 'King', 'Queen', 'Jack']
    for i in range(2,11):
        numbers.append(str(i))

    # Initialize deck
    deck = {}
    for suit in suits:
        for num in numbers:
            #TODO Add the numbers 2-10 to the deck [Hint: you will need to check if the value is numeric]
            #if num in numbers contains numeric digits, converts to int in value variable
            if num.isdigit():
                value = int(num)
            #TODO Add the Ace, King, Queen, or Jack values to the deck using the dictionary special_values.
            #if does not contain numeric digits, meaning num in numbers cannot be converted to an int, then uses num as the key in special_values to return its associated value
            else:
                value = special_values[num]
            #creates cardName variable to store concatenated card name string
            cardName = num + " of " + suit
            #adds cardName as the key and value as its associated value to the deck
            deck[cardName] = value

    return deck


# TODO Given the player's current hand, the value of the card they were just dealt
# and the name of the card they were just dealt, return the new value of their hand 
# Remember: If a player is dealt an ace, the program should decide the value by:
# The ace will be worth 11 points, unless that makes the player's hand exceed 21 points.
# In that case the ace will be worth 1 point.
def update_hand_value(hand, value, card):
    #if "Ace" is in the card name, meaning if it is an ace card
    if "Ace" in card:
        #if the ace card with value 11 points added to the player's hand exceeds 21,
        #will change the value of the ace card to 1 point.
        #if (hand+11) == Max, ace card value will NOT change to 1 point.
        if (hand + 11) > MAX:
            value = 1
        else:
            value = 11

    #adds value to hand
    hand += value
    #returns the new value of the hand
    return hand
  

# Call the main function
main()