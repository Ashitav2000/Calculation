import random


# Deck creation
def forming_pack():
    # Define the deck of cards with their values
    pack = {"2 of hearts": 2, "3 of hearts": 3, "4 of hearts": 4, "5 of hearts": 5,
            "6 of hearts": 6, "7 of hearts": 7, "8 of hearts": 8, "9 of hearts": 9,
            "10 of hearts": 10, "Jack of hearts": 10, "Queen of hearts": 10, "King of hearts": 10,
            "Ace of hearts": 11, "2 of diamonds": 2, "3 of diamonds": 3, "4 of diamonds": 4,
            "5 of diamonds": 5, "6 of diamonds": 6, "7 of diamonds": 7, "8 of diamonds": 8,
            "9 of diamonds": 9, "10 of diamonds": 10, "Jack of diamonds": 10, "Queen of diamonds": 10,
            "King of diamonds": 10, "Ace of diamonds": 11, "2 of clubs": 2, "3 of clubs": 3,
            "4 of clubs": 4, "5 of clubs": 5, "6 of clubs": 6, "7 of clubs": 7,
            "8 of clubs": 8, "9 of clubs": 9, "10 of clubs": 10, "Jack of clubs": 10,
            "Queen of clubs": 10, "King of clubs": 10, "Ace of clubs": 11, "2 of spades": 2,
            "3 of spades": 3, "4 of spades": 4, "5 of spades": 5, "6 of spades": 6,
            "7 of spades": 7, "8 of spades": 8, "9 of spades": 9, "10 of spades": 10,
            "Jack of spades": 10, "Queen of spades": 10, "King of spades": 10, "Ace of spades": 11}

    return pack


# Shuffling the cards and dealing the pack in hands
def handling_cards(pack, hand):
    cards, value = random.choice(list(pack.items()))
    del pack[cards]
    hand[cards] = value


# Summation of card values in each hand of the player
def sum_of_totals(hand):
    # Calculate the total value of the hand
    count = sum(hand.values())
    # Count the number of Aces in the hand
    num_of_aces = list(hand.values()).count(11)
    while count > 21 and num_of_aces > 0:
        count -= 10
        num_of_aces -= 1
    return count


# Initiating the game
def start_game():
    # Create a deck of cards
    pack = forming_pack()
    # Initialize hands for player A and player B
    hand_a = {}
    hand_b = {}
    while len(pack) > 0:
        handling_cards(pack, hand_a)
        handling_cards(pack, hand_b)
        # Check if player A or player B has exceeded 21
        if sum_of_totals(hand_a) > 21:
            print("Player B Wins!")
            break
        elif sum_of_totals(hand_b) > 21:
            print("Player A Wins!")
            break
    else:
        print("No winner, as the total exceeded 21")
    # Print the hands and totals for player A and player B
    print("Player A's hand:", hand_a)
    print("Player A's total:", sum_of_totals(hand_a))
    print("Player B's hand:", hand_b)
    print("Player B's total:", sum_of_totals(hand_b))


# Call the Game function
start_game()
