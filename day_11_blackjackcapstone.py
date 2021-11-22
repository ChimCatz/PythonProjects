import random
from day11_art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dealCard = random.choice(cards)
    return dealCard


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(userScore, computerScore):
    if userScore == computerScore:
        return "Draw"
    elif computerScore == 0:
        return "Lose, opponent has Blackjack"
    elif userScore == 0:
        return "Win with a Blackjack"
    elif userScore > 21:
        return "You went over. You lose"
    elif computerScore > 21:
        return "Opponent went over. You win"
    elif userScore > computerScore:
        return "You win"
    else:
        return "You lose"

def play_game():

    print(logo)

    user_cards = []
    computer_cards = []
    isGameOver = False

    for _ in range (2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not isGameOver:

        userScore = calculate_score(user_cards)
        computerScore = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {userScore}")
        print(f"    Computer's first card: {computer_cards}")
        if userScore == 0 or computerScore == 0 or userScore > 21:
            isGameOver = True
        else:
            userShouldDeal = input("Type 'y' to get another card, type 'n' to pass: ")
            if userShouldDeal == "y":
                user_cards.append(deal_card())
            else:
                isGameOver = True

    #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computerScore != 0 and computerScore < 17:
        computer_cards.append(deal_card())
        computerScore = calculate_score(computer_cards)

    print(f"    Your final: {user_cards}, final score: {userScore}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computerScore}")
    print(compare(userScore, computerScore))
#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

while input("Do wou want to play a game of BLackjack? Type 'y' or 'n': ") == "y":
    play_game()