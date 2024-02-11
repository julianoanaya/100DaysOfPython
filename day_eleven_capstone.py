import random

play_game = input(
    "Do you want to play a game of Blackjack? type 'y' for yes and 'n' for no "
)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_hand = []

if play_game == "y":
    for stating_hand in range(1, 3):
        random_card = random.choice(cards)
        user_cards.append(random_card)
    for computer_starting_hand in range(1, 3):
        random_card = random.choice(cards)
        computer_hand.append(random_card)

first_cards = user_cards[0]
second_card = user_cards[1]
score = first_cards + second_card
print(score)

print(f"Your cards: {user_cards}, current score: {score}")
print(f"Computer's first hand: {computer_hand[0]}")

# for current_user_score in range(1, user_hand + 1):
